-- Part 3: Joins, Inventory, Geography, and Bonus Queries

-- 12. Join customer and payment tables
SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;

-- 13. Get all movies not in inventory
SELECT film_id, title 
FROM film 
WHERE film_id NOT IN (SELECT DISTINCT film_id FROM inventory);

-- 14. Find which city is in which country
SELECT ci.city, co.country
FROM city ci
JOIN country co ON ci.country_id = co.country_id;

-- 15. Bonus: Customer details ordered by staff ID
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY p.staff_id ASC;