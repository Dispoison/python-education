CREATE TABLE potential_customers (
	id serial PRIMARY KEY,
	email VARCHAR ( 255 ) NOT NULL,
	name VARCHAR ( 255 ) NOT NULL,
	surname VARCHAR ( 255 ) NOT NULL,
	second_name VARCHAR ( 255 ) NOT NULL,
	city VARCHAR ( 255 ) NOT NULL
);

INSERT INTO potential_customers (email, name, surname, second_name, city) VALUES
    ('email1@gmail.com', 'name 1', 'surname 1', 'second_name 1', 'city 1'),
    ('email2@gmail.com', 'name 2', 'surname 2', 'second_name 2', 'city 2'),
    ('email3@gmail.com', 'name 3', 'surname 3', 'second_name 3', 'city 3'),
    ('email4@gmail.com', 'name 4', 'surname 4', 'second_name 4', 'city 4'),
    ('email5@gmail.com', 'name 5', 'surname 5', 'second_name 5', 'city 5'),
    ('email6@gmail.com', 'name 6', 'surname 6', 'second_name 6', 'city 6'),
    ('email7@gmail.com', 'name 7', 'surname 7', 'second_name 7', 'city 7'),
    ('email8@gmail.com', 'name 8', 'surname 8', 'second_name 8', 'city 8'),
    ('email9@gmail.com', 'name 9', 'surname 9', 'second_name 9', 'city 9'),
    ('email10@gmail.com', 'name 10', 'surname 10', 'second_name 10', 'city 10'),
    ('email11@gmail.com', 'name 11', 'surname 11', 'second_name 11', 'city 11'),
    ('email12@gmail.com', 'name 12', 'surname 12', 'second_name 12', 'city 12'),
    ('email13@gmail.com', 'name 13', 'surname 13', 'second_name 13', 'city 13'),
    ('email14@gmail.com', 'name 14', 'surname 14', 'second_name 14', 'city 14'),
    ('email15@gmail.com', 'name 15', 'surname 15', 'second_name 15', 'city 15'),
    ('email16@gmail.com', 'name 16', 'surname 16', 'second_name 16', 'city 16'),
    ('email17@gmail.com', 'name 17', 'surname 17', 'second_name 17', 'city 17'),
    ('email18@gmail.com', 'name 18', 'surname 18', 'second_name 18', 'city 18'),
    ('email19@gmail.com', 'name 19', 'surname 19', 'second_name 19', 'city 19'),
    ('email20@gmail.com', 'name 20', 'surname 20', 'second_name 20', 'city 20');

SELECT email, first_name, last_name, middle_name
FROM users
WHERE city = 'city 17'
UNION
SELECT email, name, surname, second_name
FROM potential_customers
WHERE city = 'city 17'
