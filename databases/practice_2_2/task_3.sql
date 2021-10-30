-- 1. Продукты, цена которых больше 80.00 и меньше или равно 150.00
SELECT *
FROM products
WHERE 80 < price AND price <= 150;

-- 2. заказы совершенные после 01.10.2020 (поле created_at)
SELECT *
FROM orders
WHERE created_at > '2020-10-01';

-- 3 заказы полученные за первое полугодие 2020 года
SELECT *
FROM orders
WHERE '2020-01-01' <= created_at AND created_at <= '2020-06-30';

SELECT *
FROM orders
WHERE created_at BETWEEN '2020-01-01' AND '2020-06-30';

SELECT *
FROM orders
WHERE EXTRACT(YEAR FROM created_at) = '2020' AND EXTRACT(QUARTER FROM created_at) IN (1, 2);

-- 4. Продукты следующих категорий Category 7, Category 11, Category 18
SELECT *
FROM products
JOIN categories c on products.category_id = c.category_id
WHERE c.category_title IN ('Category 7', 'Category 11', 'Category 18');

-- 5. незавершенные заказы по состоянию на 31.12.2020
SELECT *
FROM orders
JOIN order_status os on orders.order_status_id = os.order_status_id
WHERE os.status_name NOT IN ('Finished', 'Canceled') AND orders.updated_at = '2020-12-31';

-- 6.Вывести все корзины, которые были созданы, но заказ так и не был оформлен.
SELECT carts.*
FROM carts
FULL JOIN orders o on carts.cart_id = o.cart_id
GROUP BY carts.cart_id
HAVING COUNT(o.order_id) = 0;

SELECT carts.*
FROM carts
LEFT JOIN orders o on carts.cart_id = o.cart_id
WHERE o.order_id IS NULL