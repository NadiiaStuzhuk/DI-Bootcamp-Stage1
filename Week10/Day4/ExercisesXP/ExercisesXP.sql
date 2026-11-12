-- 1. All items, ordered by price (lowest to highest)
SELECT * 
FROM items 
ORDER BY price ASC;

-- 2. Items with a price above 80 (80 included), ordered by price (highest to lowest)
SELECT * 
FROM items 
WHERE price >= 80 
ORDER BY price DESC;

-- 3. The first 3 customers in alphabetical order of the first name (A-Z) – excluding the primary key
SELECT first_name, last_name 
FROM customers 
ORDER BY first_name ASC 
LIMIT 3;

-- 4. All last names (no other columns!), in reverse alphabetical order (Z-A)
SELECT last_name 
FROM customers 
ORDER BY last_name DESC;

-- =========================================================================
-- 🌟 Exercise 2: dvdrental database - Complete Combined Solution
-- =========================================================================

-- 1. Select all columns from the “customer” table
SELECT * 
FROM customer;

-- 2. Display names (first_name, last_name) using an alias named “full_name”
SELECT first_name || ' ' || last_name AS full_name 
FROM customer;

-- 3. Select all the create_date from the “customer” table (no duplicates)
SELECT DISTINCT create_date 
FROM customer;

-- 4. Get all the customer details in descending order by their first name
SELECT * 
FROM customer 
ORDER BY first_name DESC;

-- 5. Get film ID, title, description, year of release, and rental rate in ascending order by rental rate
SELECT film_id, title, description, release_year, rental_rate 
FROM film 
ORDER BY rental_rate ASC;

-- 6. Get the address and phone number of all customers living in the Texas district
SELECT address, phone 
FROM address 
WHERE district = 'Texas';

-- 7. Retrieve all movie details where the movie id is either 15 or 150
SELECT * 
FROM film 
WHERE film_id IN (15, 150);

-- 8. Check if your favorite movie exists in the database (e.g., 'Academy Dinosaur')
SELECT film_id, title, description, length, rental_rate 
FROM film 
WHERE title = 'Academy Dinosaur';

-- 9. Get details of all movies starting with the two first letters of your favorite movie ('Ac')
SELECT film_id, title, description, length, rental_rate 
FROM film 
WHERE title LIKE 'Ac%';

-- 10. Find the 10 cheapest movies
SELECT film_id, title, rental_rate 
FROM film 
ORDER BY rental_rate ASC 
LIMIT 10;

-- 11. Find the next 10 cheapest movies (Bonus: Without using LIMIT)
WITH ranked_films AS (
    SELECT film_id, title, rental_rate,
           ROW_NUMBER() OVER (ORDER BY rental_rate ASC, film_id ASC) AS rn
    FROM film
)
SELECT film_id, title, rental_rate
FROM ranked_films
WHERE rn BETWEEN 11 AND 20;

-- 12. Join customer and payment tables to get customer names, payment amount, and date, ordered by customer ID
SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;

-- 13. Check your inventory: Get all movies which are not in inventory
SELECT film_id, title 
FROM film 
WHERE film_id NOT IN (
    SELECT DISTINCT film_id 
    FROM inventory
);

-- 14. Find which city is in which country
SELECT ci.city, co.country
FROM city ci
JOIN country co ON ci.country_id = co.country_id;

-- 15. Bonus: Get customer's ID, names, amount, and payment date ordered by the staff member ID
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY p.staff_id ASC;