#!/usr/bin/env python3
"""Журнал договорных решений: подбор, чтение, проверка и атомарный пересмотр."""
import argparse
import copy
from datetime import date
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile

DEFAULT = Path(__file__).resolve().parents[1] / 'references' / 'решения.json'
STATES = {'Принято', 'Отклонено', 'Кандидат', 'Заменено'}
LEVELS = {'Только проект', 'Шаблон для адаптации', 'Предпочтение владельца', 'Общее правило владельца'}
REQUIRED = {'id', 'название', 'тема', 'риск', 'решение', 'статус', 'область',
            'условия_применения', 'не_переносить', 'остаточный_риск', 'источник', 'состояние_редакции'}


def check_card(card):
    if not isinstance(card, dict):
        raise ValueError('Нужен объект карточки')
    if REQUIRED - card.keys():
        raise ValueError('Карточка неполна: ' + ', '.join(sorted(REQUIRED - card.keys())))
    if not isinstance(card['id'], str) or not re.fullmatch(r'LPP-\d{3,}', card['id']):
        raise ValueError('ID должен иметь вид LPP-014')
    for key in ('название', 'тема', 'риск', 'решение', 'состояние_редакции'):
        if not isinstance(card[key], str) or not card[key].strip():
            raise ValueError('Неполное текстовое поле: ' + key)
    if card['статус'] not in STATES:
        raise ValueError('Неизвестное состояние карточки')
    scope = card['область']
    if not isinstance(scope, dict) or scope.get('уровень') not in LEVELS:
        raise ValueError('Не определена область решения')
    for key in ('проект', 'юрисдикция', 'сторона', 'тип_сделки'):
        if not isinstance(scope.get(key), str) or not scope[key].strip():
            raise ValueError('Не определено поле области: ' + key)
    for key in ('условия_применения', 'не_переносить', 'остаточный_риск'):
        if not isinstance(card[key], list) or not all(isinstance(x, str) and x.strip() for x in card[key]):
            raise ValueError('Нужен список строк: ' + key)
    src = card['источник']
    if not isinstance(src, dict):
        raise ValueError('Не задан источник')
    for key in ('тип', 'цитата', 'локатор', 'дата'):
        if not isinstance(src.get(key), str) or not src[key].strip():
            raise ValueError('Не определён источник: ' + key)
    if src['тип'] not in {'Прямое решение владельца', 'Предложение агента'}:
        raise ValueError('Недопустимый тип источника')
    if card['статус'] != 'Кандидат' and src['тип'] != 'Прямое решение владельца':
        raise ValueError('Принятие, отказ или замена требуют прямого решения владельца')
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', src['дата']):
        raise ValueError('Дата источника должна иметь вид ГГГГ-ММ-ДД')
    date.fromisoformat(src['дата'])
    if not isinstance(src.get('физические_источники'), list):
        raise ValueError('Нужен список физических источников')
    if 'история' in card and not isinstance(card['история'], list):
        raise ValueError('История должна быть списком')


def validate(data):
    if not isinstance(data, dict) or data.get('версия_схемы') != 1 or not isinstance(data.get('решения'), list):
        raise ValueError('Неверная структура журнала')
    seen = set()
    for card in data['решения']:
        check_card(card)
        if card['id'] in seen:
            raise ValueError('Повтор ID: ' + card['id'])
        seen.add(card['id'])
    for card in data['решения']:
        for ref in card.get('связанные_решения', []):
            if ref not in seen:
                raise ValueError('Неизвестная связанная карточка: ' + ref)


def load(path):
    data = json.loads(path.read_text(encoding='utf-8'))
    validate(data)
    return data


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def save(path, data, expected):
    validate(data)
    fd, name = tempfile.mkstemp(prefix='.decisions-', suffix='.tmp', dir=path.parent)
    temp = Path(name)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            json.dump(data, stream, ensure_ascii=False, indent=2)
            stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
        load(temp)
        if fingerprint(load(path)) != expected:
            raise ValueError('Журнал изменён другим процессом; перечитай его перед записью')
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ledger', type=Path, default=DEFAULT)
    actions = parser.add_subparsers(dest='action', required=True)
    listing = actions.add_parser('list'); listing.add_argument('--query', default=''); listing.add_argument('--limit', type=int, default=15)
    showing = actions.add_parser('show'); showing.add_argument('--id', required=True)
    actions.add_parser('validate')
    record = actions.add_parser('record'); record.add_argument('--input', type=Path, required=True)
    record.add_argument('--revise', action='store_true'); record.add_argument('--reason')
    args = parser.parse_args()
    # Постоянный путь блокировки переживает атомарную замену самого JSON.
    lock = None
    if args.action == 'record':
        lock_key = hashlib.sha256(str(args.ledger.resolve()).encode()).hexdigest()
        lock = open(Path(tempfile.gettempdir()) / ('lawyer-pp-' + lock_key + '.lock'), 'a')
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
    data = load(args.ledger)
    if args.action == 'validate':
        print('Журнал корректен. Карточек: ' + str(len(data['решения'])))
    elif args.action == 'show':
        found = next((x for x in data['решения'] if x['id'] == args.id), None)
        if found is None:
            raise ValueError('Карточка не найдена: ' + args.id)
        print(json.dumps(found, ensure_ascii=False, indent=2))
    elif args.action == 'list':
        if not 1 <= args.limit <= 50:
            raise ValueError('Лимит должен быть от 1 до 50')
        terms = args.query.lower().split()
        ranked = []
        for card in data['решения']:
            text = json.dumps({k: v for k, v in card.items() if k != 'история'}, ensure_ascii=False).lower()
            score = sum(term in text for term in terms)
            if not terms or score:
                ranked.append((score, card))
        ranked.sort(key=lambda item: (-item[0], item[1]['id']))
        for _, card in ranked[:args.limit]:
            print(f"{card['id']} | {card['статус']} | {card['название']} | {card['область']['уровень']} | {card['область']['проект']}")
        print('Совпадений: ' + str(len(ranked)) + '; показано: ' + str(min(len(ranked), args.limit)))
    elif args.action == 'record':
        card = json.loads(args.input.read_text(encoding='utf-8')); check_card(card)
        expected = fingerprint(data)
        current = next((x for x in data['решения'] if x['id'] == card['id']), None)
        if current:
            compared = lambda x: {k: v for k, v in x.items() if k != 'история'}
            if compared(current) == compared(card):
                print('Без изменений: ' + card['id']); return
            if not args.revise or not args.reason:
                raise ValueError('Пересмотр требует --revise и --reason')
            if current['источник'] == card['источник']:
                raise ValueError('Пересмотр требует нового или уточнённого источника решения')
            if current['область'] != card['область']:
                raise ValueError('Для другой области создай отдельную карточку; локальное исключение не затирает исходное решение')
            previous = copy.deepcopy(current); previous.pop('история', None)
            card['история'] = copy.deepcopy(current.get('история', [])) + [{'основание': args.reason, 'предыдущая_версия': previous}]
            data['решения'][data['решения'].index(current)] = card
            result = 'Уточнено: '
        else:
            if args.revise:
                raise ValueError('Для пересмотра нужна существующая карточка')
            if card.get('история'):
                raise ValueError('История новой карточки формируется при пересмотре')
            data['решения'].append(card); result = 'Сохранено: '
        save(args.ledger, data, expected)
        written = next(x for x in load(args.ledger)['решения'] if x['id'] == card['id'])
        if written != card:
            raise ValueError('Проверка после записи не пройдена')
        print(result + card['id'] + ' — ' + card['название'])


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, TypeError, KeyError) as error:
        print('Ошибка: ' + str(error), file=sys.stderr)
        sys.exit(1)
