# vault-brain-scan

Назначение: health-check графа знаний vault. v0 делает лёгкий аудит структуры: объём файлов, свежесть, проблемные зоны (слишком большие файлы, папки-архивы, дубли).

Артефакт:
- `Vault/60-отчёты/health/vault-brain-scan-<ДД-ММ-ГГГГ>.md`

Запуск:

```bash
python3 scripts/vault_brain_scan.py
```

