-- Introduction
-- Embark on a detailed exploration of the film industry with this SQL-based data analysis challenge using a comprehensive movies database. These exercises will leverage advanced SQL window functions and common table expressions (CTEs) to uncover insights into movie rankings, revenue, budget trends, and cast and crew performance. Prepare to deepen your understanding of SQL techniques through real-world applications in the context of the movie industry.



-- 👩‍🏫 👩🏿‍🏫 What You’ll learn
-- Through this series of exercises, you will enhance your SQL skills and gain valuable insights into data manipulation and analysis in the entertainment sector. Here’s what we will cover:

-- Advanced Window Functions: Learn to apply window functions like RANK(), NTILE(), and SUM() to perform complex rankings, segmentations, and cumulative calculations.
-- Insights into Movie Industry Trends: Analyze trends in movie popularity, revenue distribution, and budget allocations across different genres and production companies.
-- Performance Evaluation of Cast and Crew: Evaluate the performance of actors and directors based on various metrics such as movie appearances, average ratings, and budget management.
-- Real-World SQL Applications: Gain hands-on experience with practical SQL applications that reflect scenarios encountered by data analysts in the film industry.
-- Analytical Thinking and Problem Solxing: Develop your analytical thinking by tackling tasks that require careful consideration of both the data available and the SQL techniques suitable for extracting meaningful insights.
-- By the end of these exercises, you will have not only advanced your technical skills but also acquired a deeper understanding of the dynamics within the film industry.



-- 🌟 Exercise 1: Movie Rankings and Analysis


-- SQL Dataset we will be using

-- Movies Database


-- Task 1: Rank Movies by Popularity within Each Genre

-- Use the RANK() function to rank movies by their popularity within each genre. Display the genre name, movie title, and their rank based on popularity.



-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company

-- Use the NTILE() function to divide the movies produced by each production company into quartiles based on revenue. Display the company name, movie title, revenue, and quartile.



-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre

-- Use the SUM() function with the ROWS frame specification to calculate the running total of movie budgets within each genre. Display the genre name, movie title, budget, and running total budget.



-- Task 4: Identify the Most Recent Movie for Each Genre

-- Use the FIRST_VALUE() function to find the most recent movie within each genre based on the release date. Display the genre name, movie title, and release date.

SELECT g.genre_name, 
       m.title, 
       m.popularity,
       RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS popularity_rank
FROM movies m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genres g ON mg.genre_id = g.genre_id;

WITH company_quartiles AS (
    SELECT pc.company_name, 
           m.title, 
           m.revenue,
           NTILE(4) OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS revenue_quartile
    FROM movies m
    JOIN movie_companies mc ON m.movie_id = mc.movie_id
    JOIN production_companies pc ON mc.company_id = pc.company_id
)
SELECT company_name, 
       title, 
       revenue, 
       revenue_quartile
FROM company_quartiles
WHERE revenue_quartile = 1; -- Represents the top quartile (top 25% by revenue)

SELECT g.genre_name, 
       m.title, 
       m.budget,
       SUM(m.budget) OVER (
           PARTITION BY g.genre_name 
           ORDER BY m.release_date 
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total_budget
FROM movies m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genres g ON mg.genre_id = g.genre_id;

WITH ranked_movies AS (
    SELECT g.genre_name, 
           m.title, 
           m.release_date,
           FIRST_VALUE(m.title) OVER (
               PARTITION BY g.genre_name 
               ORDER BY m.release_date DESC
           ) AS most_recent_title,
           FIRST_VALUE(m.release_date) OVER (
               PARTITION BY g.genre_name 
               ORDER BY m.release_date DESC
           ) AS most_recent_date
    FROM movies m
    JOIN movie_genres mg ON m.movie_id = mg.movie_id
    JOIN genres g ON mg.genre_id = g.genre_id
)
SELECT DISTINCT genre_name, 
       most_recent_title AS movie_title, 
       most_recent_date AS release_date
FROM ranked_movies;







-- 🌟 Exercise 2: Cast and Crew Performance Analysis


-- Task 1: Rank Actors by Their Appearance in Movies

-- Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in. Display the actor’s name and their rank.



-- Task 2: Identify the Top Director by Average Movie Rating

-- Use a CTE and the RANK() function to find the director with the highest average movie rating. Display the director’s name and their average rating.



-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor

-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor. Display the actor’s name and the cumulative revenue.



-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget

-- Use a CTE and a window function to find the director whose movies have the highest total budget. Display the director’s name and the total budget.




SELECT actor_name, 
       COUNT(movie_id) AS movie_appearances,
       DENSE_RANK() OVER (ORDER BY COUNT(movie_id) DESC) AS actor_rank
FROM movie_cast
GROUP BY actor_name;

WITH director_ratings AS (
    SELECT director_name, 
           AVG(rating) AS avg_rating,
           RANK() OVER (ORDER BY AVG(rating) DESC) AS rating_rank
    FROM movie_directors
    GROUP BY director_name
)
SELECT director_name, 
       avg_rating
FROM director_ratings
WHERE rating_rank = 1;

SELECT actor_name, 
       title AS movie_title, 
       revenue,
       SUM(revenue) OVER (
           PARTITION BY actor_name 
           ORDER BY release_date 
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS cumulative_revenue
FROM movie_cast_details; -- Assumes a joined view or table containing actor_name, title, revenue, and release_date

WITH director_budgets AS (
    SELECT md.director_name, 
           SUM(m.budget) AS total_budget,
           RANK() OVER (ORDER BY SUM(m.budget) DESC) AS budget_rank
    FROM movie_directors md
    JOIN movies m ON md.movie_id = m.movie_id
    GROUP BY md.director_name
)
SELECT director_name, 
       total_budget
FROM director_budgets
WHERE budget_rank = 1;

