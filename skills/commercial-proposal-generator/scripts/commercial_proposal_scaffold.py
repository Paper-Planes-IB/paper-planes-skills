#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys


CLIENT_TEMPLATE = """---
тип: черновик-кп
клиент: {client}
дата: {today}
статус: черновик
тема: {offer_slug}
---

# Коммерческое предложение для {client}

## 0. Gamma-first карта КП

Перед написанием финальной версии собрать КП как слайдовый нарратив:

| Слайд | Основное сообщение | Что должно быть на слайде |
|---|---|---|
| 1. Название оффера |  |  |
| 2. Что предлагаем сейчас / что можем подключить рядом |  |  |
| 3. Контекст клиента |  |  |
| 4. Почему предлагаем именно этот маршрут |  |  |
| 5. Доказательная база и похожие задачи |  |  |
| 6. Целевая логика проекта |  |  |
| 7. Карта 9 рычагов роста |  |  |
| 8. Этапы работ |  |  |
| 9. Аналитические и методологические модули |  |  |
| 10. Артефакты и решения на выходе |  |  |
| 11. Что потребуется для внедрения |  |  |
| 12. Как PP может сопровождать внедрение |  |  |
| 13. Вовлечение команды клиента |  |  |
| 14. Сроки и формат |  |  |
| 15. Стоимость и условия |  |  |
| 16. Следующий шаг |  |  |

## 0. Матрица релевантных услуг

### Вот что предлагаем сейчас

- Ядро оффера 1:
- Ядро оффера 2:
- Ядро оффера 3:

### Что ещё умеем рядом

- Соседняя релевантная услуга 1:
- Соседняя релевантная услуга 2:
- Соседняя релевантная услуга 3:

## 0.1. Релевантный контент и цитаты для усиления КП

- Отраслевой контент / файл:
- Продуктовый контент / файл:
- Сильная формулировка клиента из созвона:
- Цитата / мысль, которую стоит использовать в opening:
- Цитата / мысль, которую стоит использовать в блоке проблемы:
- Что лучше пересказать своими словами, а не цитировать:

## 0.2. Почему предлагаем именно этот маршрут

- Какая клиентская развилка требует именно такого проекта:
- Какой основной продукт Paper Planes здесь активируется:
- Какие соседние продукты могут понадобиться позже:
- Что пока сознательно оставляем за рамками:

## 0.3. Похожие задачи и доказательная база

- Похожий кейс / проект 1:
- Что он доказывает для этого клиента:
- Похожий кейс / проект 2:
- Что он доказывает для этого клиента:
- Какие методологии лучше не называть кодами, а перевести в клиентский результат:

## 0.4. Контекстно-повторяемая стратегия (для общего аудита / широкой стратегии)

- Режим применения: полный контур / внутренняя проверка границ / не применимо
- Среда и вероятный стратегический режим по бизнесам / функциям / ставкам:
- Жизнеспособное ядро дифференциации:
- Усиливающие capabilities и активы:
- Причинный механизм мультипликации:
- Обязательные принципы и фронтовые действия:
- Фильтр смежностей и бюджет сложности:
- Capability strategy команды:
- Требования к операционной модели и петлям обучения:
- Клиентский перевод без методологического жаргона:
- Какое evidence ещё нужно получить:

## 1. Контекст клиента

- Кто клиент:
- Какую задачу решает:
- Почему задача актуальна сейчас:
- Что уже было сделано до нас:

## 2. Проблема, которую нужно решить

- Симптомы:
- Корневая проблема:
- Цена бездействия:
- Почему нельзя просто «сделать как раньше»:

## 2.1. Ось перехода

- Какой переход описывает задачу клиента на человеческом и управленческом языке:
- Что именно перестаёт работать:
- К какой более устойчивой, прибыльной или управляемой логике должен перейти клиент:
- Почему формула этого перехода сильнее, чем абстрактное `модель А / модель Б`:

## 3. Что мы предлагаем

Короткая формула предложения:

> {offer}

### Что входит

- Направление 1:
- Направление 2:
- Направление 3:

### Что сознательно не делаем

- Не дублируем уже выполненные исследования без необходимости.
- Не создаём аналитический контур ради аналитического контура.
- Не подменяем стратегию набором разрозненных активностей.

## 4. Подход к решению

### Этап 1

- Цель:
- Работы:
- Результат:

### Этап 2

- Цель:
- Работы:
- Результат:

### Этап 3

- Цель:
- Работы:
- Результат:

## 5. Артефакты на выходе

- Артефакт 1:
- Артефакт 2:
- Артефакт 3:
- Артефакт 4:

## 5.1. Какие решения сможет принять клиент на выходе

- Решение 1:
- Решение 2:
- Решение 3:
- Решение 4:

## 5.1.1. Карта 9 рычагов роста

Для стратегического / трансформационного КП описать не список локальных доработок, а новый образ организации, который порождает выбранная стратегическая ставка.

Для нишевого КП вроде CRM, дашборда, регламента, обучения или отдельного исследования не разворачивать все 9 рычагов наружу. Использовать этот блок как внутреннюю проверку 1–3 зависимостей, которые реально влияют на успех узкого проекта.

| Рычаг | Входит в первый scope | Артефакты | Ритмы / внедрение | Возможный этап 2 |
|---|---|---|---|---|
| Стратегия |  |  |  |  |
| Финансы |  |  |  |  |
| Маркетинг / клиентские политики |  |  |  |  |
| Продажи |  |  |  |  |
| Бизнес-процессы |  |  |  |  |
| Организационная структура |  |  |  |  |
| HR и модель компетенций |  |  |  |  |
| Автоматизации и целевая модель данных |  |  |  |  |
| Культура |  |  |  |  |

## 5.2. Что останется у команды клиента

- Какой навык / методика передаётся:
- Что команда сможет делать самостоятельно после проекта:
- Какие управленческие ритуалы или инструменты будут внедрены:

## 5.3. Как можем остаться на сопровождение внедрения

- Какие решения могут перейти в сопровождение:
- Какие пилоты / gate-циклы / комитеты можно сопровождать:
- Роль Paper Planes после стратегии:
- Возможная коммерческая модель сопровождения:
- Условия, при которых сопровождение имеет смысл:

## 6. Вовлечение команды клиента

- Кто нужен со стороны клиента:
- Какие данные нужны:
- Какие решения должны приниматься по ходу проекта:
- Сколько времени потребуется от ключевых участников:

## 7. Сроки

- Общий горизонт:
- От чего зависит сокращение или удлинение:

## 8. Стоимость

- Базовая модель:
- Диапазон / ориентир:
- Что влияет на стоимость:

### Коммерческие условия

- Разбивка по этапам:
- Возможные варианты оплаты:
- Есть ли пауза между этапами:
- Есть ли опциональное сопровождение:

## 9. Почему этот подход сработает

- Основание 1:
- Основание 2:
- Основание 3:

## 9.1. Почему это не повторение прошлого неудачного контура

- Что уже было сделано клиентом:
- Что мы берём в работу:
- Что мы не повторяем:
- Как у нас аналитика превращается в решение:

## 10. Альтернативы для клиента

| Альтернатива | Что в ней не так | Наш ответ |
|---|---|---|
| Делать своими силами |  |  |
| Нанять человека внутрь |  |  |
| Пойти к крупным консультантам |  |  |
| Ничего не менять |  |  |

## 10.1. Гарантия / рамка доверия

- Как устроена ответственность команды:
- Что происходит, если ценность не подтверждается:
- Что передаётся клиенту в любом случае:

## 11. Что нужно уточнить

- [ ] 
- [ ] 
- [ ] 

## 12. Версия для Gamma

Этот документ должен быть достаточно полным для прямой укладки в Gamma.
Перед экспортом проверить:

- есть ли сильный opening с проблемой клиента;
- названа ли живая ось перехода, а не только общий тип проекта;
- видны ли этапы и логика решения;
- перечислены ли решения, которые сможет принять клиент;
- достаточно ли конкретны результаты;
- не потеряны ли сроки, деньги и следующий шаг.
"""


INTERNAL_TEMPLATE = """---
тип: внутренний-qa-кп
клиент: {client}
дата: {today}
статус: внутренний-review
тема: {offer_slug}
---

# Внутренний QA КП для {client}

## 1. Archetype-to-proposal routing

- Тип КП: стратегическое / трансформационное / внедренческое / нишевое:
- Основной архетип проекта:
- Альтернативные архетипы:
- Почему выбран основной архетип:
- Уверенность / что нужно уточнить:

## 2. Продуктовый маршрут витрины

- Какие страницы актуальной продуктовой витрины проверены:
- Основной продукт витрины:
- Соседние продукты:
- Отраслевые / классовые витрины:
- Связки витрины по кейсам, контенту, рычагам и направлениям:
- Отраслевая / классовая сборка:
- Что сознательно не включаем в scope:
- Как объяснить маршрут клиенту без внутренних кодов:
- Не устарел ли маршрут по сравнению с актуальной витриной:

## 3. Методологический пакет

- Вероятные BPM / BPV / BPA / SIEF:
- Релевантные SI:
- Какие артефакты это предсказывает:
- Какие модели можно упоминать клиенту:
- Какие модели остаются только внутренней методологией:

## 4. ПВЦЗ / PCWZ reuse

- Похожие проблемы:
- Похожие вызовы:
- Похожие цели / задачи:
- Похожие реализованные проекты:
- Какие формулировки из reuse стоит перенести в КП:

## 5. Кейсы-доноры

- Кейс-донор 1:
- Что доказывает:
- Кейс-донор 2:
- Что доказывает:
- Кейс-донор 3:
- Что доказывает:
- Что не стоит показывать, потому что донор слабый или нерелевантный:

## 6. MEDDPICC QA контента

- `M — Metrics`: какие метрики уже есть в тексте и каких не хватает?
- `E — Economic Buyer`: достаточно ли текст говорит на языке денег, риска и цены промедления?
- `D — Decision Criteria`: понятны ли критерии выбора?
- `D — Decision Process`: виден ли следующий шаг после прочтения?
- `P — Paper Process`: ясно ли описаны этапы, оплаты, артефакты и формат работы?
- `I — Identify Pain`: достаточно ли остро названа проблема?
- `C — Champion`: поможет ли текст внутреннему чемпиону защищать проект внутри компании?
- `C — Competition`: закрыт ли вопрос «почему не сами / не другой подрядчик / не потом»?

## 7. Комментарии к улучшению

- Что усилить:
- Что сократить:
- Что уточнить у клиента:
- Что перенести в приложение / расширенную версию:

## 7.1. Gamma-readiness QA

- Можно ли вставить клиентский текст в Gamma без дополнительной смысловой сборки:
- Есть ли у каждого слайда одно основное сообщение:
- Не смешаны ли несколько решений на одном слайде:
- Переведены ли внутренние BPM / BPV / BPA / SI / SIEF / ПВЦЗ / PCWZ в клиентский язык:
- Хватает ли кейсов и референсов:
- Не торчит ли наружу MEDDPICC или внутренняя методологическая арматура:

## 7.2. 9 рычагов / implementation QA

- Выбран ли правильный режим: полная 9-рычажная карта или лёгкая проверка границ для нишевого КП:
- Не пытается ли КП чинить нижние рычаги без решений наверху:
- Есть ли связь стратегии с финансами и клиентскими политиками:
- Описан ли новый образ организации, который порождает выбранная стратегическая ставка:
- Понятно ли, как этот образ организации меняет продажи, процессы, оргструктуру, HR/компетенции, IT/данные и культуру:
- Не сведены ли IT/данные к узкому дашборду или аналитике вместо целевого IT-контура новой операционной модели:
- Для каждого релевантного рычага названы ли артефакты и ритмы:
- Есть ли мост от проектирования к сопровождению внедрения:
- Не выглядит ли внедрение как навязанная допродажа:

## 8. Проверка оси оффера

- Какая формула перехода лежит в центре КП:
- Нет ли здесь пустого штампа `модель А / модель Б`:
- Как переписать ось оффера более предметно, если сейчас она слишком абстрактна:
- Какие 1–2 фразы внутренний чемпион сможет пересказать внутри клиента:

## 9. Архивация после отправки

- Финальный файл сохранён:
- Архивная карточка создана:
- Запись в реестре обновлена:
- Архивация считается завершённой только если заполнены все три пункта выше.

## 10. Commercial metric trace

- `metric_storage_primary`: Реестр коммерческого происхождения проектов / Связь с пирамидой метрик
- `metric_storage_secondary`: архив КП / commercial_origin_trace; Notion / CRM / Calendar / Soroka; sales forecast / договор / счёт после win
- `client_entity`:
- `lead_origin`:
- `source_type`:
- `source_detail`:
- `partner_channel_candidate`:
- `region`:
- `stage`:
- `product_route`:
- `ICP-fit`:
- `proposal_status`:
- `expected_revenue`:
- `win/loss/outcome`:
- `data_lack_status`: sourced / partially_sourced / needs_storage_definition / no_metric_signal
- Что добавить в `Бэклог источников и сигналов для пирамиды метрик`:
"""


