#!/usr/bin/env python3
"""Bounded, read-only public website audit. Python 3.9+, standard library only."""
import argparse
import csv
import hashlib
import html
import ipaddress
import json
import re
import socket
import statistics
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ET
from collections import Counter, deque
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

VERSION = '0.1.0'
UA = 'PPWebsiteAudit/0.1'
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
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')


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

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag not in ('area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'):
            self.stack.append(tag)
        if tag == 'base' and a.get('href'):
            self.base = canonical_url(a['href'], self.url) or self.base
        if tag == 'meta':
            self.meta[(a.get('name') or a.get('property') or '').lower()] = a.get('content', '')
        if tag == 'h1':
            self.h1.append('')
        if tag == 'link':
            rel = a.get('rel', '').lower().split()
            u = canonical_url(a.get('href', ''), self.base)
            if 'canonical' in rel:
                self.canonical = u
            if 'stylesheet' in rel and u:
                self.resources.append({'url': u, 'type': 'css'})
        if tag == 'script' and a.get('src'):
            u = canonical_url(a['src'], self.base)
            if u:
                self.resources.append({'url': u, 'type': 'js'})
        if tag == 'script' and a.get('type', '').lower() == 'application/ld+json':
            self.json_buffer = ''
        if tag == 'a':
            self.anchor = {'source': self.url, 'target': canonical_url(a.get('href', ''), self.base) if a.get('href') else None,
                           'href': a.get('href'), 'anchor': '', 'rel': a.get('rel', '')}
            self.links.append(self.anchor)
        if tag == 'img':
            self.images.append({'src': canonical_url(a.get('src', ''), self.base) if a.get('src') else None,
                                'alt': a.get('alt'), 'width': a.get('width'), 'height': a.get('height'),
                                'loading': a.get('loading'), 'srcset': a.get('srcset'), 'sizes': a.get('sizes'),
                                'style': a.get('style', '')})
        if tag == 'form':
            self.forms += 1

    def handle_endtag(self, tag):
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
        if 'title' in self.stack:
            self.title += data
        if 'h1' in self.stack and self.h1:
            self.h1[-1] += data
        if self.anchor is not None:
            self.anchor['anchor'] += data.strip() + ' '
        if not any(t in self.stack for t in ('script', 'style', 'noscript', 'head')):
            if data.strip():
                self.text.append(data.strip())
                if 'main' in self.stack or 'article' in self.stack:
                    self.main_text.append(data.strip())

    def result(self):
        return {'title': self.title.strip(), 'h1': [s.strip() for s in self.h1],
                'description': self.meta.get('description'), 'robots': self.meta.get('robots', ''),
                'canonical': self.canonical, 'og': {k: v for k, v in self.meta.items() if k.startswith('og:')},
                'text': ' '.join(self.text), 'main_text': ' '.join(self.main_text), 'links': self.links,
                'images': self.images, 'resources': self.resources, 'jsonld': self.jsonld, 'forms': self.forms}


