BEGIN;

SELECT * FROM cart_product;

INSERT INTO cart_product (cart_id, product_id) VALUES
    (2, 5);

SELECT * FROM carts WHERE cart_id = 2;

UPDATE carts SET total = total + (SELECT price FROM products WHERE product_id = 5) WHERE cart_id = 2;

ROLLBACK;
COMMIT;