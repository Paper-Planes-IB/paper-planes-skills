# vault-note-enricher

Назначение: обогащать свежие заметки vault (в целевых папках) короткими блоками: summary, выделенные сущности, links-to-canon, и next actions. v0 работает в proposal-only: ничего не перетирает, только добавляет новый блок в конец заметки.

Запуск:

```bash
python3 scripts/vault_note_enricher.py
```

## Writeback / Approval Gate

Этот skill считается рискованным, потому что прямо обогащает заметки Vault и может добавить summary, links-to-canon, next actions, YAML/frontmatter или смысловые связи.

По умолчанию работать в proposal-only: показать, какой блок будет добавлен, в какой файл, на основании какого источника и что изменится. Добавлять блоки в заметки, менять ссылки, frontmatter, статусы или next actions можно только после явного акцепта Ильи на конкретный writeback.
