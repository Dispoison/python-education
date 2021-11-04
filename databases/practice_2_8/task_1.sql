SELECT category_title, product_title, price, AVG(price) OVER (PARTITION BY c.category_id) AS avg,
       price - AVG(price) OVER (PARTITION BY c.category_id) AS variance
FROM products
JOIN categories c on c.category_id = products.category_id;
