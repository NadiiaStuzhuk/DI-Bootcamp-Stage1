-- Part 2: Movie Lookups, Patterns, and Pagination

-- 8. Check if favorite movie exists ('Academy Dinosaur')
SELECT film_id, title, description, length, rental_rate 
FROM film 
WHERE title = 'Academy Dinosaur';

-- 9. Get movies starting with the first two letters ('Ac')
SELECT film_id, title, description, length, rental_rate 
FROM film 
WHERE title LIKE 'Ac%';

-- 10. Find the 10 cheapest movies
SELECT film_id, title, rental_rate 
FROM film 
ORDER BY rental_rate ASC 
LIMIT 10;

-- 11. Find the next 10 cheapest movies (Without LIMIT)
WITH ranked_films AS (
    SELECT film_id, title, rental_rate,
           ROW_NUMBER() OVER (ORDER BY rental_rate ASC, film_id ASC) AS rn
    FROM film
)
SELECT film_id, title, rental_rate
FROM ranked_films
WHERE rn BETWEEN 11 AND 20;