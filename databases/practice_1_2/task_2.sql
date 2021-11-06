-- -- number of customers by city and street (INNER JOIN)
EXPLAIN ANALYZE
SELECT c.name, s.name, COUNT(customer.id) AS customer_count FROM customer
JOIN address a on a.id = customer.address
JOIN city_street cs on cs.id = a.city_street_id
JOIN street s on cs.street_id = s.id
JOIN city c on cs.city_id = c.id
GROUP BY c.id, s.id
ORDER BY customer_count DESC;
-- Sort  (cost=164.26..166.76 rows=1000 width=1048) (actual time=1.658..1.661 rows=6 loops=1)
CREATE INDEX idx_city_street ON city_street(city_id, street_id);
-- Sort  (cost=144.30..146.80 rows=1000 width=1048) (actual time=2.579..2.584 rows=6 loops=1)
DROP INDEX idx_city_street;


-- -- customers with no car rentals (LEFT OUTER JOIN)
SELECT customer.* FROM customer
LEFT JOIN rent r on customer.id = r.customer
WHERE r.customer IS NULL;

-- -- top profitable customers who rented cars from 25 to 30 days (LEFT JOIN)
EXPLAIN ANALYSE
SELECT c.*, SUM(price) AS sum_per_year FROM customer c
LEFT JOIN rent r on c.id = r.customer
WHERE days BETWEEN 25 AND 30
GROUP BY c.id
ORDER BY sum_per_year DESC;
-- Sort  (cost=102.26..103.28 rows=406 width=81) (actual time=1.041..1.060 rows=330 loops=1)
CREATE INDEX idx_rent_days ON rent(days);
-- Sort  (cost=86.79..87.81 rows=406 width=81) (actual time=1.011..1.032 rows=330 loops=1)
DROP INDEX idx_rent_days;
