#!/usr/bin/env python3
"""Behavioral regressions; local fixture only, no live production requests."""
import argparse
import csv
import importlib.util
import json
import os
import subprocess
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location('audit', HERE / 'audit_site.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class Fixture(BaseHTTPRequestHandler):
    hits = []
    robots_status = 200

    def log_message(self, *args):
        pass

    def do_GET(self):
        type(self).hits.append(self.path)
        status, typ, body, extra = 200, 'text/html; charset=utf-8', '', {}
        base = 'http://' + self.headers['Host']
        if self.path == '/robots.txt':
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
        self.wfile.write(body.encode())


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
