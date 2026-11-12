-- PART 1: Count how many actors are in the table
SELECT COUNT(*) AS total_actors FROM actors;


-- PART 2: Try to add a new actor with some blank fields
-- Example 1: Attempting to insert a record with missing/NULL values
-- (Assuming first_name and last_name have NOT NULL constraints in your schema)
INSERT INTO actors (first_name, last_name, age, number_oscars) 
VALUES ('Brad', NULL, '1963-12-18', 2);

-- Example 2: Omitting a required column entirely
INSERT INTO actors (last_name) 
VALUES ('Pitt');