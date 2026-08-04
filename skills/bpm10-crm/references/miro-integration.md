# БПМ-10. Miro-интеграция для CRM-моделирования

## 1. Назначение

Эта инструкция описывает, как Codex должен подключаться к Miro и воспроизводимо рисовать CRM-модель данных и схему CRM в рамках БПМ-10.

Инструкция обобщает проверенный проектный опыт, где через Miro API были построены:

- модель данных CRM Bitrix24;
- схема воронок CRM;
- схема воронок в формате клиентского референса: большой контейнер, верхняя плашка процесса, класс 4R, сущность, владелец, этапы внутри контейнера.

## 2. Что должен уметь повторить другой Codex

Другой Codex должен уметь:

1. Получить доступ к Miro REST API без хранения секретов в файлах.
2. Найти нужную доску и исходные фреймы.
3. Считать структуру референсной схемы: фреймы, карточки, цвета, тексты, связи.
4. Создать новый фрейм для CRM-модели данных.
5. Создать новый фрейм для CRM-схемы.
6. Нарисовать блоки, этапы и связи через Miro API.
7. Проверить, сколько блоков и связей реально созданы.
8. Не перезаписывать и не удалять исходные клиентские фреймы без отдельного подтверждения.

## 3. Безопасность доступа

Нельзя писать Miro token, client secret или OAuth secret:

- в Markdown-файлы;
- в кодовые файлы проекта;
- в финальные ответы пользователю;
- в Miro-блоки;
- в историю shell-команд, если можно избежать.

Рабочий вариант для локального запуска:

```bash
export MIRO_ACCESS_TOKEN='...'
```

После работы с токеном, который пользователь прислал в чат или скриншотом, нужно сказать пользователю, что токен / secret лучше перевыпустить.

## 4. Как получить идентификатор доски

Из Miro-ссылки:

```text
https://miro.com/app/board/BOARD_ID/?moveToWidget=WIDGET_ID
```

Board ID:

```text
BOARD_ID
```

В API его нужно URL-encode:

```js
const boardId = process.env.MIRO_BOARD_ID;
if (!boardId) throw new Error('MIRO_BOARD_ID is required');
const base = `https://api.miro.com/v2/boards/${encodeURIComponent(boardId)}`;
```

## 5. Базовая функция Miro API

```js
async function miro(path, method = 'GET', body) {
  const res = await fetch(base + path, {
    method,
    headers: {
      Authorization: `Bearer ${process.env.MIRO_ACCESS_TOKEN}`,
      'Content-Type': 'application/json'
    },
    body: body ? JSON.stringify(body) : undefined
  });

  const text = await res.text();
  if (!res.ok) throw new Error(`${method} ${path} -> ${res.status}: ${text}`);
  return text ? JSON.parse(text) : null;
}
```

## 6. Как читать доску

Miro API возвращает объекты постранично. Нужно читать все страницы.

```js
async function getAll(path) {
  let url = `${base}${path}${path.includes('?') ? '&' : '?'}limit=50`;
  const arr = [];

  while (url) {
    const res = await fetch(url, {
      headers: { Authorization: `Bearer ${process.env.MIRO_ACCESS_TOKEN}` }
    });
    const text = await res.text();
    if (!res.ok) throw new Error(`${res.status} ${text}`);
    const data = JSON.parse(text);
    arr.push(...(data.data || []));
    url = data.links?.next || null;
  }

  return arr;
}
```

Что читать:

```js
const items = await getAll('/items?');
const connectors = await getAll('/connectors?');
```

## 7. Как найти фреймы и элементы

```js
const frames = items
  .filter((it) => it.type === 'frame')
  .map((f) => ({
    id: f.id,
    title: f.data?.title,
    x: f.position?.x,
    y: f.position?.y,
    w: f.geometry?.width,
    h: f.geometry?.height
  }));
