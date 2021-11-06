SELECT c.category_title, COUNT(products.product_id) as product_count
FROM products
JOIN categories c on products.category_id = c.category_id
GROUP BY c.category_title
ORDER BY product_count DESC;
