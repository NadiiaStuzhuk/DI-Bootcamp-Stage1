-- Exercise XP: Advanced Olympic Data Analysis


-- Introduction
-- Dive into the intricacies of the Olympic Games dataset through a series of sophisticated SQL challenges designed to stretch your understanding of database management and data analysis. This set of exercises will involve complex queries, temporary tables, and a deep dive into subqueries to uncover insights into Olympic competitors, medals, and events.



-- 👩‍🏫 👩🏿‍🏫 What You’ll learn
-- In this session, you will enhance your SQL skills with hands-on applications on a real-world dataset. Here’s what you can expect to master:

-- Complex Query Formulation: Learn to construct and execute complex SQL subqueries and understand their use in real-world data analysis.
-- Data Manipulation Techniques: Develop advanced data manipulation skills including updating, inserting, and deleting records using subqueries within SQL commands.
-- Analytical Thinking: Improve your analytical thinking by solving problems that require deep analysis of nested data and relationships within a large dataset.
-- Optimization of SQL Queries: Gain experience in optimizing SQL queries to improve efficiency and performance, particularly in large-scale data environments.
-- Collaborative Problem Solving: Engage with scenarios that simulate real-life data management tasks, enhancing both your technical skills and your ability to think critically about data.
-- By the end of these exercises, you will be equipped with a robust set of skills to handle complex SQL queries and data analysis challenges, preparing you for advanced roles in data management and analytics.



-- Set up the database
-- To do the following exercises, you can use pgAdmin4 but I recommend using sqliteonline which is very intuitive.

-- If you are working on pgadmin, here how to download the file :
-- 1. Go to pgadmin and create a new database. Click on it.
-- 2. Download all of the .sql files.
-- 3. Go to the downloaded sql files and select them all at once. Then slide them in your database in pgadmin.

-- For those using sqliteonline you can find the sqlite dataset here.

-- How to import the database on sqliteonline :

-- Go to this github link and download on github olympics.db
-- Go to sqliteonline, click on the “+” on the left corner and select “Open SQLite DB”
-- Select the olympics.db you just downloaded.
-- Thats all, you should be able to see your tables in the left windowns like so :


-- Screenshot 2024-12-29 at 2 06 32 pm


-- 🌟 Exercise 1: Complex Subquery Analysis


-- SQL Dataset we will be using
-- Olympic Data

-- Task 1: Find the average age of competitors who have won at least one medal, grouped by the type of medal they won. Use a correlated subquery to achieve this.

-- Task 2: Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 different events. Use nested subqueries to filter and aggregate the data.

-- Task 3: Create a temporary table to store the total number of medals won by each competitor and filter to show only those who have won more than 2 medals. Use subqueries to aggregate the data.

-- Task 4: Use a subquery within a DELETE statement to remove records of competitors who have not won any medals from a temporary table created for analysis.



-- A visualization of the DB to help us navigate it



-- Olympics DB Visualization


SELECT 
    ce.medal,
    (
        SELECT AVG(p.age) 
        FROM person p 
        JOIN competitor_event ce2 ON p.id = ce2.person_id 
        WHERE ce2.medal = ce.medal 
          AND ce2.medal IS NOT NULL 
          AND ce2.medal != 'NA'
    ) AS avg_age
FROM (
    SELECT DISTINCT medal 
    FROM competitor_event 
    WHERE medal IS NOT NULL AND medal != 'NA'
) ce;

SELECT 
    r.region_name,
    COUNT(DISTINCT c.person_id) AS unique_competitors
FROM person_region r
JOIN competitor c ON r.person_id = c.person_id
WHERE c.person_id IN (
    SELECT person_id
    FROM (
        SELECT person_id, COUNT(DISTINCT event_id) AS event_count
        FROM competitor_event
        GROUP BY person_id
        HAVING COUNT(DISTINCT event_id) > 3
    ) sub
)
GROUP BY r.region_name
ORDER BY unique_competitors DESC
LIMIT 5;

CREATE TEMP TABLE temp_competitor_medals AS
SELECT 
    person_id,
    (
        SELECT COUNT(*) 
        FROM competitor_event ce 
        WHERE ce.person_id = p.person_id 
          AND ce.medal IS NOT NULL 
          AND ce.medal != 'NA'
    ) AS total_medals
FROM (SELECT DISTINCT person_id FROM competitor_event) p
WHERE (
    SELECT COUNT(*) 
    FROM competitor_event ce 
    WHERE ce.person_id = p.person_id 
      AND ce.medal IS NOT NULL 
      AND ce.medal != 'NA'
) > 2;

DELETE FROM temp_competitor_medals
WHERE person_id NOT IN (
    SELECT DISTINCT person_id 
    FROM competitor_event 
    WHERE medal IS NOT NULL AND medal != 'NA'
);







-- 🌟 Exercise 2: Advanced Data Manipulation and Optimization
-- Task 1: Update the heights of competitors based on the average height of competitors from the same region. Use a correlated subquery within the UPDATE statement.

-- Task 2: Insert new records into a temporary table for competitors who participated in more than one event in the same games and list their total number of events participated. Use nested subqueries for filtering.

-- Task 3: Identify regions where the average number of medals won per competitor is greater than the overall average. Use subqueries to calculate and compare averages.

-- Task 4: Create a temporary table to track competitors’ participation across different seasons and identify those who have participated in both Summer and Winter games.


UPDATE person p
SET height = (
    SELECT AVG(p2.height)
    FROM person p2
    JOIN person_region pr2 ON p2.id = pr2.person_id
    JOIN person_region pr ON p.id = pr.person_id
    WHERE pr2.region_id = pr.region_id 
      AND p2.height IS NOT NULL
)
WHERE height IS NULL;

CREATE TEMP TABLE temp_multi_event_games AS
SELECT 
    person_id,
    games_id,
    (
        SELECT COUNT(DISTINCT event_id) 
        FROM competitor_event ce2 
        WHERE ce2.person_id = ce.person_id 
          AND ce2.games_id = ce.games_id
    ) AS total_events
FROM competitor_event ce
GROUP BY person_id, games_id
HAVING COUNT(DISTINCT event_id) > 1;

SELECT 
    pr.region_name,
    AVG(medal_count.medals) AS avg_medals_per_competitor
FROM person_region pr
JOIN (
    SELECT person_id, COUNT(*) AS medals
    FROM competitor_event
    WHERE medal IS NOT NULL AND medal != 'NA'
    GROUP BY person_id
) medal_count ON pr.person_id = medal_count.person_id
GROUP BY pr.region_name
HAVING AVG(medal_count.medals) > (
    SELECT AVG(total_medals)
    FROM (
        SELECT COUNT(*) AS total_medals
        FROM competitor_event
        WHERE medal IS NOT NULL AND medal != 'NA'
        GROUP BY person_id
    ) overall_avg
);

CREATE TEMP TABLE temp_seasonal_competitors AS
SELECT DISTINCT person_id
FROM competitor_event ce
JOIN games g ON ce.games_id = g.id
WHERE g.season = 'Summer'
  AND person_id IN (
      SELECT DISTINCT person_id
      FROM competitor_event ce2
      JOIN games g2 ON ce2.games_id = g2.id
      WHERE g2.season = 'Winter'
  );