def parse_page(body, url):
    p = PageParser(url)
    p.feed(body)
    return p.result()


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

    def request(self, url, policy=True, kind='page'):
        row = {'requested_url': url, 'kind': kind, 'at': timestamp(), 'chain': [], 'status': None,
               'final_url': url, 'headers': {}, 'error': None, 'raw_file': None, 'truncated': False}
        current = url
        for _ in range(11):
            if kind == 'page' and urllib.parse.urlsplit(current).query and not self.a.include_query:
                row['error'] = 'параметрический URL вне согласованного охвата'; break
            if not self.internal(current):
                row['error'] = 'переход вне согласованного хоста'; break
            if not self.public(current):
                row['error'] = 'адрес не является доступным публичным хостом'; break
            if policy and not self.allowed(current):
                row['error'] = 'запрос запрещён robots или robots недоступен'; break
            if self.count >= self.a.max_requests:
                row['error'] = 'достигнут лимит запросов'; break
            delay = self.a.delay
            pol = self.policies.get(urllib.parse.urlsplit(current).scheme)
            if pol and pol.get('parser'):
                rp = pol['parser']
                rate = rp.request_rate(UA)
                delay = max(delay, rp.crawl_delay(UA) or 0, rate.seconds / rate.requests if rate and rate.requests else 0)
            time.sleep(max(0, delay - (time.monotonic() - self.last)))
            self.count += 1
            req = urllib.request.Request(current, headers={'User-Agent': UA, 'Accept-Encoding': 'identity'})
            try:
                try:
                    resp = self.opener.open(req, timeout=self.a.timeout)
                except urllib.error.HTTPError as e:
                    resp = e
                with resp:
                    status = resp.code
                    headers = {k.lower(): v for k, v in resp.headers.items()}
                    data = resp.read(self.a.max_bytes + 1)
                self.last = time.monotonic()
                row['chain'].append({'url': current, 'status': status, 'location': headers.get('location')})
                row.update(status=status, final_url=current, headers=headers, truncated=len(data) > self.a.max_bytes)
                data = data[:self.a.max_bytes]
                if status in (301, 302, 303, 307, 308) and headers.get('location'):
                    target = canonical_url(headers['location'], current)
                    if not target or target in [x['url'] for x in row['chain']]:
                        row['error'] = 'некорректный или циклический редирект'; break
                    current = target
                    continue
                suffix = 'html' if 'text/html' in headers.get('content-type', '') else 'bin'
                raw = self.out / 'raw' / (key(url) + '.' + suffix)
                raw.write_bytes(data)
                row['raw_file'] = raw.relative_to(self.out).as_posix()
                charset = re.search(r'charset=([^;\s]+)', headers.get('content-type', ''), re.I)
                try:
                    body = data.decode(charset.group(1).strip('"') if charset else 'utf-8', errors='replace')
                except LookupError:
                    body = data.decode('utf-8', errors='replace')
                row['bytes'] = len(data)
                return row, body
            except (OSError, urllib.error.URLError, ValueError) as e:
                self.last = time.monotonic()
                row['error'] = str(e); break
        else:
            row['error'] = 'слишком много редиректов'
        return row, ''

    def allowed(self, url):
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

    def crawl(self):
        self.sitemap()
        queue = deque([(self.start, 0)] + [(u, 0) for u in sorted(self.sitemap_urls) if u != self.start])
        seen = set()
        while queue and len(self.rows) < self.a.max_pages:
            url, depth = queue.popleft()
            if url in seen: continue
            seen.add(url)
            if depth > self.a.max_depth:
                self.excluded.append({'url': url, 'reason': 'лимит глубины'}); continue
            if urllib.parse.urlsplit(url).query and not self.a.include_query:
                self.excluded.append({'url': url, 'reason': 'параметрический URL вне охвата'}); continue
            row, body = self.request(url)
            row['depth'] = depth
            self.rows[url] = row
            if row['status'] == 200 and 'text/html' in row['headers'].get('content-type', '') and not row['error']:
                row['page'] = parse_page(body, row['final_url'])
                for link in row['page']['links']:
                    u = link['target']
                    if u and self.internal(u) and u not in seen:
                        queue.append((u, depth + 1))
            if self.count >= self.a.max_requests: break
        self.pending = sorted({u for u, _ in queue if u not in seen})
        resources = []
        unique = set()
        for row in self.rows.values():
            for item in row.get('page', {}).get('resources', []):
                if self.internal(item['url']) and item['url'] not in unique:
                    unique.add(item['url']); resources.append(item)
        self.resource_total = len(resources)
        self.resources = []
        for item in resources[:self.a.max_resources]:
            row, _ = self.request(item['url'], kind=item['type'])
            self.resources.append(row)
        self.complete = not self.pending and not self.excluded and self.sitemap_complete and all(
            not r['error'] and not r['truncated'] for r in self.rows.values())
        manifest = {'version': VERSION, 'at': timestamp(), 'site': self.start, 'profile': self.a.profile,
                    'scope': 'публичные страницы одного хоста; GET; без авторизации и отправки форм',
                    'coverage': {'pages': len(self.rows), 'requests': self.count, 'complete': self.complete,
                                 'pending': self.pending, 'excluded': self.excluded,
                                 'sitemap_complete': self.sitemap_complete,
                                 'resource_total': self.resource_total, 'resource_sample': len(self.resources)},
                    'config': vars(self.a), 'robots': [{k: v for k, v in p.items() if k != 'parser'} for p in self.policies.values()],
                    'sitemap_urls': sorted(self.sitemap_urls), 'sitemaps': self.sitemap_docs,
                    'limitations': ['Доступность для индексации не доказывает фактическую индексацию.',
                                    'Внешние ссылки и ресурсы других хостов не запрашиваются HTTP-коллектором.',
                                    'Новые формы, покупки и изменения сайта не выполняются.',
                                    'Полнота относится к объявленному охвату, а не ко всем страницам сайта.']}
        dump(self.out / 'raw/manifest.json', manifest)
        dump(self.out / 'raw/pages.json', list(self.rows.values()))
        dump(self.out / 'raw/resources.json', self.resources)
        return manifest


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
        clean = [r for r in items if r.get('ok') and r.get('same_url') and not r.get('network_failed') and r.get('navigation_status') == 200]
        enough = len(clean) >= min_clean
        result.append({'url': url, 'profile': json.loads(profile), 'runs': len(items), 'clean': len(clean),
                       'status': 'измерено' if enough else 'нужен повтор',
                       'median': {m: statistics.median([r[m] for r in clean if r.get(m) is not None])
                                  if enough and len([r for r in clean if r.get(m) is not None]) >= min_clean else None
                                  for m in ('lcp_ms', 'fcp_ms', 'cls', 'ttfb_ms')},
                       'limitations': 'Диагностическое наблюдение с инструментальной задержкой DNS/robots guard; для приёмки скорости нужен отдельный инструмент. INP и Lighthouse TBT не измерены.'})
    return result


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
    rep.add('INDEX-01', 'Неиндексируемые или ошибочные адреса в sitemap', [ev(r, 'sitemap + noindex/HTTP', 'status,page.robots,headers.x-robots-tag') for r in rows if r['requested_url'] in sm and not r['error'] and not r['truncated'] and ((r.get('page') and not indexable(r)) or (r['status'] and r['status'] >= 400))],
            'Владелец выбирает режим публикации; разработчик согласует robots и sitemap.', 'В sitemap только согласованные индексируемые действующие адреса.', 'ошибка', 'высокая')
    rep.add('INDEX-02', 'Индексируемые адреса вне обследованного sitemap', [ev(r, 'URL вне sitemap', 'page.canonical; raw/manifest.json') for r in indexed if r['requested_url'] not in sm],
            'Владелец выбирает предназначенные для поиска страницы; разработчик добавляет их в карту.', 'Нужные страницы включены; исключения объяснены.', note='Обследование sitemap: ' + ('завершено' if manifest['coverage']['sitemap_complete'] else 'частичное'))
    rep.add('INDEX-03', 'Canonical отсутствует или отличается от конечного URL', [ev(r, str(r['page']['canonical']), 'page.canonical,final_url') for r in indexed if r['page']['canonical'] != r['final_url']],
            'Разработчик проверяет основной адрес и назначение альтернативных страниц.', 'Canonical соответствует утверждённой роли страницы; исключения документированы.')
    rep.add('INDEX-04', 'Редиректы в sitemap', [ev(r, r['final_url'], 'chain,final_url') for r in rows if r['requested_url'] in sm and len(r['chain']) > 1],
            'Разработчик сверяет loc с утверждёнными конечными canonical-адресами.', 'Карта содержит согласованные конечные адреса; исключения обоснованы.')
    for cid, title, pred, action, accept in [
        ('HTML-01', 'Пустые или шаблонные Title', lambda p: not p['title'] or bool(re.search(r'blank page|copy of', p['title'], re.I)), 'Редактор подтверждает публикацию и задаёт предметный Title.', 'Опубликованные страницы имеют собственный точный Title.'),
        ('HTML-02', 'Число H1 отличается от одного', lambda p: len(p['h1']) != 1, 'Редактор и разработчик задают один предметный H1 в исходном шаблоне.', 'На опубликованных страницах один содержательный H1; исключения обоснованы.'),
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
    rep.add('IMAGE-01', 'Изображения без атрибута alt', [ev(r, im['src'] or '', 'page.images') for r in pages for im in r['page']['images'] if im['alt'] is None],
            'Редактор задаёт alt содержательным изображениям и alt="" декоративным.', 'Назначение каждого изображения подтверждено; атрибут задан.')
    rep.add('IMAGE-02', 'Размеры изображения не заданы в HTML — кандидат', [ev(r, im['src'] or '', 'page.images') for r in pages for im in r['page']['images'] if not (im['width'] and im['height']) and 'aspect-ratio' not in im['style']],
            'Разработчик проверяет CSS/DOM и резервирует место там, где его нет.', 'Место зарезервировано до загрузки; браузерная проверка не показывает связанного сдвига.', note='Размер может задаваться во внешнем CSS; отсутствие HTML-атрибутов не доказывает CLS.')
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
        rep.add('BROWSER-01', 'Смена URL при браузерной загрузке', [bev(r, r['final_url']) for r in runs if r.get('ok') and not r.get('same_url')],
                'Разработчик устанавливает механизм перехода; владелец выбирает назначение URL.', 'Исходный HTTP и браузер согласованы; DOM другой страницы не используется для исходного URL.')
        rep.add('BROWSER-02', 'Сетевые сбои браузерных загрузок', [bev(r, json.dumps(r.get('network_failed'), ensure_ascii=False)) for r in runs if r.get('network_failed') or not r.get('ok')],
                'Разработчик устраняет подтверждённые сбои; аналитик повторяет измерение.', 'Есть минимум три чистых сопоставимых прогона.', UNKNOWN)
        rep.add('BROWSER-03', 'Мобильное горизонтальное переполнение', [bev(r, str(r['dom']['overflow_px'])) for r in runs if r.get('same_url') and r.get('dom', {}).get('overflow_px', 0) > 1],
                'Разработчик исправляет переполняющий блок; проверяет оба мобильных размера.', 'Основной контент доступен без нежелательной горизонтальной прокрутки.')
        rep.add('BROWSER-04', 'Кандидаты в перекрывающие фиксированные блоки', [bev(r, json.dumps(r['dom']['fixed'], ensure_ascii=False)[:500]) for r in runs if r.get('same_url') and any(x['height'] > r['profile']['height'] * .2 for x in r.get('dom', {}).get('fixed', []))],
                'Редактор проверяет актуальность анонса; разработчик проверяет перекрытие на снимке.', 'Полезный первый экран доступен; закрытие проверено отдельно.', note='Геометрия даёт кандидат; сама по себе не доказывает перекрытие.')
        rep.add('BROWSER-05', 'Lazy у наблюдаемого LCP-изображения', [bev(r, json.dumps(r.get('lcp_element'), ensure_ascii=False)) for r in runs if r.get('same_url') and (r.get('lcp_element') or {}).get('loading') == 'lazy'],
                'Разработчик проверяет положение изображения и снимает lazy у критического визуала.', 'Критический визуал загружается своевременно; чистые повторы подтверждают результат.')
        thin = []
        for r in runs:
            src = byurl.get(r['requested_url'])
            if src and src.get('page') and r.get('same_url') and r.get('ok'):
                a = set(re.findall(r'\w+', src['page']['main_text'] or src['page']['text']))
                b = set(re.findall(r'\w+', r.get('dom', {}).get('main_text', '')))
                if b and len(a & b) / len(b) < .9:
                    thin.append(bev(r, 'Покрытие слов DOM в сыром HTML: {:.1%}'.format(len(a & b) / len(b))))
        rep.add('BROWSER-06', 'Основной текст DOM не полностью обнаружен в исходном HTML', thin,
                'Разработчик и редактор проверяют значимые блоки, переносимые в исходный HTML.', 'Ключевое содержание доступно в согласованном представлении.', note='Словарное сравнение — эвристика; порядок, CSS-видимость и роль текста требуют review.')
        rep.gate('PERF-01', 'Пригодность лабораторных повторов', 'измерено' if summary and all(x['status'] == 'измерено' for x in summary) else UNKNOWN,
                 'Аналитик повторяет каждый профиль до трёх чистых загрузок.', 'См. report/browser-summary.json. Окно наблюдения ограничено; результаты не являются полевыми Core Web Vitals.')
        rep.gate('PERF-02', 'Достижение согласованного бюджета скорости', 'требует проверки',
                 'Владелец задаёт бюджет/профиль; аналитик выполняет отдельную приёмочную серию с известной инструментальной нагрузкой.', 'Медианы встроенного сборщика диагностические: DNS/robots guard может задерживать загрузку. Порог не заменён универсальным нормативом.')
    else:
        for cid, title in [('BROWSER-01', 'HTTP и браузер: переходы и содержание'), ('BROWSER-03', 'Мобильный интерфейс'), ('PERF-01', 'Лабораторная скорость')]:
            rep.gate(cid, title, UNKNOWN, 'Аналитик запускает browser_probe.cjs на разрешённых обследованных URL.', 'Браузерный сбор не выполнялся; данные не подменены нулём.')
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
    if out.exists(): ap.error('Каталог уже существует; выберите новый срез')
    if min(a.max_pages, a.max_requests, a.max_sitemaps, a.max_sitemap_urls, a.max_bytes) < 1 or a.max_resources < 0 or a.max_depth < 0 or a.timeout <= 0 or a.delay < 0:
        ap.error('Лимиты должны быть положительными; delay/depth/resources могут быть нулём')
    # Validate before creating output.
    c = Collector(a, out)
    for n in ('raw', 'report'): (out / n).mkdir(parents=True, exist_ok=True)
    c.crawl()
    result = analyse(out)
    print(json.dumps({'пакет': str(out), 'проверки': dict(result)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