ARCHIVE_CARD_TEMPLATE = """---
тип: архивная-карточка-кп
клиент: {client}
дата-отправки: {sent_date}
дата-архивации: {today}
статус: отправлено-клиенту
домен: коммерческая
тема: {topic_slug}
---

# {client} — архивная карточка КП

## Что запросил клиент

- Заполнить краткое описание исходного запроса:

## Какую задачу решало КП

- В чём была управленческая задача:
- Какая ось перехода лежала в центре оффера:
- Почему эта ось сильнее, чем абстрактный консультантский штамп:

## Что именно было отправлено клиенту

- Формат файла:
- Ключевые смысловые блоки:
- Что было обещано на выходе:

## Коммерческая рамка

- Формат:
- Срок:
- Стоимость:
- Оплата:

## Что важно помнить при возврате клиента

- Ключевая чувствительность клиента:
- Вероятные вопросы или возражения:
- Что нельзя потерять при следующем заходе:

## Связанные файлы

### Финальный файл

- [{final_file_name}]({final_file_path})

## Internal commercial metric trace

- `metric_storage_primary`: Реестр коммерческого происхождения проектов / Связь с пирамидой метрик
- `metric_storage_secondary`: архив КП / commercial_origin_trace; Notion / CRM / Calendar / Soroka; sales forecast / договор / счёт после win
- `client_entity`:
- `lead_origin`:
- `source_type`:
- `source_detail`:
- `partner_channel_candidate`:
- `region`:
- `stage`: proposal-sent
- `product_route`:
- `ICP-fit`:
- `proposal_status`: sent
- `expected_revenue`:
- `win/loss/outcome`: unknown
- `data_lack_status`: sourced / partially_sourced / needs_storage_definition / no_metric_signal
- `next_metric_action`: обновить outcome после ответа клиента; при win перенести trace в forecast / договор / проектный контур
"""


