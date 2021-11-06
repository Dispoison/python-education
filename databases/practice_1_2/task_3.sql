CREATE OR REPLACE VIEW customer_pretty_view AS
    SELECT c.id, c.first_name, c.last_name, c.phone_number, ct.name AS city_name, s.name AS street_name, bn.number FROM customer c
        JOIN address a on a.id = c.address
        JOIN building_number bn on bn.id = a.building_number_id
        JOIN city_street cs on cs.id = a.city_street_id
        JOIN street s on cs.street_id = s.id
        JOIN city ct on ct.id = cs.city_id;

SELECT * FROM customer_pretty_view;

DROP VIEW IF EXISTS customer_pretty_view;

--

CREATE OR REPLACE VIEW car_rent_statistic_view AS
    SELECT car.name, car.serial_number, SUM(days) AS total_days, SUM(price) AS total_money, COUNT(DISTINCT customer) AS total_customers FROM car
        JOIN rent r on car.id = r.car
        GROUP BY car.serial_number, car.name;

SELECT * FROM car_rent_statistic_view;

DROP VIEW IF EXISTS car_rent_statistic_view;

--

CREATE MATERIALIZED VIEW branches_statistic_view AS
SELECT b.id, b.name, b.phone_number, ct.name AS city, s.name AS street, bn.number AS building_number,
       SUM(price) AS total_money, COUNT(DISTINCT manufacturer_id) AS car_manufacturers_count,
       COUNT(r.days) AS total_days_rented,
       COUNT(DISTINCT r.customer) AS total_customers, COUNT(DISTINCT r.car) AS total_rented_cars,
       MIN(r.date) AS first_date_rent, MAX(r.date) AS last_date_rent FROM branch b
    JOIN car c on b.id = c.branch_id
    JOIN rent r on c.id = r.car
    JOIN address a on a.id = b.address
    JOIN building_number bn on bn.id = a.building_number_id
    JOIN city_street cs on a.city_street_id = cs.id
    JOIN street s on cs.street_id = s.id
    JOIN city ct on cs.city_id = ct.id
    GROUP BY b.id, ct.id, s.id, bn.id
    ORDER BY b.id
    WITH NO DATA;

REFRESH MATERIALIZED VIEW branches_statistic_view;

SELECT * FROM branches_statistic_view;

DROP MATERIALIZED VIEW IF EXISTS branches_statistic_view;

