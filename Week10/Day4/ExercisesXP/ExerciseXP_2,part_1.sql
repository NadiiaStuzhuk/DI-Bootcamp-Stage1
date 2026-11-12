-- Part 1: Basic Queries, Aliases, Distinct, and Ordering

-- 1. Select all columns from the customer table
SELECT * FROM customer;

-- 2. Display names using an alias named full_name
SELECT first_name || ' ' || last_name AS full_name FROM customer;

-- 3. Select all unique create_date from customer
SELECT DISTINCT create_date FROM customer;

-- 4. Get customer details in descending order by first name
SELECT * FROM customer ORDER BY first_name DESC;

-- 5. Get film details in ascending order by rental rate
SELECT film_id, title, description, release_year, rental_rate 
FROM film 
ORDER BY rental_rate ASC;

-- 6. Address and phone of customers in Texas
SELECT address, phone FROM address WHERE district = 'Texas';

-- 7. Retrieve movie details where film_id is 15 or 150
SELECT * FROM film WHERE film_id IN (15, 150);