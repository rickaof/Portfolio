-- ANALISANDO OS 10 ÚLTIMOS CANCELAMENTOS.

SELECT TOP 10
	orders.order_status AS [Status do Pedido],
	customers.customer_unique_id AS [Nome Cliente],
	order_items.product_id AS [Nome do Produto],
	products.product_category_name AS [Categoria do Produto],
	orders.order_purchase_timestamp AS [Data do Pedido]
FROM orders
JOIN customers ON customers.customer_id = orders.customer_id
JOIN order_items ON order_items.order_id = orders.order_id
JOIN products ON order_items.product_id = products.product_id
WHERE orders.order_status = 'canceled'
ORDER BY orders.order_purchase_timestamp DESC;