def slugify(text: str) -> str:
    out = []
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in {" ", "-", "_"}:
            out.append("-")
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "offer"


def validate_offer_axis(offer: str, allow_model_ab_axis: bool) -> None:
    normalized = offer.lower().replace("ё", "е")
    has_model_a = re.search(r"модел\w*\s+а\b", normalized)
    has_model_b = re.search(r"модел\w*\s+б\b", normalized)
    if has_model_a and has_model_b and not allow_model_ab_axis:
        raise SystemExit(
            "Offer axis rejected: replace abstract `модель А / модель Б` with a more specific transition, or pass --allow-model-ab-axis if this is the client's exact language."
        )


def default_output(client: str) -> Path:
    home = Path.home()
    name = f"{date.today().isoformat()}-КП-{client}.md"
    return home / "Library/CloudStorage/GoogleDrive-balahnin@paper-planes.ru/Мой диск/CLAUDE/Vault/10-отделы/02-продажи-маркетинг/04 — Коммерческие функции/04.3 — Составление КП/03 — Черновики" / name


def default_internal_output(output: Path) -> Path:
    return output.with_name(output.stem + "-internal.md")


def default_archive_card_output(client: str, final_file: Path) -> Path:
    return final_file.parent / f"{date.today().isoformat()}-{client}-КП.md"


