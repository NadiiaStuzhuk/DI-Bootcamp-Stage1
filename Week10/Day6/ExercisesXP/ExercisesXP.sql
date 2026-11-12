-- 👩‍🏫 👩🏿‍🏫 What You’ll learn
-- Relationship between tables
-- Queries


-- How to push your work to Github ?
-- Save the queries into a sql file (.sql extension) and push this file to Github.
-- To save the file into an sql file, click on the “Save” button : the instructions are in the image below
-- save pgadmin file


-- DVD Rental Dataset


-- 🌟 Exercise 1: DVD Rental
-- Instructions
-- Get a list of all the languages, from the language table.

-- Get a list of all films joined with their languages – select the following details : film title, description, and language name.

-- Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.

-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.

-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

-- Delete a film that has a review from the new_film table, what happens to the customer_review table?


-- =========================================================================
-- 🌟 Exercise 1: DVD Rental - Complete Solution Script
-- =========================================================================

-- 1. Get a list of all the languages from the language table
SELECT * 
FROM language;


-- 2. Get a list of all films joined with their languages 
-- (film title, description, and language name)
SELECT f.title, f.description, l.name AS language_name
FROM film f
JOIN language l ON f.language_id = l.language_id;


-- 3. Get all languages, even if there are no films in those languages
-- (film title, description, and language name using LEFT JOIN)
SELECT f.title, f.description, l.name AS language_name
FROM language l
LEFT JOIN film f ON l.language_id = f.language_id;


-- 4. Create a new table called "new_film" and add some new films
CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO new_film (name) VALUES 
('Inception'),
('The Matrix'),
('Interstellar');


-- 5. Create a new table called "customer_review" with a DELETE cascade constraint
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255),
    score INT CHECK (score >= 1 AND score <= 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- 6. Add 2 movie reviews linked to valid objects in the database
-- (Assuming language_id = 1 exists, and new_film IDs 1 and 2 exist)
INSERT INTO customer_review (film_id, language_id, title, score, review_text) VALUES 
(1, 1, 'Mind-blowing!', 10, 'An incredible cinematic experience with complex layers.'),
(2, 1, 'Sci-Fi Masterpiece', 9, 'Groundbreaking visual effects and a timeless story.');


-- 7. Delete a film that has a review from the "new_film" table
-- Explanation: Because we used "ON DELETE CASCADE" in the foreign key constraint,
-- deleting this film will automatically delete its corresponding review from "customer_review".
DELETE FROM new_film 
WHERE id = 1;

-- To verify that the review was automatically deleted, you can run:
SELECT * FROM customer_review;




-- 🌟 Exercise 2 : DVD Rental
-- Instructions
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.


-- =========================================================================
-- 🌟 MASTER SQL SOLUTION: DVD RENTAL EXERCISES & PUZZLES
-- =========================================================================


-- =========================================================================
-- PART A: DVD RENTAL - BASIC QUERIES, FILTERING & JOINS
-- =========================================================================

-- 1. Select all columns from the "customer" table
SELECT * 
FROM customer;

-- 2. Display names (first_name, last_name) using an alias named "full_name"
SELECT first_name || ' ' || last_name AS full_name 
FROM customer;

-- 3. Select all unique create_date from the "customer" table
SELECT DISTINCT create_date 
FROM customer;

-- 4. Get all customer details in descending order by their first name
SELECT * 
FROM customer 
ORDER BY first_name DESC;

-- 5. Get film ID, title, description, year of release, and rental rate in ascending order
SELECT film_id, title, description, release_year, rental_rate 
FROM film 
ORDER BY rental_rate ASC;

-- 6. Get the address and phone number of all customers living in the Texas district
SELECT address, phone 
FROM address 
WHERE district = 'Texas';

-- 7. Retrieve all movie details where the movie ID is either 15 or 150
SELECT * 
FROM film 
WHERE film_id IN (15, 150);

-- 8. Check if your favorite movie exists in the database ('Academy Dinosaur')
SELECT film_id, title, description, length, rental_rate 
FROM film 
WHERE title = 'Academy Dinosaur';

-- 9. Get details of all movies starting with the first two letters of your favorite movie ('Ac')
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

-- 12. Join customer and payment tables to get names, amount, and payment date
SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;

-- 13. Get all movies which are not in inventory
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

-- 15. Bonus: Customer details and payments ordered by staff member ID
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY p.staff_id ASC;


-- =========================================================================
-- PART B: SQL NULL & NOT IN PUZZLE (FirstTab & SecondTab)
-- =========================================================================

-- Setup tables
CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5, 'Pawan'),
(6, 'Sharlee'),
(7, 'Krish'),
(NULL, 'Avtaar');

CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab VALUES
(5),
(NULL);

-- Puzzle test queries
-- Q1 (Output: 
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );