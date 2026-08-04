# trails-generator

Назначение: генерация cross-source trails и черновиков Article Briefs из vault. Ищет неявные связи между Concepts/Ideas/книгами/проектами и кладёт кандидаты в рабочие папки, не ломая канон.

Артефакты (v0):
- `Vault/60-отчёты/trails/trails-<ДД-ММ-ГГГГ>.md` — список трейлов (proposal-only).

Запуск:

```bash
python3 scripts/trails_generator.py
```

## Writeback / Approval Gate

Этот skill считается рискованным, потому что соединяет Vault-источники в новые trails, Article Briefs и content candidates, которые могут стать каноном или контентной рельсой.

По умолчанию trails являются proposal-only. Не создавать и не обновлять рабочие файлы, briefs, content candidates, статусы, ссылки или маршруты в 2/8-ке без явного акцепта Ильи. Если связь между источниками является inference, маркировать её как inference/candidate и не выдавать за подтверждённую связку.