```

Если нужно найти карточки по тексту:

```js
const matches = items.filter((it) =>
  JSON.stringify(it.data || {})
    .toLowerCase()
    .includes('компания')
);
```

Если нужно прочитать элементы внутри фрейма:

```js
const frameId = '...';
const inFrame = items.filter((it) => it.parent?.id === frameId);
```

Важное наблюдение: Miro иногда показывает элементы внутри фрейма визуально, но API может не считать их дочерними. Тогда проверяй не только `parent.id`, но и координаты внутри границ фрейма.

```js
const b = {
  left: frame.position.x - frame.geometry.width / 2,
  right: frame.position.x + frame.geometry.width / 2,
  top: frame.position.y - frame.geometry.height / 2,
  bottom: frame.position.y + frame.geometry.height / 2
};

const shapesInBounds = items.filter((it) =>
  it.type === 'shape' &&
  it.position &&
  it.position.x >= b.left &&
  it.position.x <= b.right &&
  it.position.y >= b.top &&
  it.position.y <= b.bottom
);
```

## 8. Как создавать фрейм

```js
const frame = await miro('/frames', 'POST', {
  data: {
    title: 'Клиент CRM — схема воронок (draft v1)',
    format: 'custom',
    showContent: true
  },
  style: { fillColor: '#ffffff' },
  position: { x: 105000, y: 45000, origin: 'center' },
  geometry: { width: 82000, height: 76000 }
});
```

Правило: новый draft-фрейм создается рядом с исходным референсом. Не рисовать поверх исходной клиентской схемы, пока пользователь явно не попросил.

## 9. Как создавать блоки

```js
async function box(key, title, x, y, w, h, fill, font = 100) {
  const item = await miro('/shapes', 'POST', {
    data: {
      content: `<p><strong>${title}</strong></p>`,
      shape: 'rectangle'
    },
    style: {
      fillColor: fill,
      borderColor: '#333333',
      borderWidth: '3.0',
      color: '#1a1a1a',
      fontSize: String(font),
      textAlign: 'center',
      textAlignVertical: 'middle'
    },
    position: { x, y, origin: 'center' },
    geometry: { width: w, height: h }
  });

  ids[key] = item.id;
  await new Promise((r) => setTimeout(r, 35));
}
```

Пауза нужна, чтобы снизить риск ограничений API.

## 10. Как создавать связи

```js
async function conn(from, to, label = '', color = '#333333', style = 'normal') {
  const payload = {
    startItem: { id: ids[from], snapTo: 'auto' },
    endItem: { id: ids[to], snapTo: 'auto' },
    shape: 'straight',
    style: {
      startStrokeCap: 'none',
      endStrokeCap: 'stealth',
      strokeWidth: '8.0',
      strokeStyle: style,
      strokeColor: color,
      fontSize: '72'
    }
  };

  if (label) payload.captions = [{ content: label, position: '50%' }];
  await miro('/connectors', 'POST', payload);
  await new Promise((r) => setTimeout(r, 25));
}
```

## 11. Цветовая система для CRM-схемы

Цвета лучше брать из клиентского референса. Если референса нет, используй такую базовую систему:

| Цвет | Смысл |
|---|---|
| `#ffdc4a` | Воронка / процесс |
| `#dedaff` | Класс 4R: Reach, React, Refresh, Re-Engage |
| `#f8d3af` | Сущность CRM |
| `#ffc6c6` | Роль / владелец или отказ |
| `#c6dcff` | Рабочий этап |
| `#adf0c7` | Успешный исход |
| `#93cfdd` | Маршрутизация / системная связь |
| `#eaf8fb` | Фон контейнера воронки |

## 12. Формат воронки в Miro

Каждая воронка рисуется как отдельный большой прямоугольный контейнер.

Верхняя плашка контейнера:

| Плашка | Пример |
|---|---|
| Название процесса | `Продажа оборудования` |
| Класс 4R | `React` |
| Сущность | `Сделка` |
| Владелец / контур | `ОП / ТРП` |

Внутри контейнера размещаются этапы воронки слева направо.

Для читаемости:

- шрифт блоков — `100`, если доска крупная;
- отказные этапы — красные;
- успешные исходы — зеленые;
- связи внутри воронки — горизонтальные;
- межвороночные связи лучше выносить в правую панель переходов, чтобы линии не пересекались.

