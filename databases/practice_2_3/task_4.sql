-- 1. Вывести продукты, которые ни разу не попадали в корзину.
SELECT products.*
FROM products
LEFT JOIN cart_product cp on products.product_id = cp.product_id
WHERE cp.cart_id IS NULL;

-- 2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли).
WITH carts_with_no_orders AS (
    SELECT carts.cart_id
    FROM carts
    LEFT JOIN orders o on carts.cart_id = o.cart_id
    WHERE o.order_id IS NULL
    )
SELECT products.*
FROM products
LEFT JOIN cart_product cp on products.product_id = cp.product_id
WHERE cp.cart_id IN (SELECT cart_id FROM carts_with_no_orders);

-- 3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.
SELECT products.*, COUNT(cp.id) AS product_count
FROM products
JOIN cart_product cp on products.product_id = cp.product_id
GROUP BY products.product_id
ORDER BY product_count DESC
LIMIT 10;

-- 4. Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформляли заказы чаще всего.
SELECT products.*, COUNT(cp.id) AS product_count
FROM products
JOIN cart_product cp on products.product_id = cp.product_id
JOIN carts c on cp.cart_id = c.cart_id
JOIN orders o on c.cart_id = o.cart_id
JOIN order_status os on o.order_status_id = os.order_status_id
WHERE os.status_name = 'Finished'
GROUP BY products.product_id
ORDER BY product_count DESC
LIMIT 10;

-- 5. Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе).
SELECT users.*, SUM(o.total) AS total_sum
FROM users
JOIN carts c on users.user_id = c.user_id
JOIN orders o on c.cart_id = o.cart_id
GROUP BY users.user_id
ORDER BY total_sum DESC
LIMIT 5;

-- 6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).
SELECT users.*, COUNT(o.order_id) AS orders_count
FROM users
JOIN carts c on users.user_id = c.user_id
JOIN orders o on c.cart_id = o.cart_id
GROUP BY users.user_id
ORDER BY orders_count DESC
LIMIT 5;

-- 7. Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы.
SELECT users.*, COUNT(c.cart_id) AS carts_count
FROM users
JOIN carts c on users.user_id = c.user_id
LEFT JOIN orders o on c.cart_id = o.cart_id
WHERE o.order_id IS NULL
GROUP BY users.user_id
ORDER BY carts_count
LIMIT 5;
