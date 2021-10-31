BEGIN;

CREATE MATERIALIZED VIEW user_purchases_by_category AS
    SELECT carts.user_id, c.category_title, SUM(subtotal) AS subtotal, SUM(total) AS total, COUNT(cp.product_id) AS products_in_category
    FROM carts
    JOIN cart_product cp on carts.cart_id = cp.cart_id
    JOIN products p on p.product_id = cp.product_id
    JOIN categories c on c.category_id = p.category_id
    GROUP BY carts.user_id, c.category_id
    ORDER BY user_id, c.category_id
    WITH NO DATA;

REFRESH MATERIALIZED VIEW user_purchases_by_category;

SELECT * FROM user_purchases_by_category;

DROP MATERIALIZED VIEW IF EXISTS user_purchases_by_category;

ROLLBACK;
COMMIT;