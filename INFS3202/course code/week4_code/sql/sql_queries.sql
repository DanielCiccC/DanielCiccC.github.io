SELECT * FROM customers;
SELECT name, email FROM customers;
SELECT * FROM customers WHERE id = 3;
SELECT * FROM customers WHERE email LIKE '%Chen%';
SELECT COUNT(name) FROM customers WHERE name LIKE '%P%';
SELECT * FROM customers WHERE email LIKE '%example.com';

SELECT o.id AS order_id, o.order_date, o.total_amount, c.name, c.email FROM orders o JOIN customers c ON o.customer_id = c.id; 

SELECT o.id AS order_id, o.order_date, o.total_amount, c.name, c.email
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE c.id = 2;

