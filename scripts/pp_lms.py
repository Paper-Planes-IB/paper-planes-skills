#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.parse
import tempfile
from pathlib import Path
from typing import Optional


DEFAULT_ENV = Path.home() / ".config" / "paper-planes" / "lms.env"
DEFAULT_BACKUPS = Path.home() / ".local" / "share" / "paper-planes-lms" / "backups"


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if path.exists():
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    for key in ("PP_LMS_URL", "PP_LMS_API_KEY", "PP_LMS_API_SECRET"):
        if os.environ.get(key):
            values[key] = os.environ[key]
    return values


class LMSClient:
    def __init__(self, env_path: Path):
        cfg = load_env(env_path)
        missing = [key for key in ("PP_LMS_URL", "PP_LMS_API_KEY", "PP_LMS_API_SECRET") if not cfg.get(key)]
        if missing:
            raise RuntimeError(f"Не настроены параметры LMS: {', '.join(missing)}")
        self.base = cfg["PP_LMS_URL"].rstrip("/")
        self.authorization = f"token {cfg['PP_LMS_API_KEY']}:{cfg['PP_LMS_API_SECRET']}"

    def request(self, method: str, path: str, payload: Optional[dict] = None) -> dict:
        with tempfile.TemporaryDirectory(prefix="pp-lms-") as temp_dir:
            temp = Path(temp_dir)
            config_path = temp / "curl.conf"
            config_path.write_text(
                "".join(
                    [
                        f'header = "Authorization: {self.authorization}"\n',
                        'header = "Accept: application/json"\n',
                        'header = "Content-Type: application/json"\n',
                        'user-agent = "Paper-Planes-Codex-Rail/1.0"\n',
                    ]
                ),
                encoding="utf-8",
            )
            os.chmod(config_path, 0o600)
            command = [
                "curl",
                "--silent",
                "--show-error",
                "--connect-timeout",
                "10",
                "--max-time",
                "30",
                "--config",
                str(config_path),
                "--request",
                method,
                "--write-out",
                "\n%{http_code}",
            ]
            if payload is not None:
                payload_path = temp / "payload.json"
                payload_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
                os.chmod(payload_path, 0o600)
                command.extend(["--data-binary", f"@{payload_path}"])
            command.append(self.base + path)
            try:
                response = subprocess.run(command, capture_output=True, text=True, check=False)
            except OSError as error:
                raise RuntimeError(f"Не удалось запустить системный curl: {error}") from None
            if response.returncode != 0:
                raise RuntimeError(f"LMS недоступна: {response.stderr.strip()[:500]}")
            body, separator, status_text = response.stdout.rpartition("\n")
            if not separator or not status_text.isdigit():
                raise RuntimeError("LMS вернула ответ без HTTP-статуса")
            status = int(status_text)
            if status >= 400:
                raise RuntimeError(f"LMS вернула HTTP {status}: {body[:1000]}")
            try:
                return json.loads(body)
            except json.JSONDecodeError:
                raise RuntimeError(f"LMS вернула ответ в неожиданном формате: {body[:500]}") from None

    def resource_path(self, doctype: str, name: Optional[str] = None) -> str:
        path = "/api/resource/" + urllib.parse.quote(doctype, safe="")
        if name is not None:
            path += "/" + urllib.parse.quote(name, safe="")
        return path


def safe_filename(value: str) -> str:
    return re.sub(r"[^A-Za-zА-Яа-яЁё0-9._-]+", "-", value).strip("-") or "document"


def main() -> int:
    parser = argparse.ArgumentParser(description="Безопасный клиент Paper Planes LMS")
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("whoami")

    get_parser = commands.add_parser("get")
    get_parser.add_argument("--doctype", required=True)
    get_parser.add_argument("--name", required=True)

    list_parser = commands.add_parser("list")
    list_parser.add_argument("--doctype", required=True)
    list_parser.add_argument("--filters", default="[]")
    list_parser.add_argument("--fields", default='["name"]')
    list_parser.add_argument("--limit", type=int, default=100)

    update_parser = commands.add_parser("update")
    update_parser.add_argument("--doctype", required=True)
    update_parser.add_argument("--name", required=True)
    update_parser.add_argument("--payload", type=Path, required=True)
    update_parser.add_argument("--apply", action="store_true")

    args = parser.parse_args()
    client = LMSClient(args.env_file.expanduser())

    if args.command == "whoami":
        result = client.request("GET", "/api/method/frappe.auth.get_logged_user")
    elif args.command == "get":
        result = client.request("GET", client.resource_path(args.doctype, args.name))
    elif args.command == "list":
        json.loads(args.filters)
        json.loads(args.fields)
        query = urllib.parse.urlencode(
            {"filters": args.filters, "fields": args.fields, "limit_page_length": args.limit}
        )
        result = client.request("GET", client.resource_path(args.doctype) + "?" + query)
    elif args.command == "update":
        if not args.apply:
            raise RuntimeError("Запись остановлена: добавьте --apply после проверки payload")
        payload = json.loads(args.payload.read_text(encoding="utf-8"))
        current = client.request("GET", client.resource_path(args.doctype, args.name))
        stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = DEFAULT_BACKUPS / stamp
        backup_dir.mkdir(parents=True, exist_ok=False)
        backup_path = backup_dir / f"{safe_filename(args.doctype)}__{safe_filename(args.name)}.json"
        backup_path.write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.chmod(backup_path, 0o600)
        result = client.request("PUT", client.resource_path(args.doctype, args.name), payload)
        result = {"backup": str(backup_path), "response": result}
    else:
        raise AssertionError(args.command)

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError, json.JSONDecodeError) as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        raise SystemExit(1)
