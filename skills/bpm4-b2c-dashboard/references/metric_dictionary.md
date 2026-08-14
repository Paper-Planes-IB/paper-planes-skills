# Словарь метрик B2C-дашборда

## Денежные метрики

| Метрика | Формула |
|---|---|
| Gross revenue | `sum(gross_revenue)` |
| Discount amount | `sum(discount_amount)` |
| Return amount | `sum(return_amount)` |
| Net revenue | `sum(net_revenue)` |
| Cost amount | `sum(cost_amount)` |
| Gross profit | `sum(gross_profit)` или `sum(net_revenue - cost_amount)` |
| Gross margin | `gross_profit / net_revenue` |
| Average order value | `net_revenue / positive_orders` |
| Average item price | `line_net_revenue / quantity` |

## Клиентские метрики

| Метрика | Формула |
|---|---|
| Customers | `count_distinct(customer_id_hash)` |
| New customers | клиенты, у которых первая покупка в выбранном периоде |
| Returning customers | клиенты с покупкой в периоде и покупкой до периода |
| Repeat customers | клиенты с 2+ покупками за окно анализа |
| Repeat rate | `repeat_customers / identified_customers` |
| Purchase frequency | `positive_orders / identified_customers` |
| Orders per repeat customer | `positive_orders_of_repeat_customers / repeat_customers` |
| Days to second order | `second_order_date - first_order_date` |
| Active customers | клиенты с покупкой за выбранное окно активности |
| Dormant customers | клиенты без покупки дольше порога спячки |
| Lost customers | клиенты без покупки дольше порога потери |

## Товарные метрики

| Метрика | Формула |
|---|---|
| Items sold | `sum(quantity)` |
| Check depth | `sum(quantity) / positive_orders` |
| Category revenue share | `category_net_revenue / total_net_revenue` |
| Category gross profit share | `category_gross_profit / total_gross_profit` |
| Category repeat contribution | repeat rate клиентов, начавших с категории |

## RFM

| Поле | Формула |
|---|---|
| Recency | дней с последней покупки до даты анализа |
| Frequency | количество положительных чеков за окно анализа |
| Monetary | сумма net-выручки за окно анализа |
| R score | квантиль или бизнес-порог Recency |
| F score | квантиль Frequency |
| M score | квантиль Monetary |
| RFM segment | правило на основе R, F, M |

## Пороговые сегменты RFM

| Сегмент | Типовое правило |
|---|---|
| Champions | высокий R, высокий F, высокий M |
| Loyal | высокий R, высокий F |
| Potential loyalists | высокий R, средний F/M |
| New customers | высокий R, низкий F |
| Need attention | средний R, средний F/M |
| At risk | низкий R, высокий F/M |
| Hibernating | низкий R, низкий F/M |
| Lost | очень низкий R |

## Сравнения

| Сравнение | Правило |
|---|---|
| Месяц к месяцу | текущий период против предыдущего периода такой же длины |
| Год к году | текущий период против тех же дат прошлого года |
| Like-for-like | сравнение только по объектам, категориям или каналам, которые существовали в обоих периодах |
| Когорты | сравнение по месяцу первой покупки и месяцу жизни клиента |
