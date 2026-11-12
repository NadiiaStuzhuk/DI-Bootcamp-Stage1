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