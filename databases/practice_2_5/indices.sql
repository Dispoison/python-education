BEGIN;
EXPLAIN (ANALYZE) SELECT * FROM products WHERE product_title = 'Product 3123';
-- Seq Scan on products  (cost=0.00..155.00 rows=1 width=68) (actual time=0.505..0.683 rows=1 loops=1)
--   Filter: ((product_title)::text = 'Product 3123'::text)
--   Rows Removed by Filter: 3999
-- Planning Time: 0.056 ms
-- Execution Time: 0.695 ms
CREATE INDEX idx_products_title ON products(product_title);
EXPLAIN (ANALYZE) SELECT * FROM products WHERE product_title = 'Product 3123';
-- Index Scan using idx_products_title on products  (cost=0.28..8.30 rows=1 width=68) (actual time=0.078..0.080 rows=1 loops=1)
--   Index Cond: ((product_title)::text = 'Product 3123'::text)
-- Planning Time: 0.273 ms
-- Execution Time: 0.100 ms
ROLLBACK;
COMMIT;


BEGIN;
EXPLAIN ANALYZE SELECT * FROM orders WHERE total > 1000;
-- Seq Scan on orders  (cost=0.00..56.75 rows=138 width=39) (actual time=0.025..0.283 rows=138 loops=1)
--   Filter: (total > '1000'::numeric)
--   Rows Removed by Filter: 1362
-- Planning Time: 0.076 ms
-- Execution Time: 0.302 ms
CREATE INDEX idx_orders_total ON orders(total);
EXPLAIN ANALYZE SELECT * FROM orders WHERE total > 1000;
-- Bitmap Heap Scan on orders  (cost=5.35..45.07 rows=138 width=39) (actual time=0.030..0.067 rows=138 loops=1)
--   Recheck Cond: (total > '1000'::numeric)
--   Heap Blocks: exact=13
--   ->  Bitmap Index Scan on idx_orders_total  (cost=0.00..5.31 rows=138 width=0) (actual time=0.022..0.022 rows=138 loops=1)
--         Index Cond: (total > '1000'::numeric)
-- Planning Time: 0.071 ms
-- Execution Time: 0.088 ms
ROLLBACK;
COMMIT;


BEGIN;
EXPLAIN ANALYZE SELECT * FROM cart_product WHERE cart_id = 14;
-- Seq Scan on cart_product  (cost=0.00..197.44 rows=5 width=12) (actual time=0.029..1.232 rows=6 loops=1)
--   Filter: (cart_id = 14)
--   Rows Removed by Filter: 10989
-- Planning Time: 0.074 ms
-- Execution Time: 1.248 ms
CREATE INDEX idx_cart_product_cart_id ON cart_product(cart_id);
EXPLAIN ANALYZE SELECT * FROM cart_product WHERE cart_id = 14;
-- Index Scan using idx_cart_product_cart_id on cart_product  (cost=0.29..8.37 rows=5 width=12) (actual time=0.012..0.013 rows=6 loops=1)
--   Index Cond: (cart_id = 14)
-- Planning Time: 0.152 ms
-- Execution Time: 0.025 ms
ROLLBACK;
COMMIT;