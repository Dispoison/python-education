-- 1. среднюю сумму всех завершенных сделок
SELECT AVG(total) as average_total_price
FROM orders
JOIN order_status os on orders.order_status_id = os.order_status_id
WHERE os.status_name = 'Finished';

-- 2. вывести максимальную сумму сделки за 3 квартал 2020
SELECT MAX(total) as max_sum_in_third_quarter
FROM orders
WHERE EXTRACT(YEAR FROM updated_at) = '2020' AND EXTRACT(QUARTER FROM updated_at) = 3;