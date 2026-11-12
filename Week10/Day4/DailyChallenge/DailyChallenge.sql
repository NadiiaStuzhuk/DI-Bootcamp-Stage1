-- What You will learn :
-- SQL Basics
-- Table relationships


-- Instructions
-- In this puzzle you have to go through all the SQL queries and provide us the output of the requests before executing them (ie. make an assumption).
-- Then, execute them to make sure you were correct.



-- Queries
-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- )

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)


-- SELECT * FROM SecondTab


-- DATA
-- Table1 – FirstTab
-- ID  Name
-- 5   Pawan
-- 6   Sharlee
-- 7   Krish
-- NULL    Avtaar


-- Table2 – SecondTab
-- ID
-- 5
-- NULL


-- Questions
-- Q1. What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )


-- Q2. What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )


-- Q3. What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )


-- Q4. What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )


-- Submit your Daily Challenge :
-- Don’t forget to push to Github



-- =========================================================================
-- 🧩 SQL Puzzle: FirstTab & SecondTab Combined Script
-- =========================================================================

-- 1. Setup: Create and populate FirstTab
CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5, 'Pawan'),
(6, 'Sharlee'),
(7, 'Krish'),
(NULL, 'Avtaar');


-- 2. Setup: Create and populate SecondTab
CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab VALUES
(5),
(NULL);


-- =========================================================================
-- 📝 Test Queries (Questions Q1 to Q4)
-- =========================================================================

-- Q1. Output will be: 0
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );


-- Q2. Output will be: 2
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );


-- Q3. Output will be: 0
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab );


-- Q4. Output will be: 2
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );