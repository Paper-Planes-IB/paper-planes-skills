#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bounded, read-only public website audit. Python 3.9+, standard library only."""
import argparse
import csv
import gzip
import hashlib
import io
import html
import ipaddress
import json
import re
import socket
import statistics
import time
import threading
from concurrent.futures import ThreadPoolExecutor
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ET
from collections import Counter, deque
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

VERSION = '0.2.0'
UA = 'PPWebsiteAudit/0.2'
UNKNOWN = 'не удалось измерить'


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def canonical_url(url, base=None):
    p = urllib.parse.urlsplit(urllib.parse.urljoin(base or '', url))
    if p.scheme not in ('http', 'https') or not p.hostname or p.username or p.password:
        return None
    return urllib.parse.urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path or '/', p.query, ''))


def key(url):
    return hashlib.sha256(url.encode()).hexdigest()[:20]


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    temporary.replace(path)


class PageParser(HTMLParser):
    def __init__(self, url):
        super().__init__(convert_charrefs=True)
        self.url = url
        self.base = url
        self.title = ''
        self.h1 = []
        self.text = []
        self.main_text = []
        self.meta = {}
        self.canonical = None
        self.links = []
        self.images = []
        self.resources = []
        self.jsonld = []
        self.forms = 0
        self.stack = []
        self.anchor = None
        self.json_buffer = None
        self.hidden = 0
        self.context = []
        self.body_chunks = []
        self.main_blocks = []
        self.fragment_ids = set()
        self.headings = []
        self.meta_values = {}
        self.canonical_candidates = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'): self.fragment_ids.add(a['id'])
        if tag == 'a' and a.get('name'): self.fragment_ids.add(a['name'])
        void = tag in ('area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr')
        excluded = tag in ('nav', 'header', 'footer', 'aside', 'form') or a.get('role') in ('navigation', 'banner', 'contentinfo') or bool(re.search(r'(?:^|[\s_-])(?:menu|footer|header|cookie|popup|modal)(?:$|[\s_-])|t228|t450|t477|t886|t972', a.get('class', '') + ' ' + a.get('id', ''), re.I))
        hidden = 'hidden' in a or a.get('aria-hidden') == 'true' or bool(re.search(r'display\s*:\s*none|visibility\s*:\s*hidden', a.get('style', ''), re.I))
        if not void: self.context.append({'tag': tag, 'excluded': excluded, 'hidden': hidden, 'block': tag in ('p', 'li', 'h1', 'h2', 'h3', 'h4', 'blockquote') or bool(re.search(r't(?:ext|itle|descr)|tn-atom', a.get('class', ''))), 'text': []})
        if tag not in ('area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'):
            self.stack.append(tag)
        if tag == 'base' and a.get('href'):
            self.base = canonical_url(a['href'], self.url) or self.base
        if tag == 'meta':
            name = (a.get('name') or a.get('property') or '').lower()
            self.meta[name] = a.get('content', '')
            self.meta_values.setdefault(name, []).append(a.get('content', ''))
        if tag == 'h1':
            self.h1.append('')
        if re.fullmatch(r'h[1-6]', tag): self.headings.append({'level': int(tag[1]), 'text': ''})
        if tag == 'link':
            rel = a.get('rel', '').lower().split()
            u = canonical_url(a.get('href', ''), self.base)
            if 'canonical' in rel:
                self.canonical = u
                self.canonical_candidates.append(u)
            if 'stylesheet' in rel and u:
                self.resources.append({'url': u, 'type': 'css', 'media': a.get('media'), 'in_head': 'head' in self.stack})
        if tag == 'script' and a.get('src'):
            u = canonical_url(a['src'], self.base)
            if u:
                self.resources.append({'url': u, 'type': 'js', 'async': 'async' in a, 'defer': 'defer' in a, 'module': a.get('type') == 'module', 'in_head': 'head' in self.stack})
        if tag == 'script' and a.get('type', '').lower() == 'application/ld+json':
            self.json_buffer = ''
        if tag == 'a':
            self.anchor = {'source': self.url, 'target': canonical_url(a.get('href', ''), self.base) if a.get('href') else None,
                           'href': a.get('href'), 'anchor': '', 'rel': a.get('rel', ''),
                           'fragment': urllib.parse.unquote(urllib.parse.urlsplit(urllib.parse.urljoin(self.base, a.get('href', ''))).fragment)}
            self.links.append(self.anchor)
        if tag == 'img':
            self.images.append({'src': canonical_url(a.get('src', ''), self.base) if a.get('src') else None,
                                'alt': a.get('alt'), 'width': a.get('width'), 'height': a.get('height'),
                                'loading': a.get('loading'), 'srcset': a.get('srcset'), 'sizes': a.get('sizes'),
                                'style': a.get('style', ''), 'fetchpriority': a.get('fetchpriority')})
        if tag == 'form':
            self.forms += 1

    def handle_endtag(self, tag):
        matches = [i for i, c in enumerate(self.context) if c['tag'] == tag]
        if matches:
            i = matches[-1]
            for c in self.context[i:]:
                if c['block'] and c['text']:
                    block = re.sub(r'\s+', ' ', ' '.join(c['text'])).strip()
                    if block and block not in self.main_blocks: self.main_blocks.append(block)
            del self.context[i:]
        if tag == 'script' and self.json_buffer is not None:
            try:
                self.jsonld.append({'valid': True, 'data': json.loads(self.json_buffer)})
            except (ValueError, TypeError):
                self.jsonld.append({'valid': False, 'snippet': self.json_buffer[:200]})
            self.json_buffer = None
        if tag == 'a':
            self.anchor = None
        if tag in self.stack:
            i = len(self.stack) - 1 - self.stack[::-1].index(tag)
            del self.stack[i:]

    def handle_data(self, data):
        if self.json_buffer is not None:
            self.json_buffer += data
        if 'head' in self.stack and 'title' in self.stack and 'svg' not in self.stack:
            self.title += data
        if 'h1' in self.stack and self.h1:
            self.h1[-1] += data
        if self.headings and any('h' + str(self.headings[-1]['level']) == t for t in self.stack): self.headings[-1]['text'] += data
        if self.anchor is not None:
            self.anchor['anchor'] += data.strip() + ' '
        if not any(t in self.stack for t in ('script', 'style', 'noscript', 'head')):
            if data.strip():
                self.text.append(data.strip())
                eligible = not any(c['excluded'] or c['hidden'] for c in self.context) and 'svg' not in self.stack
                if eligible:
                    self.body_chunks.append(data.strip())
                    for c in self.context:
                        if c['block']: c['text'].append(data.strip())
                    if 'main' in self.stack or 'article' in self.stack:
                        self.main_text.append(data.strip())

    def result(self):
        explicit = bool(self.main_text)
        content = self.main_text if explicit else self.body_chunks
        return {'title': self.title.strip(), 'h1': [s.strip() for s in self.h1],
                'description': self.meta.get('description'), 'robots': self.meta.get('robots', ''),
                'canonical': self.canonical, 'og': {k: v for k, v in self.meta.items() if k.startswith('og:')},
                'text': ' '.join(self.text), 'main_text': ' '.join(content), 'links': self.links,
                'content_extraction': {'method': 'main/article' if explicit else 'body_without_boilerplate', 'method_ru': 'main/article без служебных блоков' if explicit else 'текст body без навигации, подвала, скрытых и служебных блоков', 'confidence': 'высокая' if explicit else 'средняя', 'limitations': 'CSS-видимость и назначение блоков требуют браузерной проверки.'},
                'main_blocks': self.main_blocks, 'viewport': self.meta.get('viewport'), 'fragment_ids': sorted(self.fragment_ids),
                'headings': self.headings,
                'meta_values': self.meta_values, 'canonical_candidates': self.canonical_candidates,
                'images': self.images, 'resources': self.resources, 'jsonld': self.jsonld, 'forms': self.forms}


def parse_page(body, url):
    p = PageParser(url)
    p.feed(body)
    result = p.result()
    result['tracking'] = {'metrika_loader_count': len(re.findall(r'mc\.yandex\.(?:ru|com)/metrika', body, re.I)), 'ym_ids': sorted(set(re.findall(r'\bym\s*\(\s*[\"\']?(\d+)', body))), 'ym_init_count': len(re.findall(r'\bym\s*\([^,]+,\s*[\"\']init[\"\']', body))}
    return result


class StopRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Collector:
    def __init__(self, args, out):
        self.a = args
        self.out = out
        self.start = canonical_url(args.url)
        if not self.start:
            raise ValueError('Нужен публичный HTTP/HTTPS URL без credentials')
        s = urllib.parse.urlsplit(self.start)
        self.host = s.hostname
        self.netloc = s.netloc
        self.origin = urllib.parse.urlunsplit((s.scheme, s.netloc, '', '', ''))
        self.opener = urllib.request.build_opener(StopRedirect)
        self.count = 0
        self.last = 0
        self.rows = {}
        self.policies = {}
        self.sitemap_urls = set()
        self.sitemap_docs = []
        self.sitemap_complete = True
        self.pending = []
        self.excluded = []
        self.sitemap_locs = []
        self.lock = threading.Lock()
        self.policy_lock = threading.RLock()
        self.resume_history = []

    def internal(self, url):
        p = urllib.parse.urlsplit(url)
        return p.hostname == self.host and p.netloc == self.netloc

    def public(self, url):
        host = urllib.parse.urlsplit(url).hostname
        try:
            ips = socket.getaddrinfo(host, urllib.parse.urlsplit(url).port or 443, type=socket.SOCK_STREAM)
            return all(ipaddress.ip_address(x[4][0]).is_global or
                       (self.a.allow_local and ipaddress.ip_address(x[4][0]).is_loopback) for x in ips)
        except (socket.gaierror, ValueError):
            return False

    def request(self, url, policy=True, kind='page', request_headers=None, evidence_key=None):
        row = {'requested_url': url, 'kind': kind, 'at': timestamp(), 'chain': [], 'status': None,
               'final_url': url, 'headers': {}, 'error': None, 'raw_file': None, 'truncated': False}
        current = url
        for _ in range(11):
            if kind in ('page', 'http_probe') and urllib.parse.urlsplit(current).query and not self.a.include_query:
                row['error'] = 'параметрический URL вне согласованного охвата'; break
            if not self.internal(current):
                row['error'] = 'переход вне согласованного хоста'; break
            if not self.public(current):
                row['error'] = 'адрес не является доступным публичным хостом'; break
            if policy and not self.allowed(current):
                row['error'] = 'запрос запрещён robots или robots недоступен'; break
            delay = self.a.delay
            pol = self.policies.get(urllib.parse.urlsplit(current).scheme)
            if pol and pol.get('parser'):
                rp = pol['parser']
                rate = rp.request_rate(UA)
                delay = max(delay, rp.crawl_delay(UA) or 0, rate.seconds / rate.requests if rate and rate.requests else 0)
            # A single global start-slot lock preserves delay, robots rate and request budget across workers.
            with self.lock:
                if self.count >= self.a.max_requests:
                    row['error'] = 'достигнут лимит запросов'; break
                time.sleep(max(0, delay - (time.monotonic() - self.last)))
                self.last = time.monotonic()
                self.count += 1
            req = urllib.request.Request(current, headers={'User-Agent': UA, 'Accept-Encoding': 'identity', **(request_headers or {})})
            try:
                request_start = time.monotonic()
                try:
                    resp = urllib.request.build_opener(StopRedirect).open(req, timeout=self.a.timeout)
                except urllib.error.HTTPError as e:
                    resp = e
                with resp:
                    status = resp.code
                    headers = {k.lower(): v for k, v in resp.headers.items()}
                    first = resp.read(1)
                    ttfb = (time.monotonic() - request_start) * 1000
                    data = first + resp.read(self.a.max_bytes)
                row['chain'].append({'url': current, 'status': status, 'location': headers.get('location'), 'ttfb_ms': round(ttfb, 2)})
                row.update(status=status, final_url=current, headers=headers, truncated=len(data) > self.a.max_bytes)
                row['ttfb_ms'] = round(ttfb, 2)
                row['ttfb_method'] = 'GET: начало open → первый прочитанный байт; включает соединение/TLS/сервер, без предварительного DNS/robots guard и очереди'
                row['http_version'] = None  # urllib does not negotiate/measure HTTP/2.
                data = data[:self.a.max_bytes]
                if status in (301, 302, 303, 307, 308) and headers.get('location'):
                    target = canonical_url(headers['location'], current)
                    if not target or target in [x['url'] for x in row['chain']]:
                        row['error'] = 'некорректный или циклический редирект'; break
                    current = target
                    continue
                suffix = 'html' if 'text/html' in headers.get('content-type', '') else 'bin'
                raw = self.out / 'raw' / (key(evidence_key or url) + '.' + suffix)
                raw.write_bytes(data)
                row['raw_file'] = raw.relative_to(self.out).as_posix()
                charset = re.search(r'charset=([^;\s]+)', headers.get('content-type', ''), re.I)
                decoded = data
                if headers.get('content-encoding', '').lower() == 'gzip' and not row['truncated']:
                    try:
                        with gzip.GzipFile(fileobj=io.BytesIO(data)) as zipped: decoded = zipped.read(self.a.max_bytes + 1)
                        row['decoded_truncated'] = len(decoded) > self.a.max_bytes
                        decoded = decoded[:self.a.max_bytes]
                        row['truncated'] = row['truncated'] or row['decoded_truncated']
                    except (OSError, EOFError): row['decode_error'] = 'не удалось декодировать gzip'
                try:
                    body = decoded.decode(charset.group(1).strip('"') if charset else 'utf-8', errors='replace')
                except LookupError:
                    body = data.decode('utf-8', errors='replace')
                row['bytes'] = len(data)
                return row, body
            except (OSError, urllib.error.URLError, ValueError) as e:
                row['error'] = str(e); break
        else:
            row['error'] = 'слишком много редиректов'
        return row, ''

    def allowed(self, url):
        with self.policy_lock:
            return self._allowed(url)

    def _allowed(self, url):
        scheme = urllib.parse.urlsplit(url).scheme
        if scheme not in self.policies:
            robots_url = scheme + '://' + self.netloc + '/robots.txt'
            row, body = self.request(robots_url, policy=False, kind='robots')
            rp = urllib.robotparser.RobotFileParser()
            available = row['status'] is not None and not row['error'] and not row['truncated']
            if available and row['status'] == 200:
                rp.parse(body.splitlines())
                state = 'получен'
            elif available and row['status'] in (404, 410):
                rp.parse([]); state = 'отсутствует'
            else:
                state = 'доступ не подтверждён'; available = False
            self.policies[scheme] = {'parser': rp if available else None, 'row': row, 'state': state,
                                     'sitemaps': re.findall(r'^sitemap:\s*(\S+)', body, re.I | re.M) if available else []}
        p = self.policies[scheme]
        return p['parser'] is not None and p['parser'].can_fetch(UA, url)

    def sitemap(self):
        self.allowed(self.start)
        queue = deque(self.policies[urllib.parse.urlsplit(self.start).scheme]['sitemaps'] or [self.origin + '/sitemap.xml'])
        seen = set()
        while queue and len(seen) < self.a.max_sitemaps and len(self.sitemap_urls) < self.a.max_sitemap_urls:
            url = canonical_url(queue.popleft())
            if not url or url in seen:
                continue
            seen.add(url)
            if not self.internal(url):
                self.sitemap_complete = False; self.sitemap_docs.append({'requested_url': url, 'error': 'внешний sitemap не обследован'}); continue
            row, body = self.request(url, kind='sitemap')
            self.sitemap_docs.append(row)
            if row['status'] == 404 and not row['error']:
                continue
            if row['status'] != 200 or row['error'] or row['truncated']:
                self.sitemap_complete = False; continue
            try:
                root = ET.fromstring(body)
                locs = [canonical_url(e.text.strip()) for e in root.iter() if e.tag.split('}')[-1] == 'loc' and e.text]
                if root.tag.split('}')[-1] == 'sitemapindex':
                    queue.extend(x for x in locs if x)
                elif root.tag.split('}')[-1] == 'urlset':
                    for entry in root:
                        fields = {e.tag.split('}')[-1]: (e.text or '').strip() for e in entry}
                        if fields.get('loc'):
                            self.sitemap_locs.append({'url': canonical_url(fields['loc']), 'loc': fields['loc'], 'sitemap': url, 'lastmod': fields.get('lastmod'), 'position': len(self.sitemap_locs) + 1})
                    for u in locs:
                        if not u: continue
                        if self.internal(u) and len(self.sitemap_urls) < self.a.max_sitemap_urls:
                            self.sitemap_urls.add(u)
                        else:
                            self.sitemap_complete = False
                else:
                    self.sitemap_complete = False
            except ET.ParseError:
                row['parse_error'] = 'невалидный XML'; self.sitemap_complete = False
        if queue:
            self.sitemap_complete = False

    def checkpoint(self, progress=False):
        dump(self.out / 'raw/checkpoint.json', {'version': VERSION, 'site': self.start,
            'scope_config': {k: getattr(self.a, k, None) for k in ('profile', 'include_query', 'allow_local')},
            'at': timestamp(), 'rows': list(self.rows.values()), 'count': self.count,
            'sitemap_urls': sorted(self.sitemap_urls), 'sitemap_locs': self.sitemap_locs,
            'sitemaps': self.sitemap_docs, 'sitemap_complete': self.sitemap_complete,
            'resume_history': self.resume_history})
        if progress:
            dump(self.out / 'raw/pages.json', list(self.rows.values()))
            dump(self.out / 'raw/manifest.json', {'version': VERSION, 'at': timestamp(), 'site': self.start, 'profile': self.a.profile, 'config': vars(self.a), 'robots': [{k: v for k, v in p.items() if k != 'parser'} for p in self.policies.values()], 'coverage': {'pages': len(self.rows), 'requests': self.count, 'complete': False, 'pending': [], 'excluded': self.excluded, 'sitemap_complete': self.sitemap_complete, 'resource_total': 0, 'resource_sample': 0, 'state': 'обход выполняется'}, 'sitemap_urls': sorted(self.sitemap_urls), 'sitemap_locs': self.sitemap_locs, 'sitemaps': self.sitemap_docs})

    def resume(self):
        source = self.out / 'raw/checkpoint.json'
        if not source.exists(): raise ValueError('Нет checkpoint.json для безопасного продолжения')
        state = json.loads(source.read_text())
        expected = {k: getattr(self.a, k, None) for k in ('profile', 'include_query', 'allow_local')}
        if state.get('version') != VERSION or state.get('site') != self.start or state.get('scope_config') != expected:
            raise ValueError('Версия, хост или права продолжения расходятся с checkpoint')
        self.rows = {r['requested_url']: r for r in state['rows']}
        self.count = state['count']
        self.sitemap_urls = set(state['sitemap_urls'])
        self.sitemap_locs = state.get('sitemap_locs', [])
        self.sitemap_docs = state['sitemaps']
        self.sitemap_complete = state['sitemap_complete']
        self.resume_history = state.get('resume_history', []) + [{'at': timestamp(), 'from': state['at'], 'previous_requests': self.count}]

    def collect_http_probes(self, rows, series='http-probes-v2'):
        """Three comparable bounded gzip GETs and one conditional request per sampled HTML URL."""
        results = []
        eligible = [r for r in rows if r.get('page') and not r.get('error') and not r.get('truncated')]
        for original in eligible[:getattr(self.a, 'max_http_probes', 0)]:
            url = original['requested_url']
            for attempt in range(3):
                row, _ = self.request(url, request_headers={'Accept-Encoding': 'gzip'}, kind='http_probe', evidence_key=f'{series}:{url}:{attempt}')
                row.update(probe='gzip_repeat', attempt=attempt + 1, series=series); results.append(row)
            validator = {'If-None-Match': original['headers']['etag']} if original['headers'].get('etag') else ({'If-Modified-Since': original['headers']['last-modified']} if original['headers'].get('last-modified') else None)
            if validator:
                row, _ = self.request(url, request_headers=validator, kind='http_probe', evidence_key=series + ':conditional:' + url)
                row.update(probe='conditional', sent_validator=validator, series=series); results.append(row)
            else:
                results.append({'requested_url': url, 'probe': 'conditional', 'status': None, 'error': 'валидатор ETag/Last-Modified отсутствует; условный запрос не отправлен', 'at': timestamp(), 'series': series})
        return results

    def crawl(self):
        if getattr(self.a, 'resume', False):
            self.resume()
            self.allowed(self.start)  # Revalidate current robots; no cached permission is reused.
        else:
            self.sitemap()
        seeds = [canonical_url(u.strip(), self.start) for u in getattr(self.a, 'seed_urls', '').split(',') if u.strip()]
        if getattr(self.a, 'seed_file', None):
            supplied = json.loads(Path(self.a.seed_file).read_text())
            if not isinstance(supplied, list) or not all(isinstance(u, str) for u in supplied): raise ValueError('Seed-файл должен содержать JSON-массив URL')
            seeds += [canonical_url(u.strip(), self.start) for u in supplied[:self.a.max_pages]]
        if any(not u or not self.internal(u) for u in seeds): raise ValueError('Все seed URL должны принадлежать согласованному хосту')
        queue = deque([(self.start, 0)] + [(u, 0) for u in seeds if u != self.start] + [(u, 0) for u in sorted(self.sitemap_urls) if u != self.start])
        for old in self.rows.values():
            for link in old.get('page', {}).get('links', []):
                if link['target'] and self.internal(link['target']): queue.append((link['target'], old.get('discovery_depth', 0) + 1))
        seen = set(self.rows)
        workers = getattr(self.a, 'workers', 1)
        with ThreadPoolExecutor(max_workers=workers) as pool:
            while queue and len(self.rows) < self.a.max_pages and self.count < self.a.max_requests:
                batch = []
                while queue and len(batch) < workers and len(self.rows) + len(batch) < self.a.max_pages:
                    url, depth = queue.popleft()
                    if url in seen: continue
                    seen.add(url)
                    if depth > self.a.max_depth:
                        self.excluded.append({'url': url, 'reason': 'лимит глубины обнаружения'}); continue
                    if urllib.parse.urlsplit(url).query and not self.a.include_query:
                        self.excluded.append({'url': url, 'reason': 'параметрический URL вне охвата'}); continue
                    batch.append((url, depth))
                results = list(pool.map(lambda item: self.request(item[0]), batch))
                for (url, depth), (row, body) in zip(batch, results):
                    row['discovery_depth'] = depth  # Sitemap seeds are collection seeds, not navigation depth.
                    self.rows[url] = row
                    if row['status'] == 200 and 'text/html' in row['headers'].get('content-type', '') and not row['error']:
                        row['page'] = parse_page(body, row['final_url'])
                        for link in row['page']['links']:
                            u = link['target']
                            if u and self.internal(u) and u not in seen: queue.append((u, depth + 1))
                if len(self.rows) <= 8 or len(self.rows) % 20 < workers: self.checkpoint(progress=True)
        self.pending = sorted({u for u, _ in queue if u not in self.rows and u not in {x['url'] for x in self.excluded}})
        depths = navigation_depths(list(self.rows.values()), self.start)
        for r in self.rows.values():
            r['depth'] = depths.get(r['requested_url'], depths.get(r['final_url']))
            r['navigation_depth_status'] = 'измерено' if r['depth'] is not None else 'путь не обнаружен в обследованном графе'
        resources, images = {}, {}
        for row in self.rows.values():
            for item in row.get('page', {}).get('resources', []):
                if self.internal(item['url']): resources.setdefault(item['url'], item)
            for im in row.get('page', {}).get('images', []):
                if im['src'] and self.internal(im['src']): images.setdefault(im['src'], {'url': im['src'], 'source_url': row['requested_url']})
        self.resource_total = len(resources)
        def sample(items, limit, kind):
            def collect(item):
                row, _ = self.request(item['url'], kind=item.get('type', kind), evidence_key=kind + ':' + item['url'])
                if item.get('source_url'): row['source_url'] = item['source_url']
                return row
            with ThreadPoolExecutor(max_workers=workers) as pool:
                return list(pool.map(collect, list(items.values())[:limit]))
        self.resources = sample(resources, self.a.max_resources, 'resource')
        self.images = sample(images, getattr(self.a, 'max_images', 0), 'image')
        self.http_probes = []
        eligible = [r for r in self.rows.values() if r.get('page') and not r['error'] and not r['truncated']]
        for original in eligible[:getattr(self.a, 'max_http_probes', 0)]:
            url = original['requested_url']
            for attempt in range(3):
                row, _ = self.request(url, request_headers={'Accept-Encoding': 'gzip'}, kind='http_probe', evidence_key=f'probe:{url}:{attempt}')
                row['probe'] = 'gzip_repeat'; row['attempt'] = attempt + 1; self.http_probes.append(row)
            validator = {'If-None-Match': original['headers']['etag']} if original['headers'].get('etag') else ({'If-Modified-Since': original['headers']['last-modified']} if original['headers'].get('last-modified') else None)
            if validator:
                row, _ = self.request(url, request_headers=validator, kind='http_probe', evidence_key='conditional:' + url)
                row['probe'] = 'conditional'; row['sent_validator'] = validator; self.http_probes.append(row)
            else:
                self.http_probes.append({'requested_url': url, 'probe': 'conditional', 'status': None, 'error': 'валидатор ETag/Last-Modified отсутствует; условный запрос не отправлен', 'at': timestamp()})
        self.complete = not self.pending and not self.excluded and self.sitemap_complete and all(not r['error'] and not r['truncated'] for r in self.rows.values())
        manifest = {'version': VERSION, 'at': timestamp(), 'site': self.start, 'profile': self.a.profile,
                    'scope': 'публичные страницы одного хоста; GET; без авторизации и отправки форм',
                    'coverage': {'pages': len(self.rows), 'requests': self.count, 'complete': self.complete,
                                 'pending': self.pending, 'excluded': self.excluded, 'sitemap_complete': self.sitemap_complete,
                                 'resource_total': self.resource_total, 'resource_sample': len(self.resources),
                                 'image_total': len(images), 'image_sample': len(self.images), 'http_probe_rows': len(self.http_probes)},
                    'config': vars(self.a), 'robots': [{k: v for k, v in p.items() if k != 'parser'} for p in self.policies.values()],
                    'sitemap_urls': sorted(self.sitemap_urls), 'sitemap_locs': self.sitemap_locs, 'sitemaps': self.sitemap_docs,
                    'navigation_depths': depths, 'resume_history': self.resume_history,
                    'limitations': ['Доступность для индексации не доказывает фактическую индексацию.',
                                    'Внешние ссылки и ресурсы других хостов не запрашиваются HTTP-коллектором.',
                                    'Новые формы, покупки и изменения сайта не выполняются.',
                                    'Полнота относится к объявленному охвату, а не ко всем страницам сайта.',
                                    'urllib не измеряет HTTP/2; размер — сохранённые байты ответа, при усечении нижняя граница.',
                                    'Глубина навигации вычислена только по обследованным ссылкам от стартового URL; sitemap не даёт навигационное ребро.']}
        dump(self.out / 'raw/manifest.json', manifest)
        dump(self.out / 'raw/pages.json', list(self.rows.values()))
        dump(self.out / 'raw/resources.json', self.resources)
        dump(self.out / 'raw/images.json', self.images)
        dump(self.out / 'raw/http-probes.json', self.http_probes)
        self.checkpoint()
        return manifest


def navigation_depths(rows, start):
    adjacency = {}
    for r in rows:
        targets = [(l['target'], 1) for l in r.get('page', {}).get('links', []) if l.get('target')]
        if r.get('final_url') and r['final_url'] != r['requested_url']: targets.append((r['final_url'], 0))
        adjacency.setdefault(r['requested_url'], []).extend(targets)
        adjacency.setdefault(r.get('final_url', r['requested_url']), []).extend(targets)
    depths, queue = {start: 0}, deque([start])
    while queue:
        source = queue.popleft()
        for target, cost in adjacency.get(source, []):
            proposed = depths[source] + cost
            if proposed < depths.get(target, float('inf')):
                depths[target] = proposed
                (queue.appendleft if cost == 0 else queue.append)(target)
    return depths


def indexable(row):
    p = row.get('page')
    robots = (p or {}).get('robots', '') + ',' + row.get('headers', {}).get('x-robots-tag', '')
    return bool(p and row['status'] == 200 and not row['error'] and not re.search(r'\b(noindex|none)\b', robots, re.I))


def browser_summary(runs, min_clean=3):
    groups = {}
    for r in runs:
        group = (r['requested_url'], json.dumps(r['profile'], sort_keys=True))
        groups.setdefault(group, []).append(r)
    result = []
    for (url, profile), items in groups.items():
        clean = [r for r in items if r.get('ok') and r.get('same_url') and not r.get('network_failed') and r.get('navigation_status') == 200 and r.get('dom_usable', True) and r.get('speed_clean', True) and not r.get('diagnostic_perturbation')]
        enough = len(clean) >= min_clean
        result.append({'url': url, 'profile': json.loads(profile), 'runs': len(items), 'clean': len(clean),
                       'status': 'измерено' if enough else 'нужен повтор',
                       'median': {m: statistics.median([r[m] for r in clean if r.get(m) is not None])
                                  if enough and len([r for r in clean if r.get(m) is not None]) >= min_clean else None
                                  for m in ('lcp_ms', 'fcp_ms', 'cls', 'ttfb_ms')},
                       'limitations': 'Диагностическое наблюдение с инструментальной задержкой DNS/robots guard; для приёмки скорости нужен отдельный инструмент. INP и Lighthouse TBT не измерены.'})
    return result


def fragment_kind(fragment, ids=()):
    """Existing IDs take priority over portable hash-router/Tilda command candidates."""
    fragment = fragment or ''
    if fragment in ids: return 'целевой-якорь'
    if re.match(r'^(?:(?:submenu|popup):|/|!)', fragment, re.I): return 'программное-действие'
    return 'обычный-фрагмент'


def viewport_issues(page):
    """Diagnostic viewport candidates; not a claim of WCAG conformance."""
    value = page.get('viewport') or ''
    parts = dict(re.findall(r'([\w-]+)\s*=\s*([^,;]+)', value.lower()))
    def numeric(name):
        try: return float(parts.get(name, '').strip())
        except ValueError: return None
    reasons = []
    if not value or len(page.get('meta_values', {}).get('viewport', [])) != 1: reasons.append('viewport отсутствует или имеет несколько вхождений')
    if parts.get('width', '').strip() != 'device-width': reasons.append('width отличается от device-width')
    if numeric('initial-scale') != 1: reasons.append('initial-scale отсутствует либо отличается от 1')
    if parts.get('user-scalable', '').strip() in ('no', '0'): reasons.append('user-scalable запрещает масштабирование')
    maximum = numeric('maximum-scale')
    if maximum is not None and maximum <= 1: reasons.append('maximum-scale не допускает увеличение выше 1')
    return reasons


def content_similarity(rows, max_pages=1200, max_pairs=10000, near_threshold=.8, repeated_min_words=50):
    docs, frequency, postings, blocks = [], Counter(), {}, {}
    selected = sorted(rows, key=lambda r: r['requested_url'])[:max_pages]
    for r in selected:
        words = re.findall(r'\w+', r['page'].get('main_text', '').casefold())[:10000]
        shingles = {' '.join(words[i:i + 5]) for i in range(max(0, len(words) - 4))}
        docs.append((r['requested_url'], shingles)); frequency.update(shingles)
        for block in r['page'].get('main_blocks', []):
            normalized = re.sub(r'\s+', ' ', block.casefold()).strip()
            if len(normalized.split()) >= repeated_min_words: blocks.setdefault(normalized, set()).add(r['requested_url'])
    for i, (_, shingles) in enumerate(docs):
        for sh in shingles:
            if 1 < frequency[sh] <= 50: postings.setdefault(sh, []).append(i)
    candidates = {}
    for i, (_, shingles) in enumerate(docs):
        neighbors = Counter(j for sh in shingles for j in postings.get(sh, []) if j > i)
        for j, count in sorted(neighbors.items(), key=lambda item: (-item[1], item[0]))[:20]: candidates[(i, j)] = count
    near = []
    for (i, j), _ in sorted(candidates.items(), key=lambda item: (-item[1], item[0]))[:max_pairs]:
        a, b = docs[i][1], docs[j][1]
        similarity = len(a & b) / len(a | b) if a | b else 0
        if near_threshold <= similarity < 1 and len(a) >= 20 and len(b) >= 20:
            near.append({'left': docs[i][0], 'right': docs[j][0], 'jaccard': round(similarity, 5)})
    return {'method': 'детерминированные 5-словные шинглы; до 10000 слов/страницу, 20 кандидатов/страницу, частота шингла до 50 документов',
            'coverage': {'eligible_pages': len(rows), 'sample_pages': len(docs), 'candidate_pairs': len(candidates), 'compared_pairs': min(len(candidates), max_pairs), 'max_pages': max_pages, 'max_pairs': max_pairs},
            'pages': [{'url': url, 'shingles': len(sh), 'unique_share': round(sum(frequency[x] == 1 for x in sh) / len(sh), 5) if sh else None} for url, sh in docs],
            'near_pairs': near, 'repeated_blocks': [{'text': block[:1000], 'urls': sorted(urls), 'pages': len(urls)} for block, urls in sorted(blocks.items()) if len(urls) >= 3][:1000],
            'limitations': 'Кандидаты, не доказанные дубли. unique_share относится к извлечённому тексту и обследованной выборке. Exact-дубли проверяются отдельно.'}


def jsonld_nodes(value):
    if isinstance(value, list):
        for item in value: yield from jsonld_nodes(item)
    elif isinstance(value, dict):
        if '@type' in value: yield value
        for k, item in value.items():
            if k != '@context' and isinstance(item, (list, dict)): yield from jsonld_nodes(item)


def jsonld_semantic_candidates(page):
    issues, inventory = [], Counter()
    profiles = {'Product': ('name',), 'Service': ('name', 'provider'), 'BreadcrumbList': ('itemListElement',), 'Article': ('headline', 'author', 'datePublished'), 'NewsArticle': ('headline', 'author', 'datePublished'), 'BlogPosting': ('headline', 'author', 'datePublished'), 'Organization': ('name', 'url')}
    for script_index, script in enumerate(page.get('jsonld', [])):
        if not script['valid']: continue
        for node_index, node in enumerate(jsonld_nodes(script['data'])):
            types = node['@type'] if isinstance(node['@type'], list) else [node['@type']]
            for typ in types:
                if not isinstance(typ, str):
                    issues.append({'reason': '@type не является строкой', 'script': script_index, 'node': node_index}); continue
                typ = typ.rsplit('/', 1)[-1]; inventory[typ] += 1
                expected_types = {'name': (str, dict), 'headline': (str, dict), 'datePublished': (str,), 'dateModified': (str,), 'url': (str, dict), 'provider': (str, dict, list), 'author': (str, dict, list), 'offers': (str, dict, list), 'priceCurrency': (str,)}
                for field, allowed in expected_types.items():
                    if field in node and not isinstance(node[field], allowed):
                        issues.append({'reason': typ + '.' + field + ': кандидат несовместимого JSON-типа; сверить JSON-LD модель и профиль', 'script': script_index, 'node': node_index})
                if 'priceCurrency' in node and isinstance(node['priceCurrency'], str) and not re.fullmatch(r'[A-Z]{3}', node['priceCurrency']):
                    issues.append({'reason': 'priceCurrency: проверить трёхбуквенный код; валюта и актуальность подтверждаются источником', 'script': script_index, 'node': node_index})
                missing = [f for f in profiles.get(typ, ()) if not node.get(f)]
                if missing: issues.append({'reason': typ + ': отсутствуют поля минимального аудиторского профиля ' + ', '.join(missing), 'script': script_index, 'node': node_index})
                if typ == 'BreadcrumbList':
                    items = node.get('itemListElement')
                    if not isinstance(items, list): issues.append({'reason': 'BreadcrumbList.itemListElement ожидается как массив', 'script': script_index, 'node': node_index})
                    else:
                        for item in items:
                            if not isinstance(item, dict) or not item.get('position') or not item.get('name') or not item.get('item'):
                                issues.append({'reason': 'BreadcrumbList: проверить position/name/item элемента; конечный item может иметь допустимое исключение', 'script': script_index, 'node': node_index})
                if typ in ('Offer', 'AggregateOffer') and node.get('price') is not None:
                    try: float(str(node['price']).replace(',', '.'))
                    except ValueError: issues.append({'reason': 'price содержит нечисловой Text; Schema.org разрешает Text, пригодность для Google Product проверяется отдельно', 'script': script_index, 'node': node_index})
                if typ == 'FAQPage' and not isinstance(node.get('mainEntity'), list): issues.append({'reason': 'FAQPage: mainEntity ожидается как массив вопросов', 'script': script_index, 'node': node_index})
                if typ == 'Question':
                    answer = node.get('acceptedAnswer')
                    if not node.get('name') or not isinstance(answer, dict) or not answer.get('text'): issues.append({'reason': 'Question: проверить name и acceptedAnswer.text', 'script': script_index, 'node': node_index})
                    elif re.sub(r'\s+', ' ', str(node['name']).casefold()).strip() not in re.sub(r'\s+', ' ', page['text'].casefold()): issues.append({'reason': 'FAQ: текст вопроса не найден буквально в исходном HTML; требуется DOM/видимость', 'script': script_index, 'node': node_index})
                if typ == 'AggregateRating':
                    if node.get('ratingValue') is None or not (node.get('ratingCount') or node.get('reviewCount')): issues.append({'reason': 'AggregateRating: проверить ratingValue и ratingCount/reviewCount; источник и видимость требуют review', 'script': script_index, 'node': node_index})
                for field in ('datePublished', 'dateModified'):
                    if field in node and not re.match(r'^\d{4}-\d{2}-\d{2}(?:$|T)', str(node[field])): issues.append({'reason': field + ': кандидат несовместимого формата даты', 'script': script_index, 'node': node_index})
    return issues, dict(inventory)


class Report:
    def __init__(self, out):
        self.out = out
        self.checks = []
        self.details = []

    def add(self, cid, title, issues, action, acceptance, status='предупреждение', confidence='средняя',
            empty='пройдено', note=''):
        c = {'check_id': cid, 'title': title, 'status': status if issues else empty,
             'confidence': confidence if issues else 'средняя', 'count': len(issues), 'note': note,
             'action': action, 'acceptance': acceptance,
             'evidence': [{'file': 'report/details.csv', 'locator': 'check_id=' + cid}] if issues else
                         [{'file': 'raw/manifest.json', 'locator': 'coverage; interpreted with raw/pages.json'}],
             'next_check': 'Разработчик повторяет проверку на тех же URL после изменения.' if issues else ''}
        for issue in issues:
            if isinstance(issue, str): issue = {'url': issue}
            self.details.append({'check_id': cid, **issue})
        self.checks.append(c)

    def gate(self, cid, title, status, action, note):
        self.add(cid, title, [], action, 'Физический протокол проверки и источники сохранены.', empty=status, note=note)

    def write(self, manifest):
        tasks = []
        for c in self.checks:
            if c['status'] not in ('пройдено', 'не применимо'):
                tasks.append({'task_id': 'TASK-' + c['check_id'], 'check_id': c['check_id'],
                              'title': c['title'], 'kind': 'исправление' if c['status'] == 'ошибка' else
                              'запрос данных' if c['status'] == 'нужен доступ' else 'проверка или решение',
                              'priority': 'первая очередь' if c['status'] == 'ошибка' else 'следующая очередь',
                              'actor': 'владелец сайта / разработчик; персональный исполнитель не назначен',
                              'action': c['action'], 'acceptance': c['acceptance'], 'status': 'кандидат',
                              'evidence': c['evidence'], 'next_check': c['next_check']})
        dump(self.out / 'report/checks.json', self.checks)
        dump(self.out / 'report/tasks.json', tasks)
        fields = ['check_id', 'url', 'source_url', 'target', 'fragment', 'file', 'locator', 'source_type', 'rights', 'evidence_status', 'confidence', 'next_check']
        with (self.out / 'report/details.csv').open('w', encoding='utf-8-sig', newline='') as f:
            w = csv.DictWriter(f, fields, extrasaction='ignore'); w.writeheader()
            for row in self.details:
                row.setdefault('source_type', 'HTTP/HTML или браузерное наблюдение')
                row.setdefault('rights', 'публичный источник; внешняя публикация требует отдельного решения')
                row.setdefault('evidence_status', 'один-источник')
                row.setdefault('confidence', 'средняя')
                row.setdefault('next_check', 'Разработчик проверяет тот же адрес и критерий после изменения.')
                w.writerow(row)
        control = self.out / 'Контроль исправлений.csv'
        previous = {}
        if control.exists():
            with control.open(encoding='utf-8-sig', newline='') as f:
                previous = {r['ID задачи']: r for r in csv.DictReader(f)}
        with control.open('w', encoding='utf-8-sig', newline='') as f:
            w = csv.writer(f)
            w.writerow(['ID задачи', 'Проверка', 'Задача', 'Тип', 'Очередь', 'Действие', 'Приёмка', 'Состояние', 'Исполнитель', 'Версия сайта', 'Дата проверки', 'Доказательства'])
            for t in tasks:
                old = previous.get(t['task_id'], {})
                w.writerow([t['task_id'], t['check_id'], t['title'], t['kind'], t['priority'], t['action'], t['acceptance'],
                            old.get('Состояние', 'кандидат'), old.get('Исполнитель', ''), old.get('Версия сайта', ''),
                            old.get('Дата проверки', ''), old.get('Доказательства', '')])
            active = {t['task_id'] for t in tasks}
            for tid, old in previous.items():
                if tid not in active:
                    w.writerow([old.get(n, '') for n in ['ID задачи', 'Проверка', 'Задача', 'Тип', 'Очередь', 'Действие', 'Приёмка', 'Состояние', 'Исполнитель', 'Версия сайта', 'Дата проверки', 'Доказательства']])
        summary = Counter(c['status'] for c in self.checks)
        head = '# Технический аудит сайта\n\nСайт: ' + manifest['site'] + '\n\nДата UTC: ' + manifest['at'] + '\n\n'
        head += 'Охват: {} страниц; {} запросов; {}.\n\n'.format(manifest['coverage']['pages'], manifest['coverage']['requests'],
                    'обход завершён в объявленных границах' if manifest['coverage']['complete'] else 'обход частичный')
        head += 'Проверки: ' + ', '.join('{} — {}'.format(k, v) for k, v in summary.items()) + '.\n\n'
        self.out.joinpath('report/Резюме владельцу.md').write_text(head + '\n'.join(
            '- **{}** — {}. {}'.format(c['title'], c['status'], c['action']) for c in self.checks if c['status'] != 'пройдено') +
            '\n\nФактическая индексация, конверсия и коммерческий эффект этим обходом не установлены. Автоматические предупреждения требуют предметного review.\n', encoding='utf-8')
        self.out.joinpath('report/ТЗ разработчику.md').write_text(head + '\n\n'.join(
            '## {task_id} — {title}\n\nТип: {kind}. Очередь: {priority}.\n\nДействие: {action}\n\nПриёмка: {acceptance}\n\nАдреса и доказательства: details.csv, check_id={check_id}. Перепроверка: исходный HTTP/HTML, браузер и затронутый шаблон; новые доказательства и версия сайта.\n'.format(**t) for t in tasks), encoding='utf-8')
        self.out.joinpath('НАЧАТЬ ЗДЕСЬ.md').write_text(
            '# Пакет технического аудита\n\nНачните с report/Резюме владельцу.md и report/ТЗ разработчику.md.\n'
            'Проверки: report/checks.json; задачи: report/tasks.json; адресный trace: report/details.csv.\n'
            'Исходники: raw/manifest.json, raw/pages.json, raw/resources.json, сохранённые HTML/ответы; браузер — raw/browser.json, если выполнен.\n'
            'Существующий срез не изменять. Перепроверку выполнять в новом каталоге. Ни одна задача не назначена автоматически.\n'
            'Неизмеренное не подменять нулём. Необследованные адреса и ресурсы видны в manifest.\n', encoding='utf-8')
        sums = []
        for p in sorted(self.out.rglob('*')):
            if p.is_file() and p.name != 'MANIFEST.sha256':
                sums.append(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.relative_to(self.out).as_posix())
        self.out.joinpath('MANIFEST.sha256').write_text('\n'.join(sums) + '\n', encoding='utf-8')
        return summary


def analyse(out):
    manifest = json.loads((out / 'raw/manifest.json').read_text())
    rows = json.loads((out / 'raw/pages.json').read_text())
    resources = json.loads((out / 'raw/resources.json').read_text())
    images = json.loads((out / 'raw/images.json').read_text()) if (out / 'raw/images.json').exists() else []
    probe_file = out / 'raw/http-probes-3-repeat.json' if (out / 'raw/http-probes-3-repeat.json').exists() else out / 'raw/http-probes.json'
    probes = json.loads(probe_file.read_text()) if probe_file.exists() else []
    probe_source = probe_file.relative_to(out).as_posix()
    byurl = {r['requested_url']: r for r in rows}
    pages = [r for r in rows if r.get('page') and not r['truncated']]
    indexed = [r for r in pages if indexable(r)]
    sm = set(manifest['sitemap_urls'])
    rep = Report(out)

    def ev(r, fragment='', field='page'):
        return {'url': r['requested_url'], 'file': 'raw/pages.json', 'locator': 'requested_url=' + r['requested_url'] + '; ' + field,
                'fragment': fragment, 'evidence_status': 'один-источник', 'confidence': 'высокая'}

    rep.add('HTTP-01', 'Конечные HTTP-ошибки обследованных адресов', [ev(r, str(r['status']), 'status,chain') for r in rows if r['status'] and r['status'] >= 400 and not r['error']],
            'Разработчик устраняет ошибку; владелец определяет судьбу удалённой страницы.', 'Согласованный конечный код и отсутствие публичных ссылок на ошибочный адрес.', 'ошибка', 'высокая')
    rep.add('HTTP-02', 'Редиректы и их конечные адреса', [ev(r, json.dumps(r['chain'], ensure_ascii=False), 'chain') for r in rows if len(r['chain']) > 1],
            'Разработчик проверяет назначение переходов и сокращает избыточные цепочки.', 'Каждая цепочка соответствует назначению и приходит к согласованному адресу.')
    rep.add('HTTP-03', 'Недоступные, запрещённые или усечённые измерения', [ev(r, r['error'] or 'ответ усечён', 'error,truncated') for r in rows if r['error'] or r['truncated']],
            'Владелец уточняет доступ; аналитик повторяет измерение в разрешённых границах.', 'Есть полный ответ или явное исключение с причиной.', UNKNOWN)
    links = [l for r in pages for l in r['page']['links'] if l['target']]
    broken = []
    for l in links:
        r = byurl.get(l['target'])
        if r and r['status'] and r['status'] >= 400 and not r['error']:
            broken.append({**ev(r, '{} → {} ({})'.format(l['anchor'], l['target'], r['status']), 'chain'),
                           'source_url': l['source'], 'target': l['target']})
    rep.add('LINK-01', 'Внутренние ссылки с конечной HTTP-ошибкой', broken,
            'Разработчик исправляет общий компонент и все адресные вхождения; владелец выбирает цели.',
            'Все перечисленные вхождения ведут на действующие подходящие адреса.', 'ошибка', 'высокая',
            note='Вхождений: {}; уникальных исходных целей: {}; уникальных конечных целей: {}.'.format(len(broken), len({x['target'] for x in broken}), len({byurl[x['target']]['final_url'] for x in broken})))
    unchecked = sorted({l['target'] for l in links if l['target'] not in byurl})
    rep.gate('LINK-02', 'Необследованные цели ссылок', UNKNOWN if unchecked else 'пройдено',
             'Аналитик согласует расширение охвата; внешние ссылки проверяет отдельно.', '{} уникальных целей не запрашивались; это не подтверждённые ошибки.'.format(len(unchecked)))
    rep.add('LINK-03', 'Элементы a без href', [ev(r, 'Число: ' + str(sum(l['href'] is None for l in r['page']['links'])), 'page.links') for r in pages if any(l['href'] is None for l in r['page']['links'])],
            'Разработчик различает ссылки и действия: ссылка получает href, действие — доступную кнопку.', 'Семантика и клавиатурное управление проверены.')
    rep.add('LINK-08', 'Пустые href и общие анкоры — кандидаты', [ev(r, json.dumps({'href': l['href'], 'anchor': l['anchor']}, ensure_ascii=False), 'page.links') for r in pages for l in r['page']['links'] if l['href'] == '' or re.fullmatch(r'(?:подробнее|читать|узнать больше|здесь|click here|read more)\s*[.!…]?', l['anchor'].strip(), re.I)], 'Редактор проверяет понятность ссылки в контексте; разработчик различает ссылку и действие.', 'Назначение цели понятно из доступного имени и окружающего текста.', note='Общий анкор сам по себе не доказывает дефект; контекст и aria-label требуют DOM review.')
    link_inventory = [{'url': r['requested_url'], 'nofollow_count': sum('nofollow' in l.get('rel', '').lower().split() for l in r['page']['links']), 'query_targets': sorted({l['target'] for l in r['page']['links'] if l.get('target') and urllib.parse.urlsplit(l['target']).query}), 'pagination_candidates': [l for l in r['page']['links'] if l.get('href') and re.search(r'(?:[?&](?:page|p)=\d+|/page/\d+)', l['href'])]} for r in pages]
    dump(out / 'raw/link-inventory.json', link_inventory)
    incoming = Counter(l['target'] for l in links)
    reachable = {manifest['site']}
    # Redirect targets also connect the graph; sitemap itself is not a navigation edge.
    adjacency = {}
    for r in pages:
        adjacency[r['requested_url']] = [l['target'] for l in r['page']['links'] if l['target']] + [r['final_url']]
    while True:
        expanded = reachable | {u for v in reachable for u in adjacency.get(v, [])}
        if expanded == reachable: break
        reachable = expanded
    rep.add('LINK-04', 'Страницы sitemap без обнаруженных входящих ссылок', [ev(r, 'Входящих ссылок в обследованном графе: 0', 'page.links; raw/manifest.json') for r in indexed if r['requested_url'] in sm and not incoming[r['requested_url']] and r['requested_url'] != manifest['site']],
            'Владелец утверждает публикацию; редактор добавляет релевантные пути к нужным страницам.', 'Опубликованные страницы имеют входящие ссылки; черновики выведены из sitemap.', note='Частичный граф даёт только гипотезу; обход: ' + ('полный в объявленных границах' if manifest['coverage']['complete'] else 'частичный'))
    rep.add('LINK-05', 'Страницы вне обнаруженного пути от стартовой страницы', [ev(r, 'Путь от старта не обнаружен', 'page.links; raw/manifest.json') for r in indexed if r['requested_url'] not in reachable and r['final_url'] not in reachable],
            'Редактор связывает нужные страницы с достижимой навигацией.', 'Путь от согласованного старта найден.', note='Граф: ' + ('полный в объявленных границах' if manifest['coverage']['complete'] else 'частичный'))
    rep.add('LINK-09', 'Индексируемые страницы без входящих ссылок обследованного графа', [ev(r, 'Входящих: 0; sitemap=' + str(r['requested_url'] in sm), 'page.links') for r in indexed if r['requested_url'] != manifest['site'] and not incoming[r['requested_url']] and not incoming[r['final_url']]], 'Редактор проверяет публикацию и добавляет согласованные навигационные связи.', 'У нужных страниц есть достижимый вход; исключения обоснованы.', note='Включает адреса вне sitemap; частичный граф не доказывает сиротство на всём сайте.')
    rep.add('INDEX-01', 'Неиндексируемые или ошибочные адреса в sitemap', [ev(r, 'sitemap + noindex/HTTP', 'status,page.robots,headers.x-robots-tag') for r in rows if r['requested_url'] in sm and not r['error'] and not r['truncated'] and ((r.get('page') and not indexable(r)) or (r['status'] and r['status'] >= 400))],
            'Владелец выбирает режим публикации; разработчик согласует robots и sitemap.', 'В sitemap только согласованные индексируемые действующие адреса.', 'ошибка', 'высокая')
    rep.add('INDEX-02', 'Индексируемые адреса вне обследованного sitemap', [ev(r, 'URL вне sitemap', 'page.canonical; raw/manifest.json') for r in indexed if r['requested_url'] not in sm],
            'Владелец выбирает предназначенные для поиска страницы; разработчик добавляет их в карту.', 'Нужные страницы включены; исключения объяснены.', note='Обследование sitemap: ' + ('завершено' if manifest['coverage']['sitemap_complete'] else 'частичное'))
    rep.add('INDEX-03', 'Canonical отсутствует или отличается от конечного URL', [ev(r, str(r['page']['canonical']), 'page.canonical,final_url') for r in indexed if r['page']['canonical'] != r['final_url']],
            'Разработчик проверяет основной адрес и назначение альтернативных страниц.', 'Canonical соответствует утверждённой роли страницы; исключения документированы.')
    rep.add('INDEX-04', 'Редиректы в sitemap', [ev(r, r['final_url'], 'chain,final_url') for r in rows if r['requested_url'] in sm and len(r['chain']) > 1],
            'Разработчик сверяет loc с утверждёнными конечными canonical-адресами.', 'Карта содержит согласованные конечные адреса; исключения обоснованы.')
    sm_counts = Counter(x['url'] for x in manifest.get('sitemap_locs', []) if x.get('url'))
    rep.add('INDEX-05', 'Повторные loc в обследованных sitemap', [{'url': u, 'file': 'raw/manifest.json', 'locator': 'sitemap_locs', 'fragment': 'Вхождений loc: ' + str(n)} for u, n in sm_counts.items() if n > 1], 'Разработчик проверяет и устраняет необоснованные повторения loc.', 'Повторения исключены или объяснены.', empty='пройдено' if manifest.get('sitemap_locs') else UNKNOWN)
    depths = navigation_depths(rows, manifest['site'])
    rep.add('LINK-07', 'Глубина навигации выше принятого диагностического порога — кандидат', [ev(r, 'Глубина: ' + str(depths[r['requested_url']]), 'page.links; navigation_depths') for r in indexed if depths.get(r['requested_url'], 0) > manifest.get('config', {}).get('navigation_depth_threshold', 4)], 'Редактор проверяет важность страницы и длину пути посетителя.', 'Для значимых страниц принят обоснованный путь.', note='Диагностический порог: {} переходов; не универсальный норматив. Sitemap не считается переходом.'.format(manifest.get('config', {}).get('navigation_depth_threshold', 4)))
    fragments, fragment_unknown, functional_fragments = [], [], []
    regular_fragments = 0
    final_pages = {r['final_url']: r for r in pages}
    for link in links:
        if not link.get('fragment') or urllib.parse.urlsplit(link['target']).netloc != urllib.parse.urlsplit(manifest['site']).netloc: continue
        target = byurl.get(link['target']) or final_pages.get(link['target'])
        if not target or not target.get('page') or target['truncated'] or target['error']:
            fragment_unknown.append(link); continue
        kind = fragment_kind(link['fragment'], target['page'].get('fragment_ids', []))
        if kind == 'программное-действие':
            functional_fragments.append({'url': link['source'], 'target': link['target'] + '#' + link['fragment'], 'file': 'raw/pages.json', 'locator': 'page.links; fragment_kind', 'fragment': 'Кандидат программного меню, popup или hash-router; требуется проверка функции в интерфейсе, не диагноз отсутствующего ID.'})
            continue
        regular_fragments += 1
        if kind != 'целевой-якорь':
            fragments.append({'url': link['source'], 'target': link['target'] + '#' + link['fragment'], 'file': 'raw/pages.json', 'locator': 'page.links + target.page.fragment_ids', 'fragment': 'Идентификатор обычного якоря не найден в исходном HTML; DOM может добавить его динамически.'})
    rep.add('LINK-06', 'Цели обычных якорных ссылок не найдены в исходном HTML — кандидаты', fragments, 'Разработчик сверяет обычные фрагменты с DOM и исправляет подтверждённые цели.', 'Названный блок существует и доступен после перехода.', empty=UNKNOWN if fragment_unknown else 'пройдено' if regular_fragments else 'не применимо', note='Обычных якорей: {}; программных кандидатов: {}; необследованных целей: {}. Функциональные фрагменты проверяются отдельно в LINK-10.'.format(regular_fragments, len(functional_fragments), len(fragment_unknown)))
    rep.add('LINK-10', 'Программные фрагменты ссылок — требуется проверка функции', functional_fragments, 'Разработчик проверяет запуск меню, popup или hash-router в разрешённом сценарии без отправки форм.', 'Функция ссылки и доступное управление подтверждены интерфейсной проверкой.', status='требует проверки', empty='не применимо' if pages else UNKNOWN, note='Известные префиксы submenu:, popup:, / и ! дают функционального кандидата, не доказательство работающего обработчика. Реальный существующий ID имеет приоритет.')
    for cid, title, pred, action, accept in [
        ('HTML-01', 'Пустые или шаблонные Title', lambda p: not p['title'] or bool(re.search(r'blank page|copy of', p['title'], re.I)), 'Редактор подтверждает публикацию и задаёт предметный Title.', 'Опубликованные страницы имеют собственный точный Title.'),
        ('HTML-02', 'Число содержательных H1 отличается от одного', lambda p: len(p['h1']) != 1 or not p['h1'][0].strip(), 'Редактор и разработчик задают один предметный H1 в исходном шаблоне.', 'На опубликованных страницах один содержательный H1; исключения обоснованы.'),
        ('HTML-03', 'Description отсутствует', lambda p: not p['description'], 'Редактор задаёт описание важных опубликованных страниц.', 'Описание соответствует содержанию страницы.'),
        ('HTML-04', 'Значимые Open Graph поля отсутствуют', lambda p: not all(p['og'].get(k) for k in ('og:title', 'og:type', 'og:image')), 'Редактор и разработчик согласуют превью публичных страниц.', 'Превью соответствует фактическому содержанию.'),
        ('HTML-05', 'Короткое основное содержание — кандидат', lambda p: bool(p['main_text']) and len(p['main_text'].split()) < 50, 'Редактор проверяет назначение и DOM; выбирает публикацию или доработку.', 'Роль и достаточность содержания подтверждены; порог не заменяет review.'),
        ('DATA-01', 'Невалидный JSON в JSON-LD', lambda p: any(not x['valid'] for x in p['jsonld']), 'Разработчик исправляет синтаксис JSON-LD.', 'JSON разбирается; семантика отдельно проверена валидатором.')]:
        rep.add(cid, title, [ev(r, r['page']['title'], 'page') for r in indexed if pred(r['page'])], action, accept,
                status='ошибка' if cid == 'DATA-01' else 'предупреждение', note='Публикационный статус и DOM проверяются отдельно.')
    for cid, title, field in [('DUP-01', 'Совпадающие Title', 'title'), ('DUP-02', 'Совпадающие description', 'description'), ('DUP-03', 'Совпадающий извлечённый основной текст', 'main_text')]:
        groups = {}
        for r in indexed:
            value = re.sub(r'\s+', ' ', r['page'].get(field) or '').strip()
            if value:
                groups.setdefault(value, []).append(r)
        issues = [ev(r, value[:200], 'page.' + field) for value, group in groups.items() if len(group) > 1 and len({r['final_url'] for r in group}) > 1 for r in group]
        rep.add(cid, title, issues, 'Редактор проверяет группы, различает допустимый шаблон и дубль; владелец согласует объединение.', 'У каждого адреса обоснована собственная роль или выбран основной адрес.', note='Это кандидаты: одинаковый текст не доказывает одинаковый предмет.')
    near_threshold = manifest.get('config', {}).get('near_threshold', .8)
    unique_threshold = manifest.get('config', {}).get('unique_share_threshold', .4)
    block_words = manifest.get('config', {}).get('repeated_block_words', 50)
    content = content_similarity(indexed, near_threshold=near_threshold, repeated_min_words=block_words)
    dump(out / 'raw/content-analysis.json', content)
    cev = lambda url, fragment: {'url': url, 'file': 'raw/content-analysis.json', 'locator': 'url=' + url, 'fragment': fragment}
    rep.add('DUP-04', 'Близкие основные тексты — пары кандидатов', [{**cev(x['left'], 'Jaccard 5-словных шинглов: ' + str(x['jaccard'])), 'target': x['right']} for x in content['near_pairs']], 'Редактор читает обе страницы и различает сходство, допустимый шаблон и дубль.', 'Роли обеих страниц объяснены; решение сохраняет необходимые материалы.', note=content['method'] + '; ' + content['limitations'])
    rep.add('DUP-05', 'Низкая доля уникальных шинглов — кандидат', [cev(x['url'], 'unique_share=' + str(x['unique_share'])) for x in content['pages'] if x['shingles'] >= 20 and x['unique_share'] is not None and x['unique_share'] < unique_threshold], 'Редактор проверяет долю шаблонных блоков и собственную роль страницы.', 'Достаточность собственного содержания подтверждена.', note='Диагностический порог {:.0%}; доля 5-словных шинглов с частотой 1 измерена среди обследованных документов, без CSS-видимости.'.format(unique_threshold))
    rep.add('DUP-06', 'Повторные извлечённые блоки содержания — кандидаты', [cev(u, 'Страниц: {}; блок: {}'.format(x['pages'], x['text'][:200])) for x in content['repeated_blocks'] for u in x['urls']], 'Редактор отличает полезные повторные компоненты от необоснованного дублирования.', 'Повторные блоки имеют подтверждённое назначение.', note='Минимум {} слов и 3 страницы; не доказательство SEO-ущерба.'.format(block_words))
    semantic, inventories = [], []
    for r in indexed:
        candidates, inventory = jsonld_semantic_candidates(r['page'])
        inventories.append({'url': r['requested_url'], 'types': inventory})
        semantic.extend(ev(r, json.dumps(x, ensure_ascii=False), 'page.jsonld') for x in candidates)
    dump(out / 'raw/jsonld-inventory.json', inventories)
    rep.add('DATA-02', 'Семантические кандидаты JSON-LD по аудиторским профилям', semantic, 'Разработчик и редактор сверяют типы, поля, видимое содержание и профиль поисковой системы.', 'Схема и публичные факты согласованы; право на rich results проверено отдельно.', note='Минимальный аудиторский профиль не является списком обязательных полей Schema.org. Service и валидный JSON не обещают rich results.', empty='пройдено' if any(x['types'] for x in inventories) else 'не применимо')
    rep.add('HTML-06', 'Meta viewport отсутствует или неоднозначен', [ev(r, json.dumps({'viewport': r['page'].get('viewport'), 'candidates': viewport_issues(r['page'])}, ensure_ascii=False), 'page.viewport,meta_values') for r in pages if viewport_issues(r['page'])], 'Разработчик задаёт согласованный viewport и проверяет мобильный DOM.', 'Viewport соответствует мобильному интерфейсу; переполнение и фактическое масштабирование проверены отдельно.', note='Диагностические кандидаты: width!=device-width, initial-scale отсутствует/не 1, user-scalable=no/0, maximum-scale<=1; не вердикт соответствия WCAG.')
    rep.add('HTML-07', 'Скачки уровней заголовков — кандидаты', [ev(r, json.dumps(r['page'].get('headings'), ensure_ascii=False), 'page.headings') for r in pages if any(b['level'] > a['level'] + 1 for a, b in zip(r['page'].get('headings', []), r['page'].get('headings', [])[1:]))], 'Редактор проверяет логическую вложенность разделов.', 'Порядок заголовков отражает структуру; исключения обоснованы.')
    rep.add('HTML-08', 'Несколько canonical или meta robots', [ev(r, json.dumps({'canonical': r['page'].get('canonical_candidates'), 'robots': r['page'].get('meta_values', {}).get('robots'), 'header_link': r['headers'].get('link')}, ensure_ascii=False), 'page.canonical_candidates,page.meta_values,headers.link') for r in pages if len(r['page'].get('canonical_candidates', [])) > 1 or len(r['page'].get('meta_values', {}).get('robots', [])) > 1], 'Разработчик проверяет конфликты и задаёт единое согласованное указание.', 'Указания согласованы в HTML и заголовках.')
    rep.add('HTML-09', 'Длина description вне диагностического диапазона', [ev(r, 'Символов: ' + str(len(r['page']['description'])), 'page.description') for r in indexed if r['page'].get('description') and not 110 <= len(r['page']['description']) <= 160], 'Редактор проверяет смысл и отображение описания.', 'Смысл соответствует странице; универсальная длина не используется как правило ранжирования.', note='110–160 символов — только диагностический диапазон, отображение зависит от запроса и интерфейса.')
    rep.add('HTTP-07', 'HTTP 200 с признаками страницы ошибки — кандидат soft 404', [ev(r, r['page']['main_text'][:200], 'status,page.main_text') for r in pages if len(r['page']['main_text'].split()) < 100 and re.search(r'страница не найдена|page not found|ошибка 404', r['page']['main_text'], re.I)], 'Владелец проверяет назначение; разработчик возвращает согласованный HTTP-код.', 'Содержание и статус соответствуют назначению.', note='Эвристика не доказывает фактический soft 404 в поисковой системе.')
    rep.add('INDEX-06', 'Технические адреса pageNNN.html — кандидаты публикационного review', [ev(r, r['requested_url'], 'requested_url') for r in indexed if re.search(r'/page\d+\.html$', urllib.parse.urlsplit(r['requested_url']).path)], 'Владелец определяет назначение технических адресов и актуальный canonical.', 'Роли и судьба адресов явно приняты.')
    rep.add('RESOURCE-03', 'Синхронные ресурсы в head — кандидаты блокировки рендера', [ev(r, json.dumps(item, ensure_ascii=False), 'page.resources') for r in pages for item in r['page']['resources'] if item.get('in_head') and ((item['type'] == 'js' and not item.get('async') and not item.get('defer') and not item.get('module')) or (item['type'] == 'css' and item.get('media') in (None, '', 'all', 'screen')))], 'Разработчик проверяет критический путь браузерным профилем; меняет загрузку после проверки зависимостей.', 'Критический путь измерен, функции страницы сохранены.', note='HTML даёт кандидат; реальное блокирование и выигрыш времени требуют трассы браузера.')
    font_candidates, font_eligible = [], 0
    for resource in resources:
        if resource.get('kind') != 'css' or resource.get('status') != 200 or resource.get('error') or resource.get('truncated') or not resource.get('raw_file'): continue
        source = out / resource['raw_file']
        if not source.exists(): continue
        font_eligible += 1
        for face in re.findall(r'@font-face\s*\{([^}]+)\}', source.read_text(encoding='utf-8', errors='replace'), re.I):
            if not re.search(r'font-display\s*:', face, re.I): font_candidates.append({'url': resource['requested_url'], 'file': resource['raw_file'], 'locator': '@font-face', 'fragment': face[:400]})
    rep.add('RESOURCE-04', '@font-face без font-display в HTTP-выборке CSS — кандидат', font_candidates, 'Разработчик проверяет используемый шрифт и политику появления текста.', 'Выбранный режим соответствует читаемости и визуальной стабильности.', empty='пройдено' if font_eligible else UNKNOWN, note='Внешние CSS и непроверенная часть ресурсов исключены; наличие font-display не доказывает отсутствие сдвигов.')
    robots_inventory = []
    for policy in manifest.get('robots', []):
        rr = policy.get('row', {}); source = out / rr.get('raw_file', '')
        if policy.get('state') not in ('получен', 'отсутствует') or not source.is_file(): continue
        body = source.read_text(encoding='utf-8', errors='replace') if rr.get('status') == 200 else ''
        parser = urllib.robotparser.RobotFileParser(); parser.parse(body.splitlines())
        robots_inventory.append({'url': rr.get('requested_url'), 'file': rr.get('raw_file'), 'directives': [line for line in body.splitlines() if re.match(r'\s*(?:user-agent|disallow|allow|crawl-delay|request-rate|sitemap)\s*:', line, re.I)], 'agents': [{'agent': agent, 'start_allowed': parser.can_fetch(agent, manifest['site']), 'blocked_sample_urls': [r['requested_url'] for r in indexed if not parser.can_fetch(agent, r['requested_url'])][:100]} for agent in ('OAI-SearchBot', 'PerplexityBot', 'YandexAdditional')]})
    dump(out / 'raw/robots-policies.json', robots_inventory)
    rep.gate('ROBOTS-01', 'Публичные директивы robots и доступ указанных ботов', 'измерено' if robots_inventory else UNKNOWN, 'Владелец сверяет директивы с принятой политикой; фактический доступ подтверждает логами.', 'raw/robots-policies.json: директивы и can_fetch для OAI-SearchBot, PerplexityBot, YandexAdditional. Это robots-only наблюдение, не индексация и не подтверждённый визит бота.')
    rep.gate('TRACK-01', 'Публичные сигнатуры Яндекс Метрики в исходном HTML', 'измерено' if pages and all('tracking' in r['page'] for r in pages) else UNKNOWN, 'Владелец предоставляет доступ к аналитике; разработчик сверяет loader, ym IDs и реальные события.', 'raw/pages.json page.tracking: loader count, ym IDs, init count. Сигнатура не доказывает передачу событий, настройки или конверсию.')
    rep.add('IMAGE-01', 'Изображения без атрибута alt', [ev(r, im['src'] or '', 'page.images') for r in pages for im in r['page']['images'] if im['alt'] is None],
            'Редактор задаёт alt содержательным изображениям и alt="" декоративным.', 'Назначение каждого изображения подтверждено; атрибут задан.')
    rep.add('IMAGE-02', 'Размеры изображения не заданы в HTML — кандидат', [ev(r, im['src'] or '', 'page.images') for r in pages for im in r['page']['images'] if not (im['width'] and im['height']) and 'aspect-ratio' not in im['style']],
            'Разработчик проверяет CSS/DOM и резервирует место там, где его нет.', 'Место зарезервировано до загрузки; браузерная проверка не показывает связанного сдвига.', note='Размер может задаваться во внешнем CSS; отсутствие HTML-атрибутов не доказывает CLS.')
    iev = lambda r, fragment: {'url': r['requested_url'], 'source_url': r.get('source_url', ''), 'file': 'raw/images.json', 'locator': 'requested_url=' + r['requested_url'], 'fragment': fragment}
    valid_images = [r for r in images if r.get('status') is not None and not r.get('error') and not r.get('truncated')]
    rep.add('IMAGE-03', 'HTTP-ошибки изображений обследованной выборки', [iev(r, str(r['status'])) for r in valid_images if r['status'] >= 400], 'Разработчик устраняет подтверждённые ошибки источников изображений.', 'Согласованные источники доступны и содержат изображение.', status='ошибка', empty='пройдено' if valid_images else UNKNOWN)
    rep.gate('IMAGE-04', 'Охват HTTP-выборки изображений', 'измерено' if images and len(valid_images) == len(images) and len(images) == manifest['coverage'].get('image_total') else UNKNOWN, 'Аналитик расширяет или повторяет выборку в согласованных лимитах.', 'Проверено {} из {} внутренних img src; успешных полных ответов {}. CSS-background, srcset-only и внешние изображения сюда не входят.'.format(len(images), manifest['coverage'].get('image_total', 'не измерено'), len(valid_images)))
    rep.add('IMAGE-05', 'Размер или Content-Type изображений — кандидаты', [iev(r, json.dumps({'bytes': r.get('bytes'), 'content_length': r['headers'].get('content-length'), 'content_type': r['headers'].get('content-type'), 'cache_control': r['headers'].get('cache-control')}, ensure_ascii=False)) for r in valid_images if r['status'] == 200 and ((r.get('bytes') or 0) > 200 * 1024 or ('jpeg' in r['headers'].get('content-type', '').lower() and (r.get('bytes') or 0) > 100 * 1024) or not r['headers'].get('content-type', '').lower().startswith('image/'))], 'Разработчик проверяет формат и назначение изображения; оптимизирует после визуального сравнения.', 'Формат корректен; вес соответствует принятому бюджету и качеству.', empty='пройдено' if valid_images else UNKNOWN, note='Диагностические классы 200–400 / свыше 400 KiB; JPEG свыше 100 KiB — кандидат сравнения современного формата. Качество и фактический бюджет задаёт владелец; вес не доказывает лишний размер визуала.')
    rep.add('IMAGE-06', 'Политика кэширования изображений требует review', [iev(r, json.dumps({k: r['headers'].get(k) for k in ('cache-control', 'expires', 'etag', 'last-modified')}, ensure_ascii=False)) for r in valid_images if r['status'] == 200 and (not r['headers'].get('cache-control') and not r['headers'].get('expires') or 'no-store' in r['headers'].get('cache-control', '').lower() or (re.search(r'(?:s-)?max-age\s*=\s*(\d+)', r['headers'].get('cache-control', ''), re.I) and int(re.search(r'(?:s-)?max-age\s*=\s*(\d+)', r['headers'].get('cache-control', ''), re.I).group(1)) < 86400))], 'Разработчик сверяет срок жизни и версионирование ресурсов с политикой кэша.', 'Политика согласована; обновления ресурса наблюдаемы.', empty='пройдено' if valid_images else UNKNOWN, note='Сигналы: нет политики, no-store или max-age/s-maxage меньше 86400 секунд. Короткий кэш может быть необходим по назначению.')
    rep.add('IMAGE-07', 'Несколько изображений с fetchpriority=high — кандидат', [ev(r, 'Число high: ' + str(sum(im.get('fetchpriority') == 'high' for im in r['page']['images'])), 'page.images.fetchpriority') for r in pages if sum(im.get('fetchpriority') == 'high' for im in r['page']['images']) > 1], 'Разработчик проверяет конкуренцию приоритетов и фактический LCP.', 'Приоритет соответствует критическому визуалу и принятому бюджету.', note='Множественный high сам по себе не доказывает задержку LCP.')
    repeats = [r for r in probes if r.get('probe') == 'gzip_repeat' and r.get('status') == 200 and not r.get('error') and not r.get('truncated')]
    conditionals = [r for r in probes if r.get('probe') == 'conditional' and r.get('sent_validator') and r.get('status') is not None and not r.get('error')]
    rep.gate('HTTP-04', 'Прямые повторные наблюдения TTFB', 'измерено' if repeats and all(sum(x['requested_url'] == r['requested_url'] and x.get('ttfb_ms') is not None for x in repeats) >= 3 for r in repeats) else UNKNOWN, 'Аналитик проверяет стабильность на тех же URL; владелец задаёт бюджет.', 'raw/http-probes.json: три повторных GET на каждый выбранный URL; время включает соединение/TLS/сервер. Это не browser TTFB и не полевая метрика.')
    grouped_probes = {}
    for r in repeats:
        if r.get('ttfb_ms') is not None: grouped_probes.setdefault(r['requested_url'], []).append(r)
    ttfb_summary = []
    for url, samples in sorted(grouped_probes.items()):
        values = [r['ttfb_ms'] for r in samples]
        ttfb_summary.append({'url': url, 'samples': len(values), 'median_ms': statistics.median(values) if len(values) >= 3 else None, 'min_ms': min(values), 'max_ms': max(values), 'max_min_ratio': max(values)/min(values) if min(values) > 0 else None, 'status': 'измерено' if len(values) >= 3 else 'нужен повтор', 'source': probe_source, 'method': 'одинаковый GET Accept-Encoding gzip; urllib соединение/TLS/сервер до первого прочитанного байта'})
    dump(out / 'report/http-probe-summary.json', ttfb_summary)
    rep.add('HTTP-08', 'Нестабильность прямых повторов TTFB — кандидат', [{'url': x['url'], 'file': 'report/http-probe-summary.json', 'locator': 'url=' + x['url'], 'fragment': json.dumps(x, ensure_ascii=False)} for x in ttfb_summary if x['samples'] >= 3 and x['max_min_ratio'] is not None and x['max_min_ratio'] > 1.3], 'Аналитик повторяет сопоставимую серию; разработчик сопоставляет ответы с CDN/серверной трассой.', 'Стабильность и бюджет приняты по сопоставимым данным.', empty='измерено' if ttfb_summary and all(x['samples'] >= 3 for x in ttfb_summary) else UNKNOWN, note='max/min >1.3 — диагностический кандидат; три повтора не заменяют распределение реальных посетителей.')
    rep.add('HTTP-05', 'Условные GET с серверным валидатором', [{'url': r['requested_url'], 'file': probe_source, 'locator': 'probe=conditional', 'fragment': json.dumps({'status': r['status'], 'sent_validator': r['sent_validator']}, ensure_ascii=False)} for r in conditionals if r['status'] != 304], 'Разработчик сверяет валидатор и изменение содержимого; 200 может быть корректным при изменении ресурса.', 'Условная реакция соответствует версии ресурса.', empty='измерено' if conditionals else UNKNOWN, note='304 подтверждён только для указанного URL/валидатора/момента; отсутствие валидатора — пробел, а не ноль.')
    rep.add('HTTP-06', 'Сжатие при прямом GET Accept-Encoding: gzip', [{'url': r['requested_url'], 'file': probe_source, 'locator': 'probe=gzip_repeat', 'fragment': json.dumps({'content_encoding': r['headers'].get('content-encoding'), 'bytes': r.get('bytes')}, ensure_ascii=False)} for r in repeats if not r['headers'].get('content-encoding')], 'Разработчик проверяет gzip и условия CDN/сервера; сопоставляет текстовый ответ и вес.', 'Ответ выбранного текстового URL имеет согласованное сжатие либо обоснованное исключение.', empty='измерено' if repeats else UNKNOWN, note='Измерен gzip; Brotli и HTTP/2 не подтверждены этим клиентом.')
    rep.add('RESOURCE-01', 'HTTP-ошибки обследованных CSS/JS', [{'url': r['requested_url'], 'file': 'raw/resources.json', 'locator': 'requested_url=' + r['requested_url'], 'fragment': str(r['status'])} for r in resources if r['status'] and r['status'] >= 400 and not r['error']],
            'Разработчик восстанавливает ресурс или удаляет неверное подключение; проверяет функции и вид.', 'Ресурс доступен или не запрашивается; соседние функции сохранены.', 'ошибка', 'высокая')
    unresolved_resources = [r for r in resources if r['error'] or r['truncated']]
    rep.gate('RESOURCE-02', 'Охват ресурсов', UNKNOWN if unresolved_resources or len(resources) < manifest['coverage']['resource_total'] else 'пройдено',
             'Аналитик расширяет выборку в согласованных лимитах.', 'Проверено {} из {} уникальных внутренних CSS/JS; неопределённых {}. Внешние ресурсы вне HTTP-выборки.'.format(len(resources), manifest['coverage']['resource_total'], len(unresolved_resources)))
    browser_path = out / 'raw/browser.json'
    if browser_path.exists():
        browser = json.loads(browser_path.read_text())
        runs = browser.get('runs', [])
        summary = browser_summary(runs)
        dump(out / 'report/browser-summary.json', summary)
        bev = lambda r, fragment: {'url': r['requested_url'], 'file': 'raw/browser.json', 'locator': 'run_id=' + r['run_id'], 'fragment': fragment}
        dom_runs = [r for r in runs if r.get('ok') and r.get('same_url') and r.get('dom_usable', True) and r.get('dom')]
        rep.add('BROWSER-01', 'Смена URL при браузерной загрузке', [bev(r, r['final_url']) for r in runs if canonical_url(r.get('final_url', '')) and not r.get('same_url') and r.get('navigation_ok', r.get('ok')) and r.get('navigation_status') is not None],
                'Разработчик устанавливает механизм перехода; владелец выбирает назначение URL.', 'Исходный HTTP и браузер согласованы; DOM другой страницы не используется для исходного URL.')
        transition_check = rep.checks[-1]
        main_measured, main_gaps = [], []
        for r in runs:
            blocked_main = [item for item in r.get('scope_blocked', []) if item.get('is_main_document')]
            attempted_main = r.get('attempted_navigation', [])
            measured = bool(r.get('navigation_ok', r.get('ok')) and canonical_url(r.get('final_url') or '') and r.get('navigation_status') is not None and not blocked_main and not attempted_main)
            if measured: main_measured.append(r)
            else: main_gaps.append(r)
        transition_check['note'] = 'Основная навигация измерена в {} из {} прогонов; прогонов с пробелом основной навигации {}. Отдельные блокировки iframe и POST не считаются пробелом основной навигации, если основной документ измерен.'.format(len(main_measured), len(runs), len(main_gaps))
        transition_check['evidence'].append({'file': 'raw/browser.json', 'locator': 'runs: navigation_ok,navigation_status,final_url,attempted_navigation,scope_blocked.is_main_document; eligible={}/{}'.format(len(main_measured), len(runs))})
        if not transition_check['count'] and (not runs or main_gaps):
            transition_check['status'] = UNKNOWN
            transition_check['note'] += ' Отсутствие обнаруженного перехода не подтверждает отсутствие переходов в неизмеренных или заблокированных основных навигациях.'
            transition_check['next_check'] = 'Аналитик повторяет основную навигацию проблемных URL в разрешённом охвате; ограничения инструмента сохраняются отдельно.'
        rep.add('BROWSER-02', 'Неполные браузерные наблюдения', [bev(r, json.dumps({'network_failed': r.get('network_failed'), 'ok': r.get('ok'), 'navigation_ok': r.get('navigation_ok'), 'error': r.get('error')}, ensure_ascii=False)) for r in runs if r.get('network_failed') or not r.get('ok')],
                'Аналитик раздельно сверяет HTTP/DOM, ограничения инструмента и network_failed; разработчик проверяет воспроизведённые сетевые сигналы.', 'Причина каждого неполного наблюдения установлена; сетевой сигнал проверен отдельно. Для скорости есть минимум три чистых сопоставимых прогона.', UNKNOWN, note='!ok может означать заблокированную основную навигацию, неприменимый DOM или ограничение измерения. Инструментальное вмешательство не доказывает сетевой дефект сайта. network_failed хранит отдельные наблюдаемые сетевые сигналы; их причина и воспроизводимость требуют проверки.')
        mobile_runs = [r for r in dom_runs if r.get('profile', {}).get('width', 10000) <= 800]
        rep.add('BROWSER-03', 'Мобильное горизонтальное переполнение', [bev(r, str(r['dom']['overflow_px'])) for r in mobile_runs if r.get('dom', {}).get('overflow_px', 0) > 1],
                'Разработчик исправляет переполняющий блок; проверяет оба мобильных размера.', 'Основной контент доступен без нежелательной горизонтальной прокрутки.')
        rep.add('BROWSER-04', 'Кандидаты в перекрывающие фиксированные блоки', [bev(r, json.dumps(r['dom']['fixed'], ensure_ascii=False)[:500]) for r in dom_runs if any(x['height'] > r['profile']['height'] * .2 for x in r.get('dom', {}).get('fixed', []))],
                'Редактор проверяет актуальность анонса; разработчик проверяет перекрытие на снимке.', 'Полезный первый экран доступен; закрытие проверено отдельно.', note='Геометрия даёт кандидат; сама по себе не доказывает перекрытие.')
        rep.add('BROWSER-05', 'Lazy у наблюдаемого LCP-изображения', [bev(r, json.dumps(r.get('lcp_element'), ensure_ascii=False)) for r in dom_runs if (r.get('lcp_element') or {}).get('loading') == 'lazy'],
                'Разработчик проверяет положение изображения и снимает lazy у критического визуала.', 'Критический визуал загружается своевременно; чистые повторы подтверждают результат.')
        thin = []
        comparable = []
        for r in dom_runs:
            src = byurl.get(r['requested_url'])
            if src and src.get('page') and r.get('same_url') and r.get('ok'):
                a = set(re.findall(r'\w+', src['page']['main_text'] or src['page']['text']))
                b = set(re.findall(r'\w+', r.get('dom', {}).get('main_text', '')))
                if b: comparable.append(r)
                if b and len(a & b) / len(b) < .9:
                    thin.append(bev(r, 'Покрытие слов DOM в сыром HTML: {:.1%}'.format(len(a & b) / len(b))))
        rep.add('BROWSER-06', 'Основной текст DOM не полностью обнаружен в исходном HTML', thin,
                'Разработчик и редактор проверяют значимые блоки, переносимые в исходный HTML.', 'Ключевое содержание доступно в согласованном представлении.', note='Словарное сравнение — эвристика; порядок, CSS-видимость и роль текста требуют review.')
        rep.add('BROWSER-07', 'Ограничения браузерного инструмента и заблокированные попытки', [bev(r, json.dumps({'scope_blocked': r.get('scope_blocked'), 'attempted_navigation': r.get('attempted_navigation'), 'speed_clean': r.get('speed_clean')}, ensure_ascii=False)[:1500]) for r in runs if r.get('scope_blocked') or r.get('attempted_navigation')], 'Аналитик отделяет заблокированный iframe/POST/переход от ошибки основного документа; выбирает разрешённый способ наблюдения.', 'Основной документ атрибутирован; ограничения отдельно видны и не считаются дефектом сайта.', status='требует проверки', empty='измерено' if runs else UNKNOWN, note='Ограничение read-only инструмента не доказывает сетевой дефект или необходимость менять сайт.')
        rep.add('BROWSER-08', 'Малые видимые цели нажатия — кандидаты', [bev(r, json.dumps(r['dom']['tap_targets']['candidates'], ensure_ascii=False)[:1500]) for r in mobile_runs if r['dom'].get('tap_targets', {}).get('candidates')], 'Разработчик проверяет расстояния, контекст и работу целей на мобильном экране.', 'Цели доступны по принятому критерию; геометрический кандидат подтверждён проверкой.', empty='пройдено' if any(r['dom'].get('tap_targets', {}).get('measured') for r in mobile_runs) else UNKNOWN, note='Кандидат: ширина или высота меньше 24px. Геометрия не заменяет проверку расстояния, контекста, клавиатуры и сценария.')
        rep.add('BROWSER-09', 'Мелкий видимый текст — кандидаты', [bev(r, json.dumps(r['dom']['text_metrics'], ensure_ascii=False)) for r in mobile_runs if (r['dom'].get('text_metrics', {}).get('small_font_share') or 0) > manifest.get('config', {}).get('small_font_share_threshold', .4)], 'Редактор и разработчик проверяют читаемость основных блоков на мобильном экране.', 'Читаемость подтверждена; декоративные подписи отделены от основного содержания.', empty='пройдено' if any(r['dom'].get('text_metrics', {}).get('visible_chars') for r in mobile_runs) else UNKNOWN, note='Диагностический сигнал: доля видимых символов со шрифтом меньше 12px выше {:.0%}; минимум {:.0%} символов со шрифтом 12px и выше. Порог не является универсальным правилом доступности.'.format(manifest.get('config', {}).get('small_font_share_threshold', .4), 1 - manifest.get('config', {}).get('small_font_share_threshold', .4)))
        rep.add('BROWSER-10', 'Ширина Title выше диагностической модели', [bev(r, json.dumps(r['dom']['head'], ensure_ascii=False)) for r in dom_runs if (r['dom'].get('head', {}).get('title_pixel_width') or 0) > r['dom'].get('head', {}).get('title_width_threshold_px', 600)], 'Редактор проверяет предметность и отображение заголовка по важным запросам.', 'Заголовок сохраняет смысл; длина обоснована.', empty='пройдено' if any(r['dom'].get('head', {}).get('title_pixel_width') is not None for r in dom_runs) else UNKNOWN, note='Модель 20px Arial / 600px диагностическая; фактическая выдача не измерена.')
        metadata_changes = []
        for r in dom_runs:
            src = byurl.get(r['requested_url'])
            if not src or not src.get('page'): continue
            dom = r['dom']; changes = {}
            if dom.get('head') and src['page']['title'] != dom['head'].get('title'): changes['title'] = [src['page']['title'], dom['head'].get('title')]
            if 'canonical' in dom and src['page'].get('canonical_candidates', [src['page'].get('canonical')]) != dom['canonical']: changes['canonical'] = [src['page'].get('canonical_candidates'), dom['canonical']]
            if 'meta_robots' in dom:
                values = [x['content'] for x in dom['meta_robots'] if x.get('name', '').lower() == 'robots']
                if src['page'].get('meta_values', {}).get('robots', []) != values: changes['robots'] = [src['page'].get('meta_values', {}).get('robots', []), values]
            if changes: metadata_changes.append(bev(r, json.dumps(changes, ensure_ascii=False)))
        rep.add('BROWSER-11', 'Метаданные исходного HTML и DOM различаются', metadata_changes, 'Разработчик определяет скрипт изменения и согласует индексируемое представление.', 'Title/canonical/robots соответствуют принятой роли и доступны в исходном HTML.', empty='пройдено' if any(r['dom'].get('head') and 'canonical' in r['dom'] and 'meta_robots' in r['dom'] for r in dom_runs) else UNKNOWN)
        rep.add('BROWSER-12', 'Fetchpriority наблюдаемого LCP-изображения требует review', [bev(r, json.dumps(r['lcp_element'], ensure_ascii=False)) for r in dom_runs if r.get('lcp_element') and r['lcp_element'].get('tag') == 'IMG' and 'fetchpriority' in r['lcp_element'] and r['lcp_element'].get('fetchpriority') != 'high'], 'Разработчик проверяет необходимость high и конкуренцию загрузок по профилю.', 'Приоритет выбран по измеренному критическому пути.', empty='пройдено' if any(r.get('lcp_element') and 'fetchpriority' in r['lcp_element'] for r in dom_runs) else UNKNOWN, note='Отсутствие high не является доказанным дефектом скорости.')
        network_runs = [r for r in dom_runs if r.get('network', {}).get('supported')]
        dump(out / 'report/network-summary.json', [{'url': r['requested_url'], 'run_id': r['run_id'], 'profile': r['profile'], 'network': r['network']} for r in network_runs])
        rep.gate('PERF-03', 'Сетевая нагрузка и протоколы наблюдаемой браузерной выборки', 'измерено' if network_runs else UNKNOWN, 'Разработчик сверяет ресурсы, вес, кэш и протоколы с принятой политикой.', 'report/network-summary.json: только измеренные браузером ресурсы. protocol — наблюдение CDP, не вывод urllib. Усечение и byte_budget_exceeded сохраняются.')
        rep.add('PERF-04', 'Ограничения браузерной сетевой выборки', [bev(r, json.dumps({k: r['network'].get(k) for k in ('resources_truncated', 'byte_budget_exceeded', 'resource_count', 'byte_limit', 'unfinished_resource_count', 'transfer_complete', 'transferred_bytes_lower_bound')}, ensure_ascii=False)) for r in network_runs if r['network'].get('resources_truncated') or r['network'].get('byte_budget_exceeded') or r['network'].get('transfer_complete') is False], 'Аналитик уточняет лимиты и повторяет нужные адреса.', 'Выборка достаточна для выбранного вывода; ограничения сохранены.', status=UNKNOWN, empty='измерено' if network_runs else UNKNOWN)
        link_changes, fragment_missing, dom_link_eligible, fragment_eligible, fragment_functional = [], [], [], [], []
        for r in dom_runs:
            src = byurl.get(r['requested_url'])
            if 'links' not in r['dom'] or not src or not src.get('page'): continue
            dom_link_eligible.append(r)
            original_links = {canonical_url(l.get('href', ''), src['final_url']) + ('#' + l['fragment'] if l.get('fragment') else '') for l in src['page']['links'] if l.get('href') and canonical_url(l['href'], src['final_url'])}
            for link in r['dom']['links']:
                target = canonical_url(link.get('href', ''), r['final_url'])
                if not target: continue
                fragment = urllib.parse.unquote(urllib.parse.urlsplit(link.get('href', '')).fragment)
                identity = target + ('#' + fragment if fragment else '')
                if identity not in original_links: link_changes.append({**bev(r, 'Ссылка DOM не найдена в исходном HTML: ' + identity), 'target': identity})
                if link.get('target_exists') is not None:
                    kind = 'целевой-якорь' if link['target_exists'] else fragment_kind(fragment, r['dom'].get('fragment_ids', []))
                    if kind == 'программное-действие':
                        fragment_functional.append({**bev(r, 'Программный фрагмент требует проверки функции: ' + identity), 'target': identity})
                    else:
                        fragment_eligible.append(r)
                        if kind != 'целевой-якорь' and link.get('target_exists') is False: fragment_missing.append({**bev(r, 'Обычный фрагмент не найден в атрибутированном DOM: ' + identity), 'target': identity})

        rep.add('BROWSER-13', 'Ссылки DOM не обнаружены в исходном HTML — кандидаты', link_changes, 'Разработчик проверяет роль динамических ссылок и доступность маршрута без JavaScript.', 'Необходимые навигационные цели присутствуют в согласованном представлении.', empty='пройдено' if dom_link_eligible else UNKNOWN, note='Сравнение включает target и fragment; добавление ссылки скриптом само по себе не доказывает дефект. Охват ограничен max-links и атрибутированным DOM.')
        rep.add('BROWSER-14', 'Внутристраничные фрагменты не найдены в DOM', fragment_missing, 'Разработчик проверяет динамические блоки и исправляет подтверждённые цели.', 'Названный блок существует и доступен после перехода.', empty='пройдено' if fragment_eligible else 'не применимо' if fragment_functional else UNKNOWN, note='Проверены только обычные фрагменты того же URL; программные кандидаты идут в BROWSER-15. Межстраничные фрагменты требуют открытия целевого DOM.')
        rep.add('BROWSER-15', 'Программные фрагменты DOM — требуется проверка функции', fragment_functional, 'Разработчик проверяет функцию меню, popup или hash-router в разрешённом сценарии.', 'Работа обработчика и доступное управление подтверждены интерфейсной проверкой.', status='требует проверки', empty='не применимо' if dom_link_eligible else UNKNOWN, note='Префикс команды без DOM-ID не доказывает сломанную ссылку и не подтверждает работу функции. Существующий target_exists/ID имеет приоритет.')
        image_dom_eligible = [r for r in dom_runs if any(im.get('visible') and im.get('rendered_width') and im.get('naturalWidth') for im in r['dom'].get('images', []))]
        oversize = [bev(r, json.dumps(im, ensure_ascii=False)) for r in image_dom_eligible for im in r['dom']['images'] if im.get('visible') and im.get('rendered_width') and im.get('naturalWidth', 0) / im['rendered_width'] > 1.5]
        responsive = [bev(r, json.dumps(im, ensure_ascii=False)) for r in image_dom_eligible for im in r['dom']['images'] if im.get('visible') and im.get('rendered_width') and im.get('naturalWidth', 0) / im['rendered_width'] > 1.5 and (not im.get('srcset') or not im.get('sizes'))]
        rep.add('IMAGE-08', 'Естественная ширина изображения выше отрисованной — кандидат', oversize, 'Разработчик сопоставляет DPR, качество и ширины разных экранов; выбирает подходящий источник.', 'Размер источника соответствует качеству и принятому бюджету.', empty='пройдено' if image_dom_eligible else UNKNOWN, note='naturalWidth/rendered_width >1.5; это ширина в CSS-пикселях, а не доказательство лишних байтов. DPR и визуальное качество требуют review.')
        rep.add('IMAGE-09', 'У крупного видимого источника отсутствуют srcset/sizes — кандидат', responsive, 'Разработчик проверяет responsive-источники, CSS и назначение визуала.', 'Нужные размеры получают подходящий ресурс без потери качества.', empty='пройдено' if image_dom_eligible else UNKNOWN, note='Кандидат: natural/render >1.5 и отсутствует srcset либо sizes; CSS/background и picture/source требуют отдельной проверки.')
        network_budgets = []
        for r in network_runs:
            image_resources = [x for x in r['network'].get('resources', []) if str(x.get('type', '')).lower() == 'image' or str(x.get('content_type', '')).lower().startswith('image/')]
            image_total = sum(x.get('encoded_bytes') or 0 for x in image_resources)
            image_bytes_missing = sum(x.get('encoded_bytes') is None for x in image_resources)
            complete = r['network'].get('transfer_complete') is True and not image_bytes_missing
            network_budgets.append({'run': r, 'url': r['requested_url'], 'run_id': r['run_id'], 'image_total_encoded_bytes': image_total, 'image_resource_count': len(image_resources), 'image_bytes_missing_count': image_bytes_missing, 'image_total_complete': complete, 'image_total_lower_bound': not complete, 'total_encoded_bytes': r['network'].get('total_encoded_bytes'), 'transfer_complete': r['network'].get('transfer_complete'), 'heavy_images': [x for x in image_resources if (x.get('encoded_bytes') or 0) > 800*1024]})
        dump(out / 'report/network-budget-summary.json', [{k: v for k, v in x.items() if k != 'run'} for x in network_budgets])
        rep.add('PERF-07', 'Браузерная нагрузка выше диагностического бюджета — кандидат', [bev(x['run'], json.dumps({k: v for k, v in x.items() if k != 'run'}, ensure_ascii=False)[:2000]) for x in network_budgets if (x['total_encoded_bytes'] or 0) > 1.5*1024*1024 or x['image_total_encoded_bytes'] > 800*1024], 'Разработчик проверяет состав критической загрузки и утверждает бюджет с владельцем.', 'Вес выбранного профиля соответствует принятому бюджету; качество и функции сохранены.', empty='пройдено' if network_budgets and all(x['image_total_complete'] and x['total_encoded_bytes'] is not None for x in network_budgets) else UNKNOWN, note='Диагностические пороги: страница >1.5 MiB или сумма всех наблюдаемых изображений >800 KiB. Отдельные тяжёлые изображения сохранены в summary. encoded_bytes CDP включают сетевой overhead; неполная загрузка или пропущенные байты — нижняя граница.')
        network_texts = [(r, x) for r in network_runs for x in r['network'].get('resources', []) if x.get('status') == 200 and x.get('finished') and not x.get('from_disk_cache') and not x.get('from_service_worker') and str(x.get('content_type', '')).lower().startswith(('text/', 'application/javascript', 'application/json'))]
        rep.add('PERF-08', 'Наблюдаемые текстовые ресурсы без Content-Encoding — кандидаты', [bev(r, json.dumps(x, ensure_ascii=False)) for r, x in network_texts if not x.get('content_encoding') and not x.get('from_disk_cache') and not x.get('from_service_worker')], 'Разработчик проверяет сжатие по типу ресурса и условия CDN/сервера.', 'Передача выбранных текстовых ответов имеет согласованное сжатие либо обоснованное исключение.', empty='пройдено' if network_texts else UNKNOWN, note='CDP наблюдение выбранных загрузок; отсутствие заголовка не доказывает возможность ускорения.')
        observed_protocols = [(r, x) for r in network_runs for x in r['network'].get('resources', []) if x.get('protocol')]
        rep.gate('PERF-09', 'Фактически наблюдаемые браузером HTTP-протоколы', 'измерено' if observed_protocols else UNKNOWN, 'Разработчик сверяет протоколы с принятой политикой; необходимость изменения проверяет отдельно.', 'report/network-summary.json protocol: реальный CDP ответ на URL; h2/HTTP/1.1 не выводятся из urllib, схемы https или серверных заголовков.')
        browser_eligibility = {'BROWSER-01': any(r.get('navigation_status') is not None for r in runs), 'BROWSER-02': bool(runs), 'BROWSER-03': any('overflow_px' in r['dom'] for r in mobile_runs), 'BROWSER-04': any('fixed' in r['dom'] for r in dom_runs), 'BROWSER-05': any(r.get('lcp_element') for r in dom_runs), 'BROWSER-06': bool(comparable)}
        for check in rep.checks:
            if check['status'] == 'пройдено' and check['check_id'] in browser_eligibility and not browser_eligibility[check['check_id']]:
                check['status'] = UNKNOWN; check['note'] += ' Нет подходящего браузерного наблюдения для положительного вердикта.'
        rep.gate('PERF-01', 'Пригодность лабораторных повторов', 'измерено' if summary and all(x['status'] == 'измерено' for x in summary) else UNKNOWN,
                 'Аналитик повторяет каждый профиль до трёх чистых загрузок.', 'См. report/browser-summary.json. Окно наблюдения ограничено; результаты не являются полевыми Core Web Vitals.')
        rep.gate('PERF-02', 'Достижение согласованного бюджета скорости', 'требует проверки',
                 'Владелец задаёт бюджет/профиль; аналитик выполняет отдельную приёмочную серию с известной инструментальной нагрузкой.', 'Медианы встроенного сборщика диагностические: DNS/robots guard может задерживать загрузку. Порог не заменён универсальным нормативом.')
    else:
        for cid, title in [('BROWSER-01', 'HTTP и браузер: переходы и содержание'), ('BROWSER-03', 'Мобильный интерфейс'), ('PERF-01', 'Лабораторная скорость')]:
            rep.gate(cid, title, UNKNOWN, 'Аналитик запускает browser_probe.cjs на разрешённых обследованных URL.', 'Браузерный сбор не выполнялся; данные не подменены нулём.')
    coverage_name = manifest.get('browser_coverage_file', 'raw/browser.coverage.json')
    coverage_file = (out / coverage_name).resolve()
    if not coverage_file.is_relative_to((out / 'raw').resolve()) or coverage_file.suffix != '.json':
        raise ValueError('Источник профилирования должен быть JSON внутри raw')
    coverage_runs = json.loads(coverage_file.read_text()).get('runs', []) if coverage_file.exists() else []
    measured_coverage = [r for r in coverage_runs if r.get('same_url') and r.get('dom_usable') and r.get('coverage', {}).get('status') == 'измерено' and r.get('diagnostic_perturbation')]
    coverage_summary = [{'url': r['requested_url'], 'run_id': r['run_id'], 'profile': r['profile'], 'coverage': r['coverage']} for r in measured_coverage]
    dump(out / 'report/coverage-summary.json', coverage_summary)
    coverage_scope_note = 'Пригодных профилируемых прогонов: {} из {}. '.format(len(measured_coverage), len(coverage_runs))
    rep.gate('PERF-05', 'Отдельное диагностическое покрытие JavaScript и CSS', 'измерено' if measured_coverage else UNKNOWN, 'Разработчик проверяет использованный/неиспользованный код в наблюдаемом сценарии; динамические состояния проверяет отдельно.', coverage_scope_note + 'report/coverage-summary.json; источник ' + coverage_name + '. Единица — UTF-16 кодовые единицы исходного текста, не сетевые байты. Эта серия не используется для приёмки скорости.')
    coverage_gaps = [r for r in coverage_runs if r not in measured_coverage or r.get('coverage', {}).get('truncated') or r.get('coverage', {}).get('errors')]
    rep.add('PERF-06', 'Ограничения диагностического покрытия JS/CSS', [{'url': r['requested_url'], 'file': coverage_name, 'locator': 'run_id=' + r['run_id'], 'fragment': json.dumps({'dom_usable': r.get('dom_usable'), 'same_url': r.get('same_url'), 'error': r.get('error'), 'coverage_status': r.get('coverage', {}).get('status'), 'truncated': r.get('coverage', {}).get('truncated'), 'errors': r.get('coverage', {}).get('errors')}, ensure_ascii=False)} for r in coverage_gaps], 'Аналитик повторяет нужный сценарий с достаточным ограниченным бюджетом.', 'Охват и пробелы явны; неиспользованный код не удаляется без проверки зависимостей.', status=UNKNOWN, empty='измерено' if measured_coverage else UNKNOWN, note=coverage_scope_note + 'Непригодные DOM, тайм-ауты и блокировки сохраняются как пробелы всей серии, даже если другие прогоны измерены.')
    for cid, title, action in [
        ('ACCESS-01', 'Фактическая индексация', 'Владелец предоставляет датированные выгрузки Search Console / Яндекс Вебмастера.'),
        ('ACCESS-02', 'Полевые LCP, INP, CLS', 'Владелец предоставляет данные реальных пользователей с периодом и группами URL.'),
        ('ACCESS-03', 'Серверные логи и доступ роботов', 'Владелец предоставляет обезличенные HTTP-логи и правила CDN/WAF.'),
        ('ACCESS-04', 'Политика публикации и актуальные бизнес-данные', 'Владелец утверждает роли страниц, черновики, цены, даты и публичные утверждения.')]:
        rep.gate(cid, title, 'нужен доступ', action, 'Публичный обход не доказывает этот результат.')
    rep.gate('REVIEW-01', 'Семантика структурированных данных и видимость claims', 'требует проверки',
             'Аналитик сопоставляет JSON-LD с видимым содержанием и актуальной официальной документацией.', 'Парсинг JSON не заменяет семантический валидатор; Product/Service/FAQ/рейтинги проверяются по профилю.')
    rep.gate('PROFILE-01', 'Проверки функций профиля сайта', 'требует проверки',
             'Аналитик проверяет доступные сценарии профиля; отправка форм, покупки и авторизация — только по отдельному разрешению.',
             {'corporate': 'Услуги, кейсы, контакты, CTA и связи материалов с услугами.', 'store': 'Каталог, варианты товаров, фильтры, цены и публичные условия; оформление заказа не выполнялось.', 'media': 'Статьи, рубрики, архивы, даты, авторство и пагинация.', 'app': 'Публичный вход и маршруты; приватные состояния и работа приложения не проверены.'}[manifest['profile']])
    # An empty sample cannot pass a check. Partial positives remain observed positives;
    # only absence of a finding is downgraded when evidence for that check is missing.
    for c in rep.checks:
        if c['status'] != 'пройдено': continue
        cid = c['check_id']
        missing = (cid.startswith(('HTML-', 'DUP-', 'DATA-', 'INDEX-03')) and not indexed) or (
            cid.startswith(('IMAGE-', 'LINK-')) and not pages) or (
            cid == 'LINK-01' and any(l['target'] not in byurl or byurl[l['target']]['error'] for l in links
                                    if urllib.parse.urlsplit(l['target']).netloc == urllib.parse.urlsplit(manifest['site']).netloc)) or (
            cid.startswith('INDEX-') and not manifest['coverage']['sitemap_complete']) or (
            cid in ('INDEX-01', 'INDEX-04') and (any(u not in byurl for u in sm) or
                any(r['error'] or r['truncated'] for r in rows if r['requested_url'] in sm))) or (
            cid == 'RESOURCE-01' and any(r['error'] or r['truncated'] for r in resources)) or (
            cid.startswith('HTTP-') and not any(r['status'] is not None and not r['error'] for r in rows))
        if missing:
            c['status'] = UNKNOWN
            c['note'] += ' Нет достаточного обследованного набора для положительного вердикта.'
    new_fields = {'HTML-06': 'viewport', 'HTML-07': 'headings', 'HTML-08': 'canonical_candidates', 'RESOURCE-03': 'resources', 'LINK-06': 'fragment_ids', 'DUP-06': 'main_blocks', 'IMAGE-07': 'images'}
    for c in rep.checks:
        cid = c['check_id']
        if cid in new_fields and pages and not all(new_fields[cid] in r['page'] for r in pages):
            c['status'] = UNKNOWN; c['count'] = 0
            c['note'] += ' \u041f\u043e\u043b\u0435 \u043d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043e \u0432 \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u043c \u0441\u0440\u0435\u0437\u0435; \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u043d\u043e\u0432\u044b\u0439 \u0441\u0431\u043e\u0440.'
            rep.details = [d for d in rep.details if d['check_id'] != cid]
            continue
        if c['status'] not in ('пройдено', 'измерено'): continue
        missing = (cid in new_fields and (not pages or not all(new_fields[cid] in r['page'] for r in pages))) or (cid in ('DUP-03', 'DUP-04', 'DUP-05') and not any(x['shingles'] >= 20 for x in content['pages'])) or (cid in ('LINK-07', 'LINK-08', 'LINK-09', 'HTML-09', 'HTTP-07', 'INDEX-06') and not pages)
        if cid == 'RESOURCE-03': missing = missing or not any('in_head' in item for r in pages for item in r['page']['resources'])
        if cid == 'IMAGE-07': missing = missing or not any('fetchpriority' in im for r in pages for im in r['page']['images'])
        if missing:
            c['status'] = UNKNOWN; c['note'] += ' Нет соответствующих полей/подходящей выборки для положительного вердикта.'
    return rep.write(manifest)


def main():
    ap = argparse.ArgumentParser(description='Ограниченный публичный аудит сайта; сайт не изменяется.')
    ap.add_argument('url', nargs='?')
    ap.add_argument('--out', required=True, help='Новый каталог результата; существующий не перезаписывается')
    ap.add_argument('--profile', choices=['corporate', 'store', 'media', 'app'], default='corporate')
    ap.add_argument('--max-pages', type=int, default=200)
    ap.add_argument('--max-requests', type=int, default=500)
    ap.add_argument('--max-depth', type=int, default=8)
    ap.add_argument('--max-sitemaps', type=int, default=10)
    ap.add_argument('--max-sitemap-urls', type=int, default=5000)
    ap.add_argument('--max-resources', type=int, default=50)
    ap.add_argument('--max-images', type=int, default=300, help='Лимит уникальных внутренних img src для HTTP-выборки')
    ap.add_argument('--max-http-probes', type=int, default=3, help='Лимит HTML URL с тремя сопоставимыми GET gzip и условным GET при наличии валидатора')
    ap.add_argument('--workers', type=int, default=4, help='Параллельные GET; общий интервал начала и лимит запросов сохраняются')
    ap.add_argument('--resume', action='store_true', help='Продолжить тот же срез из checkpoint с неизменным хостом/правами и общим бюджетом')
    ap.add_argument('--seed-urls', default='', help='Дополнительные приоритетные URL того же хоста, через запятую')
    ap.add_argument('--seed-file', help='JSON-массив приоритетных URL того же хоста; максимум max-pages')
    ap.add_argument('--small-font-share-threshold', type=float, default=.4, help='Диагностический порог доли видимых символов шрифта меньше 12px')
    ap.add_argument('--near-threshold', type=float, default=.8, help='Диагностический порог Jaccard близких шинглов')
    ap.add_argument('--unique-share-threshold', type=float, default=.4, help='Диагностический порог доли шинглов частоты 1')
    ap.add_argument('--repeated-block-words', type=int, default=50, help='Минимум слов повторного блока на 3+ страницах')
    ap.add_argument('--navigation-depth-threshold', type=int, default=4, help='Диагностический порог переходов от старта')
    ap.add_argument('--max-bytes', type=int, default=2 * 1024 * 1024)
    ap.add_argument('--timeout', type=float, default=15)
    ap.add_argument('--delay', type=float, default=.5)
    ap.add_argument('--include-query', action='store_true')
    ap.add_argument('--allow-local', action='store_true', help='Только для явно разрешённых локальных тестов; разрешает loopback')
    ap.add_argument('--render-only', action='store_true', help='Пересобрать отчёт из сохранённых raw; без сетевых запросов')
    a = ap.parse_args()
    out = Path(a.out).resolve()
    if a.render_only:
        print(json.dumps(dict(analyse(out)), ensure_ascii=False)); return
    if not a.url: ap.error('Нужен URL')
    if out.exists() and not a.resume: ap.error('Каталог уже существует; выберите новый срез или --resume')
    if a.resume and not out.exists(): ap.error('Для --resume нужен существующий срез')
    if min(a.max_pages, a.max_requests, a.max_sitemaps, a.max_sitemap_urls, a.max_bytes) < 1 or min(a.max_resources, a.max_images, a.max_http_probes, a.max_depth) < 0 or a.timeout <= 0 or a.delay < 0 or not 1 <= a.workers <= 32 or not 0 < a.near_threshold <= 1 or not 0 <= a.unique_share_threshold <= 1 or not 0 <= a.small_font_share_threshold <= 1 or a.repeated_block_words < 1 or a.navigation_depth_threshold < 0:
        ap.error('Лимиты должны быть положительными; delay/depth/resources могут быть нулём')
    # Validate before creating output.
    c = Collector(a, out)
    for n in ('raw', 'report'): (out / n).mkdir(parents=True, exist_ok=True)
    c.crawl()
    result = analyse(out)
    print(json.dumps({'пакет': str(out), 'проверки': dict(result)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
