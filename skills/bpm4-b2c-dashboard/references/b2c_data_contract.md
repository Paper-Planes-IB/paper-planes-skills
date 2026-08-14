# Контракт данных для B2C-дашборда

## Обязательные таблицы

### 1. `orders`

Шапка чека или заказа. Одна строка — один чек.

Обязательные поля:

- `order_id` — стабильный ID чека;
- `order_datetime` — дата и время покупки;
- `customer_id_hash` — обезличенный ID клиента;
- `store_id` — точка, сайт, филиал или канал;
- `channel` — offline, online, delivery, marketplace, call center;
- `gross_revenue` — сумма до скидок и возвратов;
- `discount_amount` — скидка;
- `return_amount` — сумма возврата;
- `net_revenue` — выручка после скидок и возвратов;
- `cost_amount` — себестоимость, если доступна;
- `gross_profit` — валовая прибыль, если доступна;
- `is_internal` — внутренняя операция;
- `is_test` — тестовая операция;
- `is_b2b_or_partner` — партнёр, корпоративный клиент или закупка для перепродажи.

### 2. `order_items`

Строки чека. Одна строка — товар или услуга внутри чека.

Обязательные поля:

- `order_id`;
- `line_id`;
- `sku_id`;
- `sku_name_masked`;
- `category_l1`;
- `category_l2`;
- `brand_masked`;
- `quantity`;
- `line_gross_revenue`;
- `line_discount_amount`;
- `line_return_amount`;
- `line_net_revenue`;
- `line_cost_amount`;
- `line_gross_profit`.

### 3. `customers`

Обезличенный клиентский справочник.

Обязательные поля:

- `customer_id_hash`;
- `first_order_date`;
- `registration_date`;
- `city_or_region`;
- `acquisition_channel`;
- `gender_group` — если есть и если можно использовать;
- `age_group` — диапазон, без даты рождения;
- `loyalty_status`;
- `is_partner`;
- `is_employee`;
- `is_test_customer`.

### 4. `stores`

Справочник точек, филиалов и каналов.

Обязательные поля:

- `store_id`;
- `store_group`;
- `city_or_region`;
- `format`;
- `open_date`;
- `close_date`;
- `is_active`.

### 5. `partner_registry`

Единый реестр партнёров и корпоративных ролей. Нужен до RFM.

Обязательные поля:

- `subject_id_hash`;
- `source`;
- `role`;
- `matched_name_masked`;
- `match_confidence`;
- `is_partner`;
- `exclude_from_b2c_rfm`;

## Правила расчётного слоя

1. В B2C-метрики входят только строки, где `is_internal = false`, `is_test = false`, `is_b2b_or_partner = false`, `is_employee = false`.
2. RFM строится только по `customer_id_hash`, где `exclude_from_b2c_rfm = false`.
3. Возвраты уменьшают выручку и валовую прибыль в периоде возврата, если клиентская методика не задаёт другой порядок.
4. Чек с нулевой или отрицательной net-выручкой не используется для среднего чека и повторных покупок, но учитывается в сверке возвратов.
5. Клиент без стабильного ID не участвует в RFM, когортах и repeat-метриках. Он учитывается в блоке неопознанных продаж.

## Минимальные сверки

- сумма `net_revenue` по периоду;
- количество чеков;
- количество строк чека;
- количество уникальных клиентов;
- сумма возвратов;
- сумма скидок;
- валовая прибыль;
- доля неопознанных продаж.
