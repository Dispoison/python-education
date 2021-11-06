-- products
BEGIN;

CREATE OR REPLACE VIEW products_price_list AS
    SELECT product_id, product_title, price FROM products;

SELECT * FROM products_price_list;

DROP VIEW IF EXISTS products_price_list;

ROLLBACK;
COMMIT;
-- order and order_status
BEGIN;

CREATE OR REPLACE VIEW order_pretty AS
    SELECT o.order_id, o.cart_id, os.status_name, o.shipping_total, o.total, o.created_at, o.updated_at
    FROM orders o
    JOIN order_status os on os.order_status_id = o.order_status_id;

SELECT * FROM order_pretty;

DROP VIEW IF EXISTS order_pretty;

ROLLBACK;
COMMIT;
-- products and category
BEGIN;

CREATE OR REPLACE VIEW category_products AS
    SELECT p.product_id, c.category_title, p.product_title
    FROM products p
    JOIN categories c on c.category_id = p.category_id
    ORDER BY c.category_title, p.product_title;

SELECT * FROM category_products;

DROP VIEW IF EXISTS category_products;

ROLLBACK;
COMMIT;
