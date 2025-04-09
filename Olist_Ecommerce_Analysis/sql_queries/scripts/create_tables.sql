CREATE TABLE orders (
order_id VARCHAR(50) PRIMARY KEY,
customer_id VARCHAR(50),
order_status VARCHAR(20),
order_purchase_timestamp DATETIME,
order_approved_at DATETIME NULL,
order_delivered_carrier_date DATETIME NULL,
order_delivered_customer_date DATETIME NULL,
order_estimated_delivery_date DATETIME
);

CREATE TABLE order_items (
order_id VARCHAR(50),
order_item_id INT,
product_id VARCHAR(50),
seller_id VARCHAR(50),
shipping_limit_date DATETIME,
price FLOAT,
freight_value FLOAT,
PRIMARY KEY (order_id, order_item_id)
);

CREATE TABLE customers (
customer_id VARCHAR(50) PRIMARY KEY,
customer_unique_id VARCHAR(50),
customer_zip_code_prefix INT,
customer_city VARCHAR(50),
customer_state VARCHAR(50)
);

CREATE TABLE products (
product_id VARCHAR(50) PRIMARY KEY,
product_category_name VARCHAR(50),
product_name_lenght FLOAT,
product_description_lenght FLOAT,
product_photos_qty FLOAT,
product_weight_g FLOAT,
product_length_cm FLOAT,
product_height_cm FLOAT,
product_width_cm FLOAT,
);

CREATE TABLE sellers (
seller_id VARCHAR(50) PRIMARY KEY,
seller_zip_code_prefix INT,
seller_city VARCHAR(50),
seller_state VARCHAR(50)
);

CREATE TABLE payments (
order_id VARCHAR(50) PRIMARY KEY,
payment_sequential  INT,
payment_type VARCHAR(50),
payment_installments INT,
payment_value FLOAT
);

CREATE TABLE geolocation (
geolocation_zip_code_prefix INT,
geolocation_lat FLOAT,
geolocation_lng FLOAT,
geolocation_city VARCHAR(50),
geolocation_state VARCHAR(50)
);