## Как подключить скиллы к Codex

### Что понадобится

- личный доступ к приватному репозиторию [`Paper-Planes-IB/paper-planes-skills`](https://github.com/Paper-Planes-IB/paper-planes-skills);
- установленный [GitHub CLI](https://cli.github.com/);
- личный API-доступ к LMS, выданный администратором;
- Codex на macOS.

Общий аккаунт администратора, серверный SSH-ключ и общий API-токен сотрудникам не передаются.

### Установка

Откройте Terminal и выполните:

```bash
gh auth login
gh repo clone Paper-Planes-IB/paper-planes-skills ~/paper-planes-skills
~/paper-planes-skills/scripts/install_colleague_rail.sh
```

Установщик запросит личные API key и API secret LMS, подключит активные скиллы к Codex и зарегистрирует ежедневное обновление.

После установки перезапустите Codex и выполните проверку:

```bash
~/paper-planes-skills/scripts/doctor_colleague_rail.sh
```

Проверка должна подтвердить доступ к GitHub, целостность реестра, подключение скиллов и авторизацию в LMS.

### Как обновляются скиллы

1. Илья обновляет пакет в своей папке Google Drive.
2. Центральная рельса проверяет структуру и отсутствие секретов, затем публикует изменения в GitHub и в этот реестр.
3. Компьютер сотрудника ежедневно забирает проверенную версию из GitHub.
4. Codex читает обновлённый пакет через управляемую ссылку в `~/.codex/skills`.

Пакеты, исчезнувшие из источника, сохраняются с архивным статусом. Автоматическое удаление отключено.

### Безопасность

- API-токен LMS хранится в `~/.config/paper-planes/lms.env` с правами `600`.
- Перед изменением статьи инструмент сохраняет её копию.
- Запись требует явного флага `--apply`.
- Команды удаления в рельсе нет.

Полная техническая инструкция: [onboarding/README.md](https://github.com/Paper-Planes-IB/paper-planes-skills/blob/main/onboarding/README.md).
