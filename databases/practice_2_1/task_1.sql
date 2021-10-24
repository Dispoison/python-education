CREATE TABLE categories (
	category_id serial PRIMARY KEY,
	category_title VARCHAR ( 255 ) NOT NULL,
	category_description TEXT NOT NULL
);

CREATE TABLE products (
	product_id serial PRIMARY KEY,
	product_title VARCHAR ( 255 ) NOT NULL,
	product_description TEXT NOT NULL,
	in_stock INT NOT NULL,
	price FLOAT NOT NULL,
	slug VARCHAR ( 45 ),
	category_id INT NOT NULL,
	FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
);

CREATE TABLE users (
	user_id serial PRIMARY KEY,
	email VARCHAR ( 255 ) NOT NULL,
	password VARCHAR ( 255 ) NOT NULL,
	first_name VARCHAR ( 255 ) NOT NULL,
	last_name VARCHAR ( 255 ) NOT NULL,
	middle_name VARCHAR ( 255 ) NOT NULL,
	is_staff BOOLEAN NOT NULL,
	country VARCHAR ( 255 ) NOT NULL,
	city VARCHAR ( 255 ) NOT NULL,
	address TEXT NOT NULL
);

CREATE TABLE carts (
	cart_id serial PRIMARY KEY,
	user_id INT NOT NULL,
	subtotal DECIMAL NOT NULL,
	total DECIMAL NOT NULL,
	timestamp TIMESTAMP ( 2 ) NOT NULL,
	FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);

CREATE TABLE order_status (
	order_status_id serial PRIMARY KEY,
	status_name VARCHAR ( 255 ) NOT NULL
);

CREATE TABLE orders (
	order_id serial PRIMARY KEY,
	cart_id INT NOT NULL,
	order_status_id INT NOT NULL,
	shipping_total DECIMAL NOT NULL,
	total DECIMAL NOT NULL,
	created_at TIMESTAMP ( 2 ) NOT NULL,
	updated_at TIMESTAMP ( 2 ) NOT NULL,
	FOREIGN KEY (cart_id)
        REFERENCES carts(cart_id),
	FOREIGN KEY (order_status_id)
        REFERENCES order_status(order_status_id)
);

CREATE TABLE cart_product (
	cart_id INT NOT NULL,
	product_id INT NOT NULL,
	PRIMARY KEY  (cart_id, product_id),
	FOREIGN KEY (cart_id)
        REFERENCES carts(cart_id),
	FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

COPY categories
FROM '/usr/src/categories.csv'
DELIMITER ',';

COPY products
FROM '/usr/src/products.csv'
DELIMITER ',';

COPY users
FROM '/usr/src/users.csv'
DELIMITER ',';

COPY carts
FROM '/usr/src/carts.csv'
DELIMITER ',';

COPY order_status
FROM '/usr/src/order_statuses.csv'
DELIMITER ',';

COPY orders
FROM '/usr/src/orders.csv'
DELIMITER ',';

ALTER TABLE cart_product DROP CONSTRAINT cart_product_pkey;
ALTER TABLE cart_product ADD id SERIAL PRIMARY KEY;

COPY cart_product(cart_id, product_id)
FROM '/usr/src/cart_products.csv'
DELIMITER ',';
