BEGIN;

SELECT * FROM cart_product;

DELETE FROM cart_product WHERE id = 7;

SELECT * FROM carts;

UPDATE carts SET total = total - (SELECT price FROM products WHERE product_id = 1487) WHERE cart_id = 2;

ROLLBACK;
COMMIT;