# Week 5 - Customers App

The full code for the Customers (online store) CodeIgniter project is provided. 

You will need to update the .env file with all your database settings.

You can import records into the database using the following SQL insert statements:

```sql
INSERT INTO customers (name, email) VALUES
  ('Raj Patel', 'raj@example.com'),
  ('Wei Chen', 'wei@example.com'),
  ('Emma Müller', 'emma@example.com'),
  ('Priya Gupta', 'priya@example.com'),
  ('Liam Smith', 'liam@example.com');

INSERT INTO orders (customer_id, order_date, total_amount) VALUES
  (1, '2023-04-01', 100.00),
  (2, '2023-04-05', 80.50),
  (3, '2023-04-10', 120.25),
  (4, '2023-04-15', 90.75),
  (1, '2023-04-20', 60.00),
  (5, '2023-04-25', 110.00),
  (2, '2023-04-30', 95.50);

```

A challenge for you is to write a seeder script. Lab 3 has an example seeder script.