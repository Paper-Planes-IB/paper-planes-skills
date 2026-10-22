#!/usr/bin/env python3
"""Behavioral regressions; local fixture only, no live production requests."""
import argparse
import csv
import gzip
import importlib.util
import json
import os
import subprocess
import tempfile
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location('audit', HERE / 'audit_site.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class Fixture(BaseHTTPRequestHandler):
    hits = []
    requests = []
    routes = {}
    robots_status = 200

    def log_message(self, *args):
        pass

    def do_GET(self):
        type(self).hits.append(self.path)
        type(self).requests.append({'path': self.path, 'headers': dict(self.headers), 'at': time.monotonic()})
        status, typ, body, extra = 200, 'text/html; charset=utf-8', '', {}
        base = 'http://' + self.headers['Host']
        if self.path in self.routes:
            route = self.routes[self.path]
            status, typ, body, extra = route(self) if callable(route) else route
        elif self.path == '/robots.txt':
            status, typ = self.robots_status, 'text/plain'
            body = 'User-agent: *\nDisallow: /blocked\nSitemap: ' + base + '/sitemap.xml\n'
        elif self.path == '/sitemap.xml':
            typ = 'application/xml'
            body = '<urlset>' + ''.join('<url><loc>' + base + x + '</loc></url>' for x in ['/', '/orphan', '/noindex', '/switch', '/clean', '/query-switch', '/dirtyrobots']) + '</urlset>'
        elif self.path == '/':
            body = '<title>Главная</title><main><h1>Сайт</h1><a href="/gone">Один</a><a href="/gone">Два</a><a href="/redirect">Три</a><a href="/blocked">Закрыто</a><a href="/blocked-redirect">Переход к закрытому</a><a href="/query-redirect">Переход к параметру</a><a href="/external">Внешний переход</a><a href="/dirty">Ошибка CSS</a><a href="/doc">Документ</a><a href="/query?x=1">Параметр</a><img src="/image" alt=""></main>'
        elif self.path == '/gone':
            status, body = 404, 'Отсутствует'
        elif self.path == '/redirect':
            status, extra = 302, {'Location': '/gone'}
        elif self.path == '/blocked-redirect':
            status, extra = 302, {'Location': '/blocked'}
        elif self.path == '/query-redirect':
            status, extra = 302, {'Location': '/query?via=redirect'}
        elif self.path == '/external':
            status, extra = 302, {'Location': 'https://example.com/'}
        elif self.path == '/orphan':
            body = '<title>Изолированная страница</title><main><h1>Изолированная</h1>Содержимое страницы</main>'
        elif self.path == '/noindex':
            body = '<title>Черновик</title><meta name="robots" content="noindex"><h1>Черновик</h1>'
        elif self.path == '/doc':
            typ, body = 'application/pdf', '%PDF-1.7 fixture'
        elif self.path == '/switch':
            body = '<title>Blank page</title><script>location.replace("/clean")</script>'
        elif self.path == '/query-switch':
            body = '<title>Переход вне scope</title><script>location.replace("/clean?new=1")</script>'
        elif self.path == '/dirtyrobots':
            body = '<title>Закрытый ресурс</title><h1>Закрытый ресурс</h1><script src="/blocked.js"></script>'
        elif self.path == '/dirty':
            body = '<title>Сетевая ошибка</title><h1>Ошибка</h1><link rel="stylesheet" href="/missing.css">'
        elif self.path == '/missing.css':
            status, typ, body = 404, 'text/css', ''
        elif self.path == '/clean':
            body = '<title>Чистая страница</title><meta name="description" content="Описание"><main><h1>Контент</h1>Содержательный текст</main>'
        elif self.path == '/favicon.ico':
            typ, body = 'image/x-icon', ''
        else:
            status, body = 404, 'Нет страницы'
        self.send_response(status)
        self.send_header('Content-Type', typ)
        for k, v in extra.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body if isinstance(body, bytes) else body.encode())


class AuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), Fixture)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = 'http://127.0.0.1:' + str(cls.server.server_port)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def setUp(self):
        Fixture.hits = []
        Fixture.requests = []
        Fixture.routes = {}
        Fixture.robots_status = 200
        self.temp = tempfile.TemporaryDirectory(prefix='pp-site-audit-eval-')
        self.out = Path(self.temp.name) / 'audit'
        self.out.joinpath('raw').mkdir(parents=True)
        self.out.joinpath('report').mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def collect(self, **changes):
        params = dict(url=self.base + '/', profile='corporate', max_pages=30, max_requests=100, max_depth=8,
                      max_sitemaps=10, max_sitemap_urls=100, max_resources=10, max_bytes=200000,
                      timeout=3, delay=0, include_query=False, allow_local=True, out=str(self.out), render_only=False)
        params.update(changes)
        collector = audit.Collector(argparse.Namespace(**params), self.out)
        collector.crawl()
        audit.analyse(self.out)
        self.checks = {c['check_id']: c for c in json.loads(self.out.joinpath('report/checks.json').read_text())}
        return collector

    def isolated_site(self, pages, sitemap_paths=()):
        """An explicit small graph: no accidental links to the baseline fixture."""
        Fixture.routes['/robots.txt'] = (200, 'text/plain',
            'User-agent: *\nDisallow: /blocked\nSitemap: ' + self.base + '/sitemap.xml\n', {})
        Fixture.routes['/sitemap.xml'] = (200, 'application/xml', '<urlset>' + ''.join(
            '<url><loc>' + self.base + path + '</loc></url>' for path in sitemap_paths) + '</urlset>', {})
        for path, html in pages.items():
            Fixture.routes[path] = (200, 'text/html; charset=utf-8', html, {})

    def details(self, check_id):
        with self.out.joinpath('report/details.csv').open(encoding='utf-8-sig', newline='') as f:
            return [r for r in csv.DictReader(f) if r['check_id'] == check_id]

    def synthetic_browser_run(self, name, **changes):
        run = dict(run_id=name, requested_url=self.base + '/', final_url=self.base + '/',
                   profile={'width': 360, 'height': 800}, ok=True, navigation_ok=True, dom_usable=True,
                   speed_clean=True, same_url=True, navigation_status=200, network_failed=[], scope_blocked=[],
                   diagnostic_perturbation=False, lcp_ms=100, fcp_ms=90, cls=0, ttfb_ms=10,
                   dom={'main_text': 'Содержательный текст', 'content_present': True})
        run.update(changes)
        return run

    def functional_anchor_html(self):
        fragments = ['missing', 'submenu:open', 'popup:login', '/route', '!state', 'submenu:existing']
        return '<head><title>Фрагменты</title></head><main><h1>Контент</h1>Основное содержание' + ''.join(
            '<a href="#' + fragment + '">Ссылка</a>' for fragment in fragments) + \
            '<div id="submenu:existing">Реальная цель с двоеточием</div></main>'

    def run_browser(self, paths, *extra):
        p = subprocess.run([os.environ['AUDIT_NODE'], str(HERE / 'browser_probe.cjs'), '--audit', str(self.out),
                            '--urls', ','.join(self.base + x for x in paths), '--widths', '360',
                            '--max-pages', str(len(paths)), '--window', '1000', '--allow-local', *extra],
                           capture_output=True, text=True, timeout=120)
        self.assertEqual(p.returncode, 0, p.stderr)
        return json.loads(self.out.joinpath('raw/browser.json').read_text())

    def test_head_title_excludes_inline_svg_accessibility_title(self):
        p = audit.parse_page('<html><head><title>Услуги компании</title></head><body>'
            '<svg><title>Стрелка вправо</title><path d="M0 0"></path></svg>'
            '<main><h1>Услуги</h1>Содержательная страница</main></body></html>', self.base)
        self.assertEqual(p['title'], 'Услуги компании')
        self.assertNotIn('Стрелка', p['main_text'])

    def test_tilda_main_fallback_contains_content_excludes_navigation(self):
        p = audit.parse_page('<html><head><title>Тильда</title></head><body>'
            '<div id="allrecords" class="t-records"><div class="t-menu">Повторяющееся меню</div>'
            '<div class="t396"><h1>Услуга аудита</h1><div>Проверяем доказательства и состав результата</div></div>'
            '<footer>Повторяющийся подвал</footer></div></body></html>', self.base)
        self.assertIn('Проверяем доказательства', p['main_text'])
        self.assertNotIn('Повторяющееся меню', p['main_text'])
        self.assertNotIn('Повторяющийся подвал', p['main_text'])

    def test_empty_browser_sample_never_passes(self):
        self.isolated_site({'/': '<head><title>Полная страница</title></head><main><h1>Тест</h1>Текст</main>'})
        self.collect()
        self.out.joinpath('raw/browser.json').write_text(json.dumps({'runs': []}), encoding='utf-8')
        audit.analyse(self.out)
        checks = json.loads(self.out.joinpath('report/checks.json').read_text())
        observed = [c for c in checks if c['check_id'].startswith('BROWSER-')]
        self.assertTrue(observed, 'Нельзя заменить пустую браузерную выборку исчезнувшими проверками')
        self.assertTrue(all(c['status'] != 'пройдено' for c in observed), observed)
        self.assertEqual(next(c for c in checks if c['check_id'] == 'PERF-01')['status'], audit.UNKNOWN)

    def test_empty_dom_and_coverage_instrumentation_do_not_form_clean_medians(self):
        base = dict(requested_url=self.base, profile={'width': 360}, ok=True, same_url=True,
                    navigation_status=200, network_failed=[], lcp_ms=100, fcp_ms=90, cls=0, ttfb_ms=10)
        for limitation in ({'dom_usable': False}, {'speed_clean': False, 'diagnostic_perturbation': True}):
            with self.subTest(limitation=limitation):
                result = audit.browser_summary([{**base, **limitation} for _ in range(3)])[0]
                self.assertEqual(result['clean'], 0)
                self.assertEqual(result['status'], 'нужен повтор')
                self.assertIsNone(result['median']['lcp_ms'])

    def test_navigation_depth_uses_root_paths_and_shortest_route_not_sitemap_seed(self):
        self.isolated_site({
            '/': '<title>Главная</title><main><a href="/a">Первый уровень</a><a href="/short">Короткий путь</a></main>',
            '/a': '<title>А</title><main><a href="/b">Далее</a></main>',
            '/b': '<title>Б</title><main><a href="/deep">Далее</a></main>',
            '/short': '<title>Короткий</title><main><a href="/deep">Напрямую</a></main>',
            '/deep': '<title>Глубокий</title><main>Основной текст</main>',
            '/unreachable': '<title>Нет пути</title><main>Изолированный текст</main>',
        }, ['/deep', '/unreachable'])
        c = self.collect()
        self.assertEqual(c.rows[self.base + '/b']['depth'], 2)
        self.assertEqual(c.rows[self.base + '/deep']['depth'], 2)
        self.assertIsNone(c.rows[self.base + '/unreachable']['depth'])
        self.assertEqual(c.rows[self.base + '/deep']['discovery_depth'], 0)

    def test_sitemap_duplicates_remain_visible_but_are_fetched_once(self):
        self.isolated_site({'/': '<title>Сайт</title><main><a href="/leaf">Страница</a></main>',
                            '/leaf': '<title>Лист</title><main>Отдельный текст</main>'}, ['/', '/leaf', '/leaf'])
        self.collect()
        manifest = json.loads(self.out.joinpath('raw/manifest.json').read_text())
        self.assertEqual(sum(r['url'] == self.base + '/leaf' for r in manifest['sitemap_locs']), 2)
        self.assertEqual(Fixture.hits.count('/leaf'), 1)
        self.assertEqual(self.checks['INDEX-05']['count'], 1)

    def test_near_duplicates_exclude_exact_pairs(self):
        exact = ' '.join('точныйслово' + str(i) for i in range(120))
        near = ' '.join('близкийслово' + str(i) for i in range(120))
        changed = near.replace('близкийслово60', 'новыйотличающийсятермин')
        paths = ['/exact-a', '/exact-b', '/near-a', '/near-b']
        self.isolated_site({'/': '<title>Главная</title><main>Навигация ' + ''.join(
                '<a href="' + p + '">Маршрут ' + p + '</a>' for p in paths) + '</main>',
            **{p: '<title>' + p + '</title><main>' + text + '</main>' for p, text in
               zip(paths, [exact, exact, near, changed])}})
        self.collect()
        content = json.loads(self.out.joinpath('raw/content-analysis.json').read_text())
        pairs = {frozenset([p['left'], p['right']]) for p in content['near_pairs']}
        self.assertIn(frozenset([self.base + '/near-a', self.base + '/near-b']), pairs)
        self.assertNotIn(frozenset([self.base + '/exact-a', self.base + '/exact-b']), pairs)
        self.assertEqual(self.checks['DUP-04']['count'], 1)
        exact_urls = {r['url'] for r in self.details('DUP-03')}
        self.assertEqual(exact_urls, {self.base + '/exact-a', self.base + '/exact-b'})

    def test_fragment_target_uses_ids_names_and_decoded_fragment(self):
        self.isolated_site({
            '/': '<title>Якоря</title><main><a href="/target#known">Есть</a>'
                 '<a href="/target#named">Имя</a><a href="/target#%D1%82%D0%B5%D1%81%D1%82">Кириллица</a>'
                 '<a href="/target#missing">Нет</a></main>',
            '/target': '<title>Цели</title><main><div id="known">Есть</div>'
                       '<a name="named">Именованный якорь</a><div id="тест">Кириллица</div></main>',
        })
        self.collect()
        self.assertEqual(self.checks['LINK-06']['count'], 1)
        rows = self.details('LINK-06')
        self.assertIn('missing', json.dumps(rows, ensure_ascii=False))
        self.assertEqual(Fixture.hits.count('/target'), 1)

    def test_functional_fragments_are_not_missing_ids_and_exact_ids_have_priority(self):
        self.isolated_site({'/': self.functional_anchor_html()})
        self.collect()
        self.assertEqual(self.checks['LINK-06']['count'], 1)
        self.assertEqual(self.checks['LINK-10']['count'], 4)
        self.assertEqual(self.checks['LINK-10']['status'], 'требует проверки')
        self.assertTrue(all(r['target'].endswith('#missing') for r in self.details('LINK-06')))
        self.assertNotIn(self.base + '/#submenu:existing', {r['target'] for r in self.details('LINK-10')})
        self.assertEqual(audit.fragment_kind('submenu:existing', ['submenu:existing']), 'целевой-якорь')
        self.assertEqual(audit.fragment_kind('submenu%3Aopen'), 'обычный-фрагмент', 'Helper не должен повторно декодировать fragment')
        links = [dict(href=self.base + '/#' + f, target_exists=f == 'submenu:existing')
                 for f in ['missing', 'submenu:open', 'popup:login', '/route', '!state', 'submenu:existing']]
        run = self.synthetic_browser_run('functional-fragments', dom={
            'main_text': 'Основное содержание', 'links': links, 'fragment_ids': ['submenu:existing']})
        self.out.joinpath('raw/browser.json').write_text(json.dumps({'runs': [run]}), encoding='utf-8')
        audit.analyse(self.out)
        checks = {c['check_id']: c for c in json.loads(self.out.joinpath('report/checks.json').read_text())}
        self.assertEqual(checks['BROWSER-14']['count'], 1)
        self.assertEqual(checks['BROWSER-15']['count'], 4)
        self.assertEqual(checks['BROWSER-15']['status'], 'требует проверки')

    def test_unmeasured_main_navigation_cannot_pass_while_iframe_is_separate(self):
        self.isolated_site({'/': '<title>Навигация</title><main>Содержательный текст</main>'})
        self.collect()
        blocked = self.synthetic_browser_run('blocked-main', navigation_ok=False, final_url='chrome-error://chromewebdata/',
            attempted_navigation=[{'url': self.base + '/target?blocked=1', 'is_main_document': True}],
            scope_blocked=[{'url': self.base + '/target?blocked=1', 'is_main_document': True}])
        self.out.joinpath('raw/browser.json').write_text(json.dumps({'runs': [blocked]}), encoding='utf-8')
        audit.analyse(self.out)
        checks = {c['check_id']: c for c in json.loads(self.out.joinpath('report/checks.json').read_text())}
        self.assertEqual(checks['BROWSER-01']['count'], 0)
        self.assertEqual(checks['BROWSER-01']['status'], audit.UNKNOWN)
        self.assertTrue(any(e['file'] == 'raw/browser.json' and 'eligible=0/1' in e['locator']
                            for e in checks['BROWSER-01']['evidence']))
        iframe = self.synthetic_browser_run('blocked-iframe',
            scope_blocked=[{'url': self.base + '/frame?blocked=1', 'is_main_document': False},
                           {'url': self.base + '/form', 'is_main_document': False, 'method': 'POST', 'type': 'fetch'}],
            speed_clean=False)
        self.out.joinpath('raw/browser.json').write_text(json.dumps({'runs': [iframe]}), encoding='utf-8')
        audit.analyse(self.out)
        checks = {c['check_id']: c for c in json.loads(self.out.joinpath('report/checks.json').read_text())}
        self.assertEqual(checks['BROWSER-01']['count'], 0)
        self.assertEqual(checks['BROWSER-01']['status'], 'пройдено')
        self.assertTrue(any(e['file'] == 'raw/browser.json' and 'eligible=1/1' in e['locator']
                            for e in checks['BROWSER-01']['evidence']))

    @unittest.skipUnless(os.environ.get('AUDIT_NODE'), 'Браузерный тест: задайте AUDIT_NODE и NODE_PATH')
    def test_real_browser_separates_command_hashes_from_ordinary_missing_targets(self):
        self.isolated_site({'/': self.functional_anchor_html()})
        self.collect()
        browser = self.run_browser(['/'])
        self.assertEqual(len(browser['runs']), 3)
        for run in browser['runs']:
            links = {r['href'].split('#', 1)[-1]: r for r in run['dom']['links']}
            self.assertTrue(links['submenu:existing']['target_exists'])
            self.assertFalse(links['submenu:open']['target_exists'])
        audit.analyse(self.out)
        checks = {c['check_id']: c for c in json.loads(self.out.joinpath('report/checks.json').read_text())}
        self.assertEqual(checks['BROWSER-14']['count'], 3)
        self.assertEqual(checks['BROWSER-15']['count'], 12)
        self.assertEqual(checks['BROWSER-15']['status'], 'требует проверки')

    def test_jsonld_semantic_findings_are_candidates_not_sanctions(self):
        self.isolated_site({'/': '<head><title>Товар</title></head><main><h1>Описание товара</h1>'
            'Видимое описание</main><script type="application/ld+json">'
            '{"@context":"https://schema.org","@type":"Product"}</script>'})
        c = self.collect()
        self.assertTrue(c.rows[self.base + '/']['page']['jsonld'][0]['valid'])
        self.assertEqual(self.checks['DATA-01']['count'], 0)
        candidate = self.checks['DATA-02']
        self.assertGreater(candidate['count'], 0)
        self.assertNotEqual(candidate['status'], 'ошибка')
        self.assertIn('кандидат', (candidate['title'] + ' ' + candidate['note']).lower())
        self.assertTrue(self.details('DATA-02'))

    def test_jsonld_offer_text_and_incompatible_fields_remain_profile_candidates(self):
        good = {'@context': 'https://schema.org', '@type': 'Offer', 'price': 'По запросу', 'priceCurrency': 'RUB'}
        good_html = '<head><title>Предложение</title></head><main>Стоимость по запросу</main>' + \
            '<script type="application/ld+json">' + json.dumps(good, ensure_ascii=False) + '</script>'
        p = audit.parse_page(good_html, self.base)
        candidates, inventory = audit.jsonld_semantic_candidates(p)
        self.assertTrue(p['jsonld'][0]['valid'])
        self.assertEqual(inventory, {'Offer': 1})
        self.assertTrue(any('Schema.org разрешает Text' in c['reason'] for c in candidates))
        self.assertTrue(all('Google Product' in c['reason'] for c in candidates))

        bad = {'@context': 'https://schema.org', '@graph': [
            {'@type': 'Product', 'name': 123},
            {'@type': 'Offer', 'price': {'amount': 10}, 'priceCurrency': 'руб.'},
            {'@type': 'Offer', 'price': 10, 'priceCurrency': 123},
        ]}
        bad_html = '<head><title>Поля для проверки</title></head><main>Видимое описание</main>' + \
            '<script type="application/ld+json">' + json.dumps(bad, ensure_ascii=False) + '</script>'
        self.isolated_site({'/': bad_html})
        c = self.collect()
        parsed = c.rows[self.base + '/']['page']
        candidates, _ = audit.jsonld_semantic_candidates(parsed)
        reasons = '\n'.join(x['reason'] for x in candidates)
        self.assertIn('Product.name', reasons)
        self.assertIn('price содержит', reasons)
        self.assertIn('трёхбуквенный код', reasons)
        self.assertIn('Offer.priceCurrency', reasons)
        self.assertTrue(parsed['jsonld'][0]['valid'])
        self.assertEqual(self.checks['DATA-01']['count'], 0)
        self.assertGreaterEqual(self.checks['DATA-02']['count'], 4)
        self.assertNotEqual(self.checks['DATA-02']['status'], 'ошибка')

    def test_viewport_scale_and_zoom_restrictions_have_native_candidates(self):
        good = 'width=device-width, initial-scale=1.0'
        bad = [
            'width=device-width',
            'width=device-width, initial-scale=2',
            'width=device-width, initial-scale=1, maximum-scale=1',
            'width=device-width, initial-scale=1, user-scalable=no',
        ]
        self.isolated_site({'/': '<head><title>Viewport</title><meta name="viewport" content="' + good +
                                  '"></head><main>Контент</main>',
            **{'/viewport-' + str(i): '<head><title>Viewport ' + str(i) + '</title><meta name="viewport" content="' +
               value + '"></head><main>Контент</main>' for i, value in enumerate(bad)}},
            ['/viewport-' + str(i) for i in range(len(bad))])
        self.collect()
        self.assertEqual(self.checks['HTML-06']['count'], len(bad))
        rows = self.details('HTML-06')
        self.assertTrue(any('maximum-scale' in r['fragment'] for r in rows))
        self.assertTrue(any('user-scalable' in r['fragment'] for r in rows))
        self.assertNotIn(self.base + '/', {r['url'] for r in rows})

    def test_image_budget_sums_many_small_images_and_preserves_unknown_bytes(self):
        self.isolated_site({'/': '<title>Бюджет</title><main>Содержательный текст</main>'})
        self.collect()
        resources = [dict(url=self.base + '/image-' + str(i), type='Image', content_type='image/webp',
                          encoded_bytes=100 * 1024, finished=True) for i in range(12)]
        network = dict(supported=True, resources=resources, resource_count=12, total_encoded_bytes=1200 * 1024,
                       transfer_complete=True, resources_truncated=False, byte_budget_exceeded=False)
        run = self.synthetic_browser_run('many-small-images', network=network)
        self.out.joinpath('raw/browser.json').write_text(json.dumps({'runs': [run]}), encoding='utf-8')
        audit.analyse(self.out)
        checks = {c['check_id']: c for c in json.loads(self.out.joinpath('report/checks.json').read_text())}
        self.assertEqual(checks['PERF-07']['count'], 1)
        budgets = json.loads(self.out.joinpath('report/network-budget-summary.json').read_text())
        self.assertEqual(budgets[0]['image_total_encoded_bytes'], 1200 * 1024)
        self.assertEqual(budgets[0]['heavy_images'], [])
        self.assertTrue(budgets[0]['image_total_complete'])

        network['resources'] = [dict(url=self.base + '/unknown-image', type='Image', finished=True)]
        network['total_encoded_bytes'] = 100
        self.out.joinpath('raw/browser.json').write_text(json.dumps({'runs': [run]}), encoding='utf-8')
        audit.analyse(self.out)
        checks = {c['check_id']: c for c in json.loads(self.out.joinpath('report/checks.json').read_text())}
        self.assertEqual(checks['PERF-07']['status'], audit.UNKNOWN)
        budgets = json.loads(self.out.joinpath('report/network-budget-summary.json').read_text())
        self.assertTrue(budgets[0]['image_total_lower_bound'])

    def test_mobile_readability_uses_original_sixty_percent_boundary(self):
        self.isolated_site({'/': '<title>Текст</title><main>Содержательный текст</main>'})
        self.collect()
        runs = [self.synthetic_browser_run('font-' + str(share), dom={
            'main_text': 'Содержательный текст', 'text_metrics': {'visible_chars': 100, 'small_font_share': share}})
            for share in [.2, .4, .5]]
        self.out.joinpath('raw/browser.json').write_text(json.dumps({'runs': runs}), encoding='utf-8')
        audit.analyse(self.out)
        checks = {c['check_id']: c for c in json.loads(self.out.joinpath('report/checks.json').read_text())}
        self.assertEqual(checks['BROWSER-09']['count'], 1)
        rows = self.details('BROWSER-09')
        self.assertEqual(len(rows), 1)
        self.assertIn('run_id=font-0.5', rows[0]['locator'])

    def test_manifest_selects_profiling_json_inside_raw_and_rejects_other_paths(self):
        self.isolated_site({'/': '<title>Профилирование</title><main>Содержательный текст</main>'})
        self.collect()
        run = self.synthetic_browser_run('new-css-series', diagnostic_perturbation=True, speed_clean=False,
            coverage={'status': 'измерено', 'total_units': 100, 'used_units': 50, 'css': [], 'js': [],
                      'truncated': False, 'errors': []})
        self.out.joinpath('raw/browser.coverage-v2.json').write_text(json.dumps({'runs': [run]}), encoding='utf-8')
        self.out.joinpath('raw/browser.coverage.json').write_text(json.dumps({'runs': []}), encoding='utf-8')
        path = self.out.joinpath('raw/manifest.json')
        manifest = json.loads(path.read_text())
        manifest['browser_coverage_file'] = 'raw/browser.coverage-v2.json'
        path.write_text(json.dumps(manifest), encoding='utf-8')
        audit.analyse(self.out)
        summary = json.loads(self.out.joinpath('report/coverage-summary.json').read_text())
        self.assertEqual([r['run_id'] for r in summary], ['new-css-series'])
        checks = {c['check_id']: c for c in json.loads(self.out.joinpath('report/checks.json').read_text())}
        self.assertEqual(checks['PERF-05']['status'], 'измерено')
        for forbidden in ['../outside.json', 'raw/image.png']:
            with self.subTest(path=forbidden):
                manifest['browser_coverage_file'] = forbidden
                path.write_text(json.dumps(manifest), encoding='utf-8')
                with self.assertRaises(ValueError):
                    audit.analyse(self.out)

    def test_partial_profiling_series_retains_measured_run_and_exposes_invalid_run(self):
        self.isolated_site({'/': '<title>Профилирование</title><main>Содержательный текст</main>'})
        self.collect()
        valid = self.synthetic_browser_run('valid-profile', diagnostic_perturbation=True, speed_clean=False,
            coverage={'status': 'измерено', 'total_units': 100, 'used_units': 50,
                      'css': [], 'js': [], 'truncated': False, 'errors': []})
        invalid = self.synthetic_browser_run('timeout-profile', diagnostic_perturbation=True, speed_clean=False,
            dom_usable=False, same_url=False, error='fixture timeout',
            coverage={'status': 'не удалось измерить', 'truncated': False, 'errors': []})
        self.out.joinpath('raw/browser.coverage.json').write_text(json.dumps({'runs': [valid, invalid]}), encoding='utf-8')
        audit.analyse(self.out)
        summary = json.loads(self.out.joinpath('report/coverage-summary.json').read_text())
        self.assertEqual([r['run_id'] for r in summary], ['valid-profile'])
        checks = {c['check_id']: c for c in json.loads(self.out.joinpath('report/checks.json').read_text())}
        self.assertEqual(checks['PERF-05']['status'], 'измерено')
        self.assertEqual(checks['PERF-06']['status'], audit.UNKNOWN)
        self.assertEqual(checks['PERF-06']['count'], 1)
        self.assertIn('1 из 2', checks['PERF-05']['note'])
        self.assertIn('1 из 2', checks['PERF-06']['note'])
        rows = self.details('PERF-06')
        self.assertEqual(len(rows), 1)
        self.assertIn('run_id=timeout-profile', rows[0]['locator'])
        self.assertIn('fixture timeout', rows[0]['fragment'])

    def test_bounded_image_sample_does_not_claim_all_images_measured(self):
        self.isolated_site({'/': '<title>Изображения</title><main>Основной текст'
            '<img src="/pic-a.png" alt="А"><img src="/pic-b.png" alt="Б">'
            '<img src="/blocked-image.png" alt="Закрыто"></main>'})
        png = bytes.fromhex('89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c489')
        Fixture.routes['/pic-a.png'] = (200, 'image/png', png, {'Cache-Control': 'public,max-age=60'})
        Fixture.routes['/pic-b.png'] = (200, 'image/png', png, {})
        self.collect(max_images=1)
        manifest = json.loads(self.out.joinpath('raw/manifest.json').read_text())
        images = json.loads(self.out.joinpath('raw/images.json').read_text())
        self.assertEqual(manifest['coverage']['image_total'], 3)
        self.assertEqual(manifest['coverage']['image_sample'], 1)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0]['bytes'], len(png))
        self.assertNotIn('/pic-b.png', Fixture.hits)
        self.assertNotIn('/blocked-image.png', Fixture.hits)
        self.assertEqual(self.checks['IMAGE-04']['status'], audit.UNKNOWN)

    def test_compression_and_conditional_304_preserve_original_page(self):
        html = '<head><title>Кэш</title></head><main><h1>Повторный ответ</h1>' + ('Содержание ' * 100) + '</main>'
        encoded = html.encode()
        zipped = gzip.compress(encoded)
        self.isolated_site({'/': html})

        def conditional(handler):
            if handler.headers.get('If-None-Match') == '"fixture-v1"':
                return 304, 'text/html', b'', {'ETag': '"fixture-v1"'}
            if 'gzip' in handler.headers.get('Accept-Encoding', ''):
                return 200, 'text/html; charset=utf-8', zipped, {'Content-Encoding': 'gzip', 'ETag': '"fixture-v1"'}
            return 200, 'text/html; charset=utf-8', encoded, {'ETag': '"fixture-v1"'}

        Fixture.routes['/'] = conditional
        c = self.collect(max_http_probes=1)
        probes = json.loads(self.out.joinpath('raw/http-probes.json').read_text())
        gzip_rows = [r for r in probes if r['probe'] == 'gzip_repeat']
        conditional_rows = [r for r in probes if r['probe'] == 'conditional']
        self.assertEqual(len(gzip_rows), 3)
        self.assertTrue(all(r['status'] == 200 and r['bytes'] == len(zipped) for r in gzip_rows))
        self.assertEqual(len(conditional_rows), 1)
        self.assertEqual(conditional_rows[0]['status'], 304)
        self.assertEqual(conditional_rows[0]['bytes'], 0)
        self.assertEqual(c.rows[self.base + '/']['page']['title'], 'Кэш')
        self.assertEqual(c.rows[self.base + '/']['bytes'], len(encoded))
        self.assertTrue(self.out.joinpath(c.rows[self.base + '/']['raw_file']).read_bytes() == encoded)
        self.assertEqual(self.checks['HTTP-05']['status'], 'измерено')
        self.assertEqual(self.checks['HTTP-06']['status'], 'измерено')

    def test_http_probe_redirect_preserves_document_query_scope(self):
        html = '<title>Проба</title><main>Основной документ</main>'
        self.isolated_site({'/': html})

        def redirected_probe(handler):
            if 'gzip' in handler.headers.get('Accept-Encoding', ''):
                return 302, 'text/html', '', {'Location': '/probe-target?via=gzip'}
            return 200, 'text/html; charset=utf-8', html, {}

        Fixture.routes['/'] = redirected_probe
        self.collect(max_http_probes=1)
        probes = json.loads(self.out.joinpath('raw/http-probes.json').read_text())
        rows = [r for r in probes if r['probe'] == 'gzip_repeat']
        self.assertEqual(len(rows), 3)
        self.assertTrue(all('параметрический' in (r['error'] or '') for r in rows))
        self.assertNotIn('/probe-target?via=gzip', Fixture.hits)

    def test_gzip_decoded_size_limit_cannot_be_bypassed_by_small_transfer(self):
        html = '<head><title>Сжатие</title></head><main>' + ('длинный текст ' * 1000) + '</main>'
        zipped = gzip.compress(html.encode())
        self.assertLess(len(zipped), 512)
        self.isolated_site({'/': html})
        Fixture.routes['/'] = (200, 'text/html; charset=utf-8', zipped, {'Content-Encoding': 'gzip'})
        c = self.collect(max_bytes=512)
        row = c.rows[self.base + '/']
        self.assertTrue(row['decoded_truncated'])
        self.assertTrue(row['truncated'])
        self.assertEqual(row['bytes'], len(zipped))
        self.assertEqual(self.out.joinpath(row['raw_file']).read_bytes(), zipped)
        self.assertGreater(self.checks['HTTP-03']['count'], 0)

    def test_parallel_workers_share_request_budget_delay_and_robots_scope(self):
        paths = ['/worker-' + str(i) for i in range(12)]
        self.isolated_site({'/': '<title>Параллельный обход</title><main>' + ''.join(
            '<a href="' + p + '">Страница</a>' for p in ['/blocked', '/query?forbidden=1'] + paths) + '</main>',
            **{p: '<title>' + p + '</title><main>Проверка лимитов</main>' for p in paths}})
        c = self.collect(workers=4, max_requests=8, delay=0.03)
        self.assertEqual(c.count, 8)
        self.assertEqual(len(Fixture.hits), 8)
        self.assertNotIn('/blocked', Fixture.hits)
        self.assertNotIn('/query?forbidden=1', Fixture.hits)
        self.assertIn('robots', c.rows[self.base + '/blocked']['error'])
        self.assertTrue(any(x['url'].endswith('/query?forbidden=1') for x in c.excluded))
        self.assertFalse(c.complete)
        # Compare the entire arrival span, allowing one scheduler-sized margin.
        # Per-worker sleeps alone would finish much sooner and violate this bound.
        elapsed = Fixture.requests[-1]['at'] - Fixture.requests[0]['at']
        self.assertGreaterEqual(elapsed, 0.03 * (len(Fixture.requests) - 1) - 0.04)

    @unittest.skipUnless(os.environ.get('AUDIT_NODE'), 'Браузерный тест: задайте AUDIT_NODE и NODE_PATH')
    def test_request_guard_distinguishes_iframe_and_main_navigation(self):
        script = '''const {classifyRequest}=require(process.argv[1]);
          const main={url:()=>"http://127.0.0.1:4321/"}, child={url:()=>"about:blank"};
          const page={mainFrame:()=>main}, site=new URL("http://127.0.0.1:4321/"), manifest={config:{include_query:false}};
          const req=frame=>({url:()=>"http://127.0.0.1:4321/frame?x=1",resourceType:()=>"document",frame:()=>frame});
          console.log(JSON.stringify([classifyRequest(req(main),page,site,manifest),classifyRequest(req(child),page,site,manifest)]));'''
        p = subprocess.run([os.environ['AUDIT_NODE'], '-e', script, str(HERE / 'browser_probe.cjs')],
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        main, iframe = json.loads(p.stdout)
        self.assertTrue(main['is_main_document'])
        self.assertFalse(iframe['is_main_document'])
        self.assertEqual(main['reason'], iframe['reason'])
        self.assertIn('параметрический', main['reason'])

    @unittest.skipUnless(os.environ.get('AUDIT_NODE'), 'Браузерный тест: задайте AUDIT_NODE и NODE_PATH')
    def test_real_browser_records_blocked_target_and_retains_iframe_parent(self):
        self.isolated_site({
            '/': '<title>Сайт</title><main>Старт</main>',
            '/iframe-shell': '<title>Фрейм</title><main><h1>Основной документ</h1>Полезное содержание</main>'
                             '<iframe src="/frame?view=1"></iframe>',
            '/query-main': '<title>Переход</title><main>Содержание перед попыткой</main>'
                           '<script>location.replace("/forbidden-target?new=1")</script>',
            '/blank': '<html><head><title>Пустой документ</title></head><body></body></html>',
        }, ['/iframe-shell', '/query-main', '/blank'])
        self.collect()
        browser = self.run_browser(['/iframe-shell', '/query-main', '/blank'])
        iframe_runs = [r for r in browser['runs'] if r['requested_url'].endswith('/iframe-shell')]
        main_runs = [r for r in browser['runs'] if r['requested_url'].endswith('/query-main')]
        blank_runs = [r for r in browser['runs'] if r['requested_url'].endswith('/blank')]
        self.assertEqual(len(iframe_runs), 3)
        self.assertTrue(all(r['same_url'] and r['dom_usable'] for r in iframe_runs), iframe_runs)
        self.assertTrue(all(r['attempted_navigation'] == [] for r in iframe_runs))
        self.assertTrue(all(any(x['url'].endswith('/frame?view=1') and not x['is_main_document']
                                for x in r['instrumentation_blocked']) for r in iframe_runs))
        self.assertEqual(len(main_runs), 3)
        self.assertEqual(len(blank_runs), 3)
        self.assertTrue(all(any(x['url'].endswith('/forbidden-target?new=1') and x['is_main_document']
                                and 'параметрический' in x['reason'] for x in r['attempted_navigation'])
                            for r in main_runs))
        self.assertTrue(all(not r['dom_usable'] and not r['speed_clean'] for r in blank_runs))
        self.assertNotIn('/frame?view=1', Fixture.hits)
        self.assertNotIn('/forbidden-target?new=1', Fixture.hits)
        audit.analyse(self.out)
        checks = {c['check_id']: c for c in json.loads(self.out.joinpath('report/checks.json').read_text())}
        self.assertEqual(checks['BROWSER-01']['count'], 0, 'Внутренняя страница ошибки браузера не является иной публичной страницей')

    @unittest.skipUnless(os.environ.get('AUDIT_NODE'), 'Браузерный тест: задайте AUDIT_NODE и NODE_PATH')
    def test_coverage_accounts_nested_unused_ranges_without_double_counting(self):
        script = '''const {usedCoverageUnits}=require(process.argv[1]);
          console.log(JSON.stringify([
            usedCoverageUnits([{startOffset:0,endOffset:100,count:1},{startOffset:20,endOffset:40,count:0}],100),
            usedCoverageUnits([{startOffset:0,endOffset:100,count:1},{startOffset:10,endOffset:90,count:1}],100),
            usedCoverageUnits([{startOffset:0,endOffset:100,count:1},{startOffset:20,endOffset:80,count:0},{startOffset:30,endOffset:40,count:1}],100)
          ]));'''
        p = subprocess.run([os.environ['AUDIT_NODE'], '-e', script, str(HERE / 'browser_probe.cjs')],
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(json.loads(p.stdout), [80, 100, 50])

    @unittest.skipUnless(os.environ.get('AUDIT_NODE'), 'Браузерный тест: задайте AUDIT_NODE и NODE_PATH')
    def test_real_browser_resource_and_coverage_bounds_are_visible(self):
        self.isolated_site({'/': '<title>Лимиты</title><main><h1>Контент</h1>Содержательная страница</main>'
            '<link rel="stylesheet" href="/one.css"><link rel="stylesheet" href="/two.css">'
            '<script src="/code.js"></script>'})
        Fixture.routes['/one.css'] = (200, 'text/css', 'main { color: black; }', {})
        Fixture.routes['/two.css'] = (200, 'text/css', 'h1 { font-size: 20px; }', {})
        Fixture.routes['/code.js'] = (200, 'application/javascript', 'window.fixtureValue=1; function unused(){ return 42; }', {})
        self.collect()
        browser = self.run_browser(['/'], '--max-resources', '1', '--coverage', 'yes', '--coverage-max-bytes', '2048')
        self.assertEqual(len(browser['runs']), 3)
        for run in browser['runs']:
            self.assertLessEqual(len(run['resources']), 1)
            self.assertLessEqual(len(run['network']['resources']), 1)
            self.assertTrue(run['network']['resources_truncated'])
            self.assertTrue(run['diagnostic_perturbation'])
            self.assertFalse(run['speed_clean'])
            self.assertLessEqual(run['coverage']['total_units'], 2048)
        self.assertEqual(audit.browser_summary(browser['runs'])[0]['clean'], 0)

    @unittest.skipUnless(os.environ.get('AUDIT_NODE'), 'Браузерный тест: задайте AUDIT_NODE и NODE_PATH')
    def test_real_browser_transfer_budget_cannot_form_clean_speed_series(self):
        self.isolated_site({'/': '<title>Большой ответ</title><main><h1>Контент</h1>' +
                            ('Большое содержимое страницы ' * 1500) + '</main>'})
        self.collect()
        browser = self.run_browser(['/'], '--max-transfer-bytes', '1024')
        self.assertEqual(len(browser['runs']), 3)
        for run in browser['runs']:
            self.assertTrue(run['network']['byte_budget_exceeded'])
            self.assertFalse(run['speed_clean'])
            self.assertEqual(run['network']['byte_limit'], 1024)
        self.assertEqual(audit.browser_summary(browser['runs'])[0]['clean'], 0)

    @unittest.skipUnless(os.environ.get('AUDIT_NODE'), 'Браузерный тест: задайте AUDIT_NODE и NODE_PATH')
    def test_inline_css_coverage_uses_stylesheet_size_and_respects_source_budget(self):
        small = 'main {color: black;} h1 {font-size: 20px;}'
        large = ''.join('.unused' + str(i) + ' {color: red;}' for i in range(200))
        self.assertGreater(len(large), 1024)
        self.isolated_site({'/': '<head><title>CSS</title><style>' + small + '</style><style>' + large +
                            '</style></head><main><h1>Контент</h1>Видимый текст</main>'})
        self.collect()
        browser = self.run_browser(['/'], '--coverage', 'yes', '--coverage-max-bytes', '1024')
        self.assertEqual(len(browser['runs']), 3)
        for run in browser['runs']:
            coverage = run['coverage']
            self.assertTrue(coverage['css'], 'Обычный inline CSS нельзя терять из-за размера полного HTML')
            self.assertGreater(sum(x['used_units'] for x in coverage['css']), 0)
            self.assertTrue(any(x['total_units'] == len(small) for x in coverage['css']))
            self.assertLessEqual(coverage['total_units'], 1024)
            self.assertTrue(coverage['truncated'], 'Большой stylesheet должен быть явно исключён по бюджету')
            self.assertFalse(run['speed_clean'])

    @unittest.skipUnless(os.environ.get('AUDIT_NODE'), 'Браузерный тест: задайте AUDIT_NODE и NODE_PATH')
    def test_profiling_keeps_main_code_and_excludes_child_and_error_documents(self):
        main_css = 'main {color: black;} h1 {font-size: 20px;}'
        child_css = '.child {color: red; font-size: 30px;}'
        self.isolated_site({'/': '<head><title>Основной документ</title><style>' + main_css +
            '</style></head><main><h1>Контент</h1>Полезное содержание</main><script src="/main.js"></script>'
            '<iframe src="/child-style"></iframe><iframe src="/frame?blocked=1"></iframe>',
            '/child-style': '<head><title>Дочерний</title><style>' + child_css + '</style></head>'
                            '<div class="child">Контент iframe</div><script src="/child.js"></script>'})
        Fixture.routes['/main.js'] = (200, 'application/javascript',
            'window.fixtureMain=1;function unusedMain(){return 42;}', {})
        Fixture.routes['/child.js'] = (200, 'application/javascript',
            'window.fixtureChild=1;function unusedChild(){return 99;}', {})
        self.collect()
        browser = self.run_browser(['/'], '--coverage', 'yes', '--coverage-max-bytes', '4096')
        self.assertEqual(len(browser['runs']), 3)
        self.assertIn('/child-style', Fixture.hits)
        self.assertIn('/child.js', Fixture.hits)
        self.assertNotIn('/frame?blocked=1', Fixture.hits)
        for run in browser['runs']:
            self.assertTrue(run['dom_usable'])
            coverage = run['coverage']
            self.assertTrue(any(x['url'] == self.base + '/main.js' for x in coverage['js']))
            self.assertTrue(any(x['total_units'] == len(main_css) for x in coverage['css']))
            for row in coverage['js'] + coverage['css']:
                self.assertNotIn('chrome-error:', row.get('url') or '')
                self.assertNotIn('/child', row.get('url') or '')
            self.assertFalse(any(x['total_units'] == len(child_css) for x in coverage['css']))

    def test_broken_link_occurrences_and_final_targets(self):
        self.collect()
        c = self.checks['LINK-01']
        self.assertEqual(c['count'], 3)
        self.assertIn('уникальных конечных целей: 1', c['note'])
        tasks = json.loads(self.out.joinpath('report/tasks.json').read_text())
        self.assertEqual(sum(t['check_id'] == 'LINK-01' for t in tasks), 1)

    def test_redirect_chain_and_robots(self):
        c = self.collect()
        self.assertEqual([x['status'] for x in c.rows[self.base + '/redirect']['chain']], [302, 404])
        self.assertNotIn('/blocked', Fixture.hits)
        self.assertIn('robots', c.rows[self.base + '/blocked-redirect']['error'])
        self.assertIn('вне согласованного', c.rows[self.base + '/external']['error'])
        self.assertIn('параметрический URL', c.rows[self.base + '/query-redirect']['error'])
        self.assertNotIn('/query?via=redirect', Fixture.hits)

    def test_noindex_orphan_and_partial_graph(self):
        self.collect()
        self.assertEqual(self.checks['INDEX-01']['count'], 1)
        self.assertGreater(self.checks['LINK-04']['count'], 0)
        self.assertIn('частичный', self.checks['LINK-04']['note'])
        self.assertIn('Частичный граф', self.checks['LINK-04']['note'])

    def test_resource_error_and_non_html_document(self):
        c = self.collect()
        self.assertEqual(self.checks['RESOURCE-01']['count'], 1)
        self.assertNotIn('page', c.rows[self.base + '/doc'])
        self.assertEqual(c.rows[self.base + '/doc']['status'], 200)

    def test_robots_failure_stops_site_requests(self):
        Fixture.robots_status = 503
        self.collect()
        self.assertNotIn('/', Fixture.hits)
        self.assertEqual(set(Fixture.hits), {'/robots.txt'})

    def test_budget_partial_and_no_false_orphan(self):
        c = self.collect(max_pages=1, max_requests=10)
        self.assertFalse(c.complete)
        self.assertTrue(c.pending)
        self.assertEqual(self.checks['LINK-01']['count'], 0)
        self.assertEqual(self.checks['LINK-01']['status'], audit.UNKNOWN)
        self.assertEqual(self.checks['LINK-02']['status'], audit.UNKNOWN)

    def test_parser_empty_alt_and_duplicate_alias(self):
        p = audit.parse_page('<title>Тест</title><h1>Раз</h1><h1>Два</h1><img alt=""><script type="application/ld+json">{bad}</script>', self.base)
        self.assertEqual(p['h1'], ['Раз', 'Два'])
        self.assertEqual(p['images'][0]['alt'], '')
        self.assertFalse(p['jsonld'][0]['valid'])

    def test_clean_medians_require_three_comparable_runs(self):
        def run(i, clean=True, same=True):
            return dict(requested_url='https://example.com/', profile={'width': 360}, ok=True,
                        same_url=same, navigation_status=200, network_failed=[] if clean else ['404'],
                        lcp_ms=i, fcp_ms=i, cls=0, ttfb_ms=i)
        result = audit.browser_summary([run(1), run(2), run(900, False), run(5, True, False)])[0]
        self.assertEqual(result['status'], 'нужен повтор')
        self.assertIsNone(result['median']['lcp_ms'])
        result = audit.browser_summary([run(1), run(2), run(3), run(900, False)])[0]
        self.assertEqual(result['median']['lcp_ms'], 2)

    def test_raw_integrity_on_render_and_overwrite_guard(self):
        self.collect()
        before = self.out.joinpath('raw/pages.json').read_bytes()
        control = self.out.joinpath('Контроль исправлений.csv')
        with control.open(encoding='utf-8-sig', newline='') as f:
            reader = csv.DictReader(f); fields = reader.fieldnames; records = list(reader)
        records[0]['Исполнитель'] = 'Тестовый разработчик'
        with control.open('w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fields); writer.writeheader(); writer.writerows(records)
        audit.analyse(self.out)
        with control.open(encoding='utf-8-sig', newline='') as f:
            self.assertEqual(list(csv.DictReader(f))[0]['Исполнитель'], 'Тестовый разработчик')
        self.assertEqual(before, self.out.joinpath('raw/pages.json').read_bytes())
        p = subprocess.run([os.sys.executable, str(HERE / 'audit_site.py'), self.base, '--out', str(self.out)], capture_output=True)
        self.assertNotEqual(p.returncode, 0)
        self.assertEqual(before, self.out.joinpath('raw/pages.json').read_bytes())
        self.assertTrue(self.out.joinpath('MANIFEST.sha256').exists())

    @unittest.skipUnless(os.environ.get('AUDIT_NODE'), 'Браузерный тест: задайте AUDIT_NODE и NODE_PATH')
    def test_browser_ip_scope_handles_mapped_ipv6(self):
        script = 'const {publicIP}=require(process.argv[1]); console.log(JSON.stringify([publicIP("::ffff:7f00:1",false),publicIP("::ffff:a00:1",false),publicIP("198.51.100.10",false),publicIP("203.0.113.10",false),publicIP("::ffff:7f00:1",true),publicIP("8.8.8.8",false)]));'
        p = subprocess.run([os.environ['AUDIT_NODE'], '-e', script, str(HERE / 'browser_probe.cjs')], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(json.loads(p.stdout), [False, False, False, False, True, True])

    @unittest.skipUnless(os.environ.get('AUDIT_NODE'), 'Браузерный тест: задайте AUDIT_NODE и NODE_PATH')
    def test_real_browser_dirty_clean_and_cross_url(self):
        self.collect()
        p = subprocess.run([os.environ['AUDIT_NODE'], str(HERE / 'browser_probe.cjs'), '--audit', str(self.out),
                            '--urls', ','.join(self.base + x for x in ['/switch', '/dirty', '/clean', '/query-switch', '/dirtyrobots']), '--widths', '360',
                            '--max-pages', '5', '--window', '1000', '--allow-local'], capture_output=True, text=True, timeout=90)
        self.assertEqual(p.returncode, 0, p.stderr)
        audit.analyse(self.out)
        results = json.loads(self.out.joinpath('report/browser-summary.json').read_text())
        lookup = {x['url']: x for x in results}
        self.assertEqual(lookup[self.base + '/switch']['clean'], 0)
        self.assertEqual(lookup[self.base + '/dirty']['clean'], 0)
        self.assertEqual(lookup[self.base + '/clean']['clean'], 3)
        self.assertEqual(lookup[self.base + '/query-switch']['clean'], 0)
        self.assertEqual(lookup[self.base + '/dirtyrobots']['clean'], 0)
        self.assertNotIn('/clean?new=1', Fixture.hits)
        self.assertNotIn('/blocked.js', Fixture.hits)
        checks = {c['check_id']: c for c in json.loads(self.out.joinpath('report/checks.json').read_text())}
        self.assertEqual(checks['BROWSER-01']['count'], 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