def default_archive_registry(final_file: Path) -> Path:
    return final_file.parent / "__реестр-архивных-КП.md"


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser()
    subparsers = ap.add_subparsers(dest="command", required=True)

    scaffold = subparsers.add_parser("scaffold")
    scaffold.add_argument("--client", required=True)
    scaffold.add_argument("--offer", required=True)
    scaffold.add_argument("--output")
    scaffold.add_argument("--internal-output")
    scaffold.add_argument("--with-internal-qa", action="store_true")
    scaffold.add_argument("--allow-model-ab-axis", action="store_true")

    archive = subparsers.add_parser("archive")
    archive.add_argument("--client", required=True)
    archive.add_argument("--topic", required=True)
    archive.add_argument("--final-file", required=True)
    archive.add_argument("--registry")
    archive.add_argument("--sent-date", default=date.today().isoformat())
    archive.add_argument("--card-output")
    return ap


def parse_args() -> argparse.Namespace:
    argv = sys.argv[1:]
    if not argv or argv[0] not in {"scaffold", "archive"}:
        argv = ["scaffold", *argv]
    return build_parser().parse_args(argv)


def scaffold_mode(args: argparse.Namespace) -> int:
    validate_offer_axis(args.offer, args.allow_model_ab_axis)

    output = Path(args.output) if args.output else default_output(args.client)
    client_doc = CLIENT_TEMPLATE.format(
        client=args.client,
        offer=args.offer,
        offer_slug=slugify(args.offer),
        today=date.today().isoformat(),
    )
    write_file(output, client_doc)
    print(output)

    if args.with_internal_qa:
        internal_output = Path(args.internal_output) if args.internal_output else default_internal_output(output)
        internal_doc = INTERNAL_TEMPLATE.format(
            client=args.client,
            offer_slug=slugify(args.offer),
            today=date.today().isoformat(),
        )
        write_file(internal_output, internal_doc)
        print(internal_output)
    return 0


def upsert_registry_entry(registry_path: Path, client: str, entry: str) -> None:
    text = registry_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    marker = "## Архивные карточки"
    if marker not in lines:
        raise SystemExit(f"Registry format error: marker `{marker}` not found in {registry_path}")

    replaced = False
    for i, line in enumerate(lines):
        if line.startswith("- ") and f"· {client} ·" in line:
            lines[i] = entry
            replaced = True
            break

    if not replaced:
        insert_at = lines.index(marker) + 1
        while insert_at < len(lines) and lines[insert_at].strip() == "":
            insert_at += 1
        lines.insert(insert_at, entry)

    registry_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def archive_mode(args: argparse.Namespace) -> int:
    final_file = Path(args.final_file).resolve()
    registry = Path(args.registry).resolve() if args.registry else default_archive_registry(final_file).resolve()

    if not final_file.exists():
        raise SystemExit(f"Final file not found: {final_file}")
    if not registry.exists():
        raise SystemExit(f"Registry not found: {registry}")

    card_output = (Path(args.card_output).resolve() if args.card_output else default_archive_card_output(args.client, final_file).resolve())
    card_doc = ARCHIVE_CARD_TEMPLATE.format(
        client=args.client,
        sent_date=args.sent_date,
        today=date.today().isoformat(),
        topic_slug=slugify(args.topic),
        final_file_name=final_file.name,
        final_file_path=str(final_file),
    )
    write_file(card_output, card_doc)

    entry = (
        f"- {args.sent_date} · {args.client} · {args.topic} · отправлено клиенту · "
        f"[архивная карточка](<{card_output}>) · [финальный PDF](<{final_file}>)"
    )
    upsert_registry_entry(registry, args.client, entry)

    registry_text = registry.read_text(encoding="utf-8")
    if not final_file.exists() or not card_output.exists() or str(card_output) not in registry_text:
        raise SystemExit("Archive completion check failed: full bundle was not created.")

    print(card_output)
    print(registry)
    return 0


def main() -> int:
    args = parse_args()
    if args.command == "archive":
        return archive_mode(args)
    return scaffold_mode(args)


if __name__ == "__main__":
    raise SystemExit(main())
