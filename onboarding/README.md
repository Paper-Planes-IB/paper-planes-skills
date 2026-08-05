# Подключение Codex к скиллам Paper Planes и LMS

Эта рельса предназначена для сотрудников Paper Planes на macOS. Она подключает Codex к каноническому репозиторию скиллов и к LMS через персональный API-доступ.

## Что выдаёт администратор

1. Доступ сотрудника к приватному репозиторию `Paper-Planes-IB/paper-planes-skills` с ролью `Read`.
2. Личный аккаунт сотрудника в LMS: `https://lms.paper-planes.ru`.
3. Персональные API key и API secret этого аккаунта. Токен наследует права пользователя в LMS, поэтому сотруднику назначают только необходимые роли.

Общий аккаунт `Administrator`, общий API-токен и SSH-ключ сервера сотрудникам не передаются.

### Действия администратора

Доступ к GitHub выдаётся командой:

```bash
gh api --method PUT \
  repos/Paper-Planes-IB/paper-planes-skills/collaborators/GITHUB_LOGIN \
  -f permission=pull
```

Для LMS администратор открывает личную карточку сотрудника в Frappe Desk, находит раздел `API Access` и нажимает `Generate Keys`. API secret показывается один раз; его передают сотруднику через менеджер паролей или другой закрытый канал.

## Установка

В Terminal:

```bash
gh auth login
gh repo clone Paper-Planes-IB/paper-planes-skills ~/paper-planes-skills
~/paper-planes-skills/scripts/install_colleague_rail.sh
```

Установщик:

- проверит доступ к GitHub;
- подключит все активные скиллы в `~/.codex/skills`;
- установит в память Codex карту обращений к активным скиллам;
- сохранит LMS-токен в `~/.config/paper-planes/lms.env` с правами `600`;
- проверит пользователя LMS и чтение Wiki;
- зарегистрирует ежедневное обновление в 08:00 по локальному времени Mac.

Совпадающие локальные папки установщик переносит в резервную копию и заменяет управляемыми ссылками. Папки с отличиями он сохраняет без изменений и выводит отдельным списком.

Если локальная версия должна остаться отдельной, добавьте имя скилла отдельной строкой в `~/.config/paper-planes/allowed-skill-overrides.txt`. Проверка будет показывать его как сохранённое исключение.

## Проверка

```bash
~/paper-planes-skills/scripts/doctor_colleague_rail.sh
```

Ожидаемый результат: GitHub доступен, репозиторий синхронизирован, активные скиллы подключены, LMS отвечает от имени личного пользователя.

## Работа с LMS

```bash
# Кто подключён
~/paper-planes-skills/scripts/pp_lms.py whoami

# Прочитать страницу Wiki
~/paper-planes-skills/scripts/pp_lms.py get --doctype "Wiki Document" --name gcj3niu80m

# Получить список опубликованных страниц
~/paper-planes-skills/scripts/pp_lms.py list --doctype "Wiki Document" \
  --filters '[["is_published","=",1]]' \
  --fields '["name","title","route"]'
```

Изменение документа требует JSON-файл и явный флаг `--apply`:

```bash
~/paper-planes-skills/scripts/pp_lms.py update \
  --doctype "Wiki Document" \
  --name gcj3niu80m \
  --payload ./change.json \
  --apply
```

Перед записью инструмент сохраняет текущий документ в `~/.local/share/paper-planes-lms/backups/`. Команды удаления в рельсе нет.

## Как приходят обновления

1. Илья меняет пакет в своей папке Google Drive.
2. Центральный проход Paper Planes проверяет структуру и секреты, публикует изменение в GitHub и обновляет большой реестр LMS.
3. Mac сотрудника ежедневно выполняет `git pull --ff-only`.
4. Управляемые ссылки Codex сразу ведут на новую версию пакета.
5. Карта обращений в `~/.codex/paper-planes-skill-routing.md` пересобирается вместе с обновлением.

Если центральная проверка отклоняет пакет, сотрудники продолжают работать с последней проверенной версией. Исчезнувшие пакеты автоматически не удаляются.

## После установки

Перезапустите Codex, чтобы он перечитал список скиллов. Секрет LMS нельзя вставлять в чат, задачу, GitHub issue или файл проекта.
