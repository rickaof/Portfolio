-- Criação de índices

-- Índice em orders.order_id.
CREATE UNIQUE INDEX idx_orders_order_id ON orders(order_id);

-- Índice em customers.customer_id.
CREATE UNIQUE INDEX idx_customers_customer_id ON customers(customer_id);

-- Índice em order_items.products_id, seller_id, product_id
CREATE UNIQUE INDEX idx_order_items_product_id ON order_items(product_id);
CREATE UNIQUE INDEX idx_order_items_seller_id ON order_items(seller_id);
CREATE UNIQUE INDEX idx_order_items_order_id ON order_items(order_id);

-- Criação de Chaves Estrangeiras

-- orders.customer_id, customers.customer_id
ALTER TABLE orders
ADD CONSTRAINT fk_orders_customers
FOREIGN KEY (customer_id) REFERENCES customers(customer_id);

-- order_items.order_id, orders.order_id
ALTER TABLE order_items
ADD CONSTRAINT fk_orderitems_orders
FOREIGN KEY (order_id) REFERENCES orders(order_id);

-- order_items.product_id, products.product_id
ALTER TABLE order_items
ADD CONSTRAINT fk_orderitems_products
FOREIGN KEY (product_id) REFERENCES products(product_id);

-- order_items.seller_id, sellers_seller_id
ALTER TABLE order_items
ADD CONSTRAINT fk_orderitems_sellers
FOREIGN KEY (seller_id) REFERENCES sellers(seller_id);

-- Validação com JOIN

SELECT TOP 10 o.order_id, c.customer_state
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;

SELECT TOP 10 oi.order_id, o.order_id, product_id, seller_id
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id;