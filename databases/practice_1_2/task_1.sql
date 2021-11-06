--                                           CREATE DATABASE                                       --
-- docker-compose --env-file ./.env.list exec db psql -U postgres -c "CREATE DATABASE car_rental;" --

DROP TABLE IF EXISTS city CASCADE;
CREATE TABLE city (
	id serial PRIMARY KEY,
	name VARCHAR ( 255 ) NOT NULL,
	abbreviation VARCHAR ( 255 ) NOT NULL
);

DROP TABLE IF EXISTS street CASCADE;
CREATE TABLE street (
	id serial PRIMARY KEY,
	name VARCHAR ( 255 ) NOT NULL
);

DROP TABLE IF EXISTS city_street CASCADE;
CREATE TABLE city_street (
	id serial PRIMARY KEY,
	city_id INT NOT NULL,
	street_id INT NOT NULL,
	FOREIGN KEY (city_id)
        REFERENCES city(id),
	FOREIGN KEY (street_id)
        REFERENCES street(id)
);

DROP TABLE IF EXISTS building_number CASCADE;
CREATE TABLE building_number (
	id serial PRIMARY KEY,
	number VARCHAR ( 8 ) NOT NULL
);

DROP TABLE IF EXISTS address CASCADE;
CREATE TABLE address (
	id serial PRIMARY KEY,
	city_street_id INT NOT NULL,
	building_number_id INT NOT NULL,
	FOREIGN KEY (city_street_id)
        REFERENCES city_street(id),
	FOREIGN KEY (building_number_id)
        REFERENCES building_number(id)
);

DROP TABLE IF EXISTS branch CASCADE;
CREATE TABLE branch (
	id serial PRIMARY KEY,
	name VARCHAR ( 255 ) NOT NULL,
	phone_number VARCHAR ( 16 ) NOT NULL,
	address INT NOT NULL,
	FOREIGN KEY (address)
        REFERENCES address(id)
);

DROP TABLE IF EXISTS manufacturer CASCADE;
CREATE TABLE manufacturer (
	id serial PRIMARY KEY,
	name VARCHAR ( 255 ) NOT NULL
);

DROP TABLE IF EXISTS car CASCADE;
CREATE TABLE car (
	id serial PRIMARY KEY,
	name VARCHAR ( 255 ) NOT NULL,
	serial_number VARCHAR ( 8 ) NOT NULL,
	manufacturer_id INT NOT NULL,
	branch_id INT NOT NULL,
	FOREIGN KEY (manufacturer_id)
        REFERENCES manufacturer(id),
	FOREIGN KEY (branch_id)
        REFERENCES branch(id)
);

DROP TABLE IF EXISTS customer CASCADE;
CREATE TABLE customer (
	id serial PRIMARY KEY,
	first_name VARCHAR ( 255 ) NOT NULL,
	last_name VARCHAR ( 255 ) NOT NULL,
	phone_number VARCHAR ( 16 ) NOT NULL,
	address INT NOT NULL,
	FOREIGN KEY (address)
        REFERENCES address(id)
);

DROP TABLE IF EXISTS rent CASCADE;
CREATE TABLE rent (
	id serial PRIMARY KEY,
	date DATE NOT NULL,
	days SMALLINT NOT NULL,
	price NUMERIC NOT NULL,
	customer INT NOT NULL,
	car INT NOT NULL,
	FOREIGN KEY (customer)
        REFERENCES customer(id),
	FOREIGN KEY (car)
        REFERENCES car(id)
);

INSERT INTO city (name, abbreviation) VALUES
    ('Kharkiv', 'KH'),
    ('Kyiv', 'KY');

INSERT INTO street (name) VALUES
    ('Sumska'),
    ('Pushkinska'),
    ('Shevchenka'),
    ('Khreshchatyk'),
    ('Sofiivska');

INSERT INTO city_street (city_id, street_id) VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 3),
    (2, 4),
    (2, 5);

INSERT INTO building_number (number)
    SELECT seq FROM generate_series(1, 100) seq;


do $$
    declare
        city_street_rec record;
        building_number_rec record;
    begin
        for city_street_rec in select * from city_street
        loop
            for building_number_rec in select * from building_number
            loop
                insert into address (city_street_id, building_number_id) values (city_street_rec.id, building_number_rec.id);
            end loop;
        end loop;
    end;
    $$ language plpgsql;

INSERT INTO manufacturer (name)
    SELECT 'manufacturer_' || seq FROM generate_series(1, 30) seq;

INSERT INTO branch (name, phone_number, address)
    SELECT 'branch_' || seq, '+' || (380000000000 + seq::int)::varchar, floor(random() * 600 + 1) FROM generate_series(1, 50) seq;

INSERT INTO car (name, serial_number, manufacturer_id, branch_id)
    SELECT 'car_' || seq, (10000000 + seq::int)::varchar, floor(random() * 30 + 1), floor(random() * 50 + 1) FROM generate_series(1, 100) seq;

INSERT INTO customer (first_name, last_name, phone_number, address)
    SELECT 'first_name_' || seq, 'last_name_' || seq, '+' || (380000000000 + seq::int)::varchar, floor(random() * 600 + 1) FROM generate_series(1, 1000) seq;

INSERT INTO rent (date, days, price, customer, car)
    SELECT timestamp '2019-01-10 00:00:00' + random()*
                 (timestamp '2021-11-05 15:00:00'-
                  timestamp '2019-01-10 00:00:00'),
           floor(random()*31+1), floor(random()*9901+100), floor(random() * 1000 + 1), floor(random() * 100 + 1) FROM generate_series(1, 2000) seq;
