from __future__ import annotations

import json
import os
import subprocess
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class LMSHandler(BaseHTTPRequestHandler):
    writes = []

    def log_message(self, format, *args):
        return

    def send_json(self, payload, status=200):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.headers.get("Authorization") != "token test-key:test-secret":
            self.send_json({"error": "unauthorized"}, 401)
            return
        if self.path == "/api/method/frappe.auth.get_logged_user":
            self.send_json({"message": "colleague@paper-planes.ru"})
        else:
            self.send_json({"data": {"name": "doc-1", "title": "До изменения"}})

    def do_PUT(self):
        size = int(self.headers.get("Content-Length", "0"))
        payload = json.loads(self.rfile.read(size))
        self.__class__.writes.append(payload)
        self.send_json({"data": payload})


class ColleagueRailTest(unittest.TestCase):
    def test_links_only_active_skills(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            repo = root / "repo"
            (repo / "registry").mkdir(parents=True)
            (repo / "skills" / "active-one").mkdir(parents=True)
            (repo / "skills" / "old-one").mkdir(parents=True)
            (repo / "registry" / "manifest.json").write_text(
                json.dumps(
                    {
                        "skills": [
                            {"name": "active-one", "lifecycle": "active"},
                            {"name": "old-one", "lifecycle": "legacy"},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            codex_home = root / "home" / ".codex"
            subprocess.run(
                [
                    "python3",
                    str(ROOT / "scripts" / "link_active_skills.py"),
                    "--repo",
                    str(repo),
                    "--codex-home",
                    str(codex_home),
                    "--strict",
                ],
                check=True,
                capture_output=True,
            )
            self.assertTrue((codex_home / "skills" / "active-one").is_symlink())
            self.assertFalse((codex_home / "skills" / "old-one").exists())

    def test_adopts_identical_directory_and_preserves_changed_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            repo = root / "repo"
            (repo / "registry").mkdir(parents=True)
            for name in ("same", "changed"):
                (repo / "skills" / name).mkdir(parents=True)
                (repo / "skills" / name / "SKILL.md").write_text(name, encoding="utf-8")
            (repo / "registry" / "manifest.json").write_text(
                json.dumps({"skills": [{"name": "same", "lifecycle": "active"}, {"name": "changed", "lifecycle": "active"}]}),
                encoding="utf-8",
            )
            codex_home = root / "home" / ".codex"
            (codex_home / "skills" / "same").mkdir(parents=True)
            (codex_home / "skills" / "same" / "SKILL.md").write_text("same", encoding="utf-8")
            (codex_home / "skills" / "changed").mkdir(parents=True)
            (codex_home / "skills" / "changed" / "SKILL.md").write_text("local change", encoding="utf-8")
            run = subprocess.run(
                ["python3", str(ROOT / "scripts" / "link_active_skills.py"), "--repo", str(repo), "--codex-home", str(codex_home), "--adopt-identical"],
                check=True,
                capture_output=True,
                text=True,
            )
            result = json.loads(run.stdout)
            self.assertTrue((codex_home / "skills" / "same").is_symlink())
            self.assertFalse((codex_home / "skills" / "changed").is_symlink())
            self.assertEqual(result["adopted_identical"], 1)
            self.assertTrue(Path(result["backup"]).joinpath("same", "SKILL.md").exists())

    def test_lms_auth_and_guarded_update_with_backup(self):
        LMSHandler.writes = []
        server = HTTPServer(("127.0.0.1", 0), LMSHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with tempfile.TemporaryDirectory() as temp:
                home = Path(temp)
                env_dir = home / ".config" / "paper-planes"
                env_dir.mkdir(parents=True)
                env_file = env_dir / "lms.env"
                env_file.write_text(
                    "\n".join(
                        [
                            f"PP_LMS_URL=http://127.0.0.1:{server.server_port}",
                            "PP_LMS_API_KEY=test-key",
                            "PP_LMS_API_SECRET=test-secret",
                        ]
                    )
                    + "\n",
                    encoding="utf-8",
                )
                run_env = {**os.environ, "HOME": str(home)}
                who = subprocess.run(
                    ["python3", str(ROOT / "scripts" / "pp_lms.py"), "whoami"],
                    env=run_env,
                    check=True,
                    capture_output=True,
                    text=True,
                )
                self.assertIn("colleague@paper-planes.ru", who.stdout)

                payload = home / "change.json"
                payload.write_text('{"title":"После изменения"}\n', encoding="utf-8")
                subprocess.run(
                    [
                        "python3",
                        str(ROOT / "scripts" / "pp_lms.py"),
                        "update",
                        "--doctype",
                        "Wiki Document",
                        "--name",
                        "doc-1",
                        "--payload",
                        str(payload),
                    ],
                    env=run_env,
                    check=False,
                    capture_output=True,
                )
                self.assertEqual(LMSHandler.writes, [])
                subprocess.run(
                    [
                        "python3",
                        str(ROOT / "scripts" / "pp_lms.py"),
                        "update",
                        "--doctype",
                        "Wiki Document",
                        "--name",
                        "doc-1",
                        "--payload",
                        str(payload),
                        "--apply",
                    ],
                    env=run_env,
                    check=True,
                    capture_output=True,
                )
                self.assertEqual(LMSHandler.writes, [{"title": "После изменения"}])
                backups = list((home / ".local" / "share" / "paper-planes-lms" / "backups").rglob("*.json"))
                self.assertEqual(len(backups), 1)
                self.assertIn("До изменения", backups[0].read_text(encoding="utf-8"))
        finally:
            server.shutdown()
            thread.join(timeout=2)
            server.server_close()


if __name__ == "__main__":
    unittest.main()
