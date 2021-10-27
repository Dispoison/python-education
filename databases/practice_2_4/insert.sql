BEGIN;

LOCK TABLE categories IN EXCLUSIVE MODE;
SELECT setval('categories_category_id_seq', COALESCE((SELECT MAX(category_id)+1 FROM categories), 1), false);

LOCK TABLE products IN EXCLUSIVE MODE;
SELECT setval('products_product_id_seq', COALESCE((SELECT MAX(product_id)+1 FROM products), 1), false);

SELECT * FROM categories;

INSERT INTO categories (category_title, category_description) VALUES
    ('Bakery', 'Delicious bakery');

SAVEPOINT bakery;

SELECT * FROM products;

INSERT INTO products (product_title, product_description, in_stock, price, slug, category_id) VALUES
    ('Sausage', 'Tasty sausage', 9, 55, 'sausage', currval('categories_category_id_seq'));

ROLLBACK TO SAVEPOINT bakery;

INSERT INTO products (product_title, product_description, in_stock, price, slug, category_id) VALUES
    ('Bread', 'Tasty bread', 15, 16, 'bread', currval('categories_category_id_seq'));

ROLLBACK;
COMMIT;