## 13. Как моделировать CRM-модель данных

Сначала определить сущности и отделить их от полей.

Типовая структура:

| Группа | Пример |
|---|---|
| Стандартные сущности Bitrix24 | Компания, Контакт, Лид, Сделка |
| Типы компаний / клиентские сущности | Конечный клиент, подрядчик, проектный институт, дилер, сервисная компания, производитель оборудования |
| Смарт-процессы и объектный слой | Площадка, сервисный объект, сервисный кейс |
| Сделочные воронки | Оборудование, ролики и ЗИП, сервис |
| Не-сущности | ТКП, договор, тендер, паспорт сделки, АСУ ТП, техническая проработка |

Правило: тип клиента может быть отдельной концептуальной сущностью, но в Bitrix24 обычно хранится как `Компания` + поле `Тип компании`.

## 14. Как моделировать CRM-схему

Сначала собрать этапы в Markdown. Потом переносить в Miro.

Минимальный набор:

| Класс | Что рисовать |
|---|---|
| Reach | Входящая воронка, ABM по типам компаний |
| React | Сделочные воронки |
| Refresh | Прогрев компаний без активной сделки |
| Re-Engage | Развитие текущих / известных клиентов |
| Service | Сервисный кейс, если входит в первую очередь CRM |

Для каждой воронки фиксировать:

- этапы;
- отказные этапы;
- успешные исходы;
- что создает лид;
- что создает сделку;
- что возвращает компанию в Refresh;
- где CRM передает работу в ERP или сервис.

## 15. Проверка после отрисовки

После создания схемы обязательно проверить, что API реально создал блоки и связи.

```js
const frame = items.find((it) => it.id === frameId);
const b = {
  left: frame.position.x - frame.geometry.width / 2,
  right: frame.position.x + frame.geometry.width / 2,
  top: frame.position.y - frame.geometry.height / 2,
  bottom: frame.position.y + frame.geometry.height / 2
};

const shapes = items.filter((it) =>
  it.type === 'shape' &&
  it.position &&
  it.position.x >= b.left &&
  it.position.x <= b.right &&
  it.position.y >= b.top &&
  it.position.y <= b.bottom
);

const shapeIds = new Set(shapes.map((s) => s.id));
const relevantConnectors = connectors.filter((c) =>
  shapeIds.has(c.startItem?.id) || shapeIds.has(c.endItem?.id)
);

console.log({
  frame: frame.data.title,
  shapes: shapes.length,
  connectors: relevantConnectors.length
});
```

В финальном ответе пользователю нужно назвать:

- ссылку на новый Miro-фрейм;
- количество созданных блоков;
- количество созданных связей;
- что исходный референс не перезаписывался.

## 16. Типовые проблемы

| Проблема | Что делать |
|---|---|
| `new position is outside of parent boundaries` | Не задавать `parent` для shapes; размещать блоки по координатам доски внутри визуальных границ фрейма |
| Фрейм пустой по API, хотя визуально там есть блоки | Проверить элементы по координатам, а не только по `parent.id` |
| Текст не помещается | Увеличить ширину блока, разбить строку через `<br/>`, не уменьшать смысловую точность |
| Много пересечений линий | Вынести межвороночные переходы в отдельную правую панель |
| Слишком много воронок | Схлопнуть процессы, если совпадают стадии, владелец, результат и аналитика |
| Токен прислали в чат | Выполнить read/write-задачу, затем попросить пользователя перевыпустить токен |

## 17. Минимальный итоговый маршрут

1. Прочитать контекст проекта и CRM-документы.
2. Найти Miro-доску и исходные фреймы.
3. Считать референсную схему и цвета.
4. Сформировать Markdown-модель данных.
5. Нарисовать Miro-модель данных.
6. Сформировать Markdown-этапы воронок.
7. Нарисовать Miro-схему CRM.
8. Сверить с пользователем.
9. Исправить шрифт, контейнеры, линии и связи.
10. Зафиксировать ссылку на финальный фрейм и результаты проверки.
