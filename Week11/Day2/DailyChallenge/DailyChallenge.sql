-- Introduction
-- Join today’s daily challenge to sharpen your SQL skills through a series of exercises based on the Olympic Games dataset. This challenge will test your proficiency with advanced SQL concepts such as subqueries and temporary tables. Dive deep into the data to explore diverse aspects of Olympic history and competitor performance.



-- 👩‍🏫 👩🏿‍🏫 What You’ll learn
-- This challenge is designed to enhance your SQL capabilities by focusing on advanced data exploration techniques. Here’s what you can expect to learn:

-- Complex Query Building: Develop your ability to construct and execute complex queries that require deep analysis and manipulation of data.
-- Subqueries and Temporary Tables: Gain practical experience using subqueries and temporary tables to solve specific problems, a skill essential for handling real-world data challenges.
-- Analytical Precision: Improve your precision in data analysis by focusing on detailed data extraction and manipulation tasks.
-- Cross-Season Analysis: Learn to perform cross-season analysis to identify competitors who excel across different Olympic seasons.
-- Regional Performance Evaluation: Explore how different regions perform by analyzing the concentration of medals and participation in the Olympics.
-- By tackling these exercises, you will not only advance your SQL skills but also develop a keen understanding of how to approach complex data scenarios effectively.


-- 🌟 Exercise 1: Detailed Medal Analysis


-- SQL Dataset we will be using
-- Olympic Data
-- Task 1: Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics. Create a temporary table to store these competitors and their medal counts for each season, and then display the contents of this table.

-- Task 2: Create a temporary table to store competitors who have won medals in exactly two different sports, and then use a subquery to identify the top 3 competitors with the highest total number of medals across all sports. Display the contents of this table.

CREATE TEMP TABLE temp_summer_winter_medallists AS
SELECT 
    p.id AS person_id,
    p.name AS competitor_name,
    SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) AS summer_medals,
    SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) AS winter_medals
FROM person p
JOIN competitor_event ce ON p.id = ce.person_id
JOIN games g ON ce.games_id = g.id
WHERE ce.medal IS NOT NULL AND ce.medal != 'NA'
GROUP BY p.id, p.name
HAVING SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) > 0;

-- Display the contents of the temporary table
SELECT * FROM temp_summer_winter_medallists;

CREATE TEMP TABLE temp_two_sport_medallists AS
SELECT 
    p.id AS person_id,
    p.name AS competitor_name,
    COUNT(DISTINCT s.id) AS sports_count,
    COUNT(ce.medal) AS total_medals
FROM person p
JOIN competitor_event ce ON p.id = ce.person_id
JOIN event e ON ce.event_id = e.id
JOIN sport s ON e.sport_id = s.id
WHERE ce.medal IS NOT NULL AND ce.medal != 'NA'
GROUP BY p.id, p.name
HAVING COUNT(DISTINCT s.id) = 2;

-- Display contents and find top 3 competitors with highest total medals using a subquery
SELECT * 
FROM temp_two_sport_medallists
WHERE total_medals IN (
    SELECT DISTINCT total_medals 
    FROM temp_two_sport_medallists 
    ORDER BY total_medals DESC 
    LIMIT 3
)
ORDER BY total_medals DESC;







-- 🌟 Exercise 2: Region and Competitor Performance
-- Task 1: Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event. Use a subquery to determine the event with the highest number of medals for each competitor, and then display the top 5 regions with the highest total medals.

-- Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any medals. Retrieve and display the contents of this table, including their full names and the number of games they participated in.



SELECT 
    r.region_name,
    COUNT(ce.medal) AS total_region_medals
FROM person_region r
JOIN competitor_event ce ON r.person_id = ce.person_id
WHERE ce.medal IS NOT NULL AND ce.medal != 'NA'
  AND ce.event_id IN (
      SELECT event_id
      FROM (
          SELECT person_id, event_id, COUNT(medal) AS event_medals,
                 ROW_NUMBER() OVER (PARTITION BY person_id ORDER BY COUNT(medal) DESC) as rn
          FROM competitor_event
          WHERE medal IS NOT NULL AND medal != 'NA'
          GROUP BY person_id, event_id
      ) top_events
      WHERE top_events.rn = 1
  )
GROUP BY r.region_name
ORDER BY total_region_medals DESC
LIMIT 5;

CREATE TEMP TABLE temp_no_medal_frequent_participants AS
SELECT 
    p.id AS person_id,
    p.name AS full_name,
    COUNT(DISTINCT ce.games_id) AS games_participated
FROM person p
JOIN competitor_event ce ON p.id = ce.person_id
GROUP BY p.id, p.name
HAVING COUNT(DISTINCT ce.games_id) > 3
   AND SUM(CASE WHEN ce.medal IS NOT NULL AND ce.medal != 'NA' THEN 1 ELSE 0 END) = 0;

-- Retrieve and display contents
SELECT full_name, games_participated 
FROM temp_no_medal_frequent_participants
ORDER BY games_participated DESC;