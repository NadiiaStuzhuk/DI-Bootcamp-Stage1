-- Daily Challenge : Advanced Movie Data Analysis
-- In these exercises, you will delve into advanced SQL window functions to analyze complex movie data. These tasks are designed to challenge your SQL skills and require a deep understanding of window functions.

-- Here is the database link:

-- Movies Database


-- 🌟 Task 1: Calculate the Average Budget Growth Rate for Each Production Company
-- Calculate the average budget growth rate for each production company across all movies they have produced. Use window functions to determine the budget growth rate and then calculate the average growth rate.



-- 🌟 Task 2: Determine the Most Consistently High-Rated Actor
-- Identify the actor who has appeared in the most movies that are rated above the average rating of all movies. Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.



-- 🌟 Task 3: Calculate the Rolling Average Revenue for Each Genre
-- Calculate the rolling average revenue for movies within each genre, considering only the last three movies released in the genre. Use window functions with the ROWS frame specification to achieve this.



-- 🌟 Task 4: Identify the Highest-Grossing Movie Series
-- Identify the movie series (based on shared keywords) with the highest total revenue. Use window functions and CTEs to group movies by their series and calculate the total revenue.



-- Conclusion
-- By completing this daily challenge, you will have applied advanced SQL window functions to solve complex data analysis problems, enhancing your skills in using LAG(), AVG(), and SUM() with windowing, as well as combining window functions with CTEs to tackle intricate queries.

WITH company_budgets AS (
    SELECT 
        pc.company_id,
        pc.company_name,
        m.movie_id,
        m.title,
        m.release_date,
        m.budget,
        LAG(m.budget) OVER (PARTITION BY pc.company_id ORDER BY m.release_date, m.movie_id) AS prev_budget
    FROM movies.production_company pc
    JOIN movies.movie_company mc ON pc.company_id = mc.company_id
    JOIN movies.movie m ON mc.movie_id = m.movie_id
    WHERE m.budget IS NOT NULL AND m.budget > 0
),
budget_growth AS (
    SELECT 
        company_id,
        company_name,
        movie_id,
        title,
        budget,
        prev_budget,
        CASE 
            WHEN prev_budget IS NULL OR prev_budget = 0 THEN NULL
            ELSE (CAST(budget AS DECIMAL) - prev_budget) / prev_budget 
        END AS growth_rate
    FROM company_budgets
)
SELECT 
    company_id,
    company_name,
    AVG(growth_rate) AS avg_budget_growth_rate
FROM budget_growth
WHERE growth_rate IS NOT NULL
GROUP BY company_id, company_name;

WITH global_avg AS (
    SELECT AVG(vote_average) AS avg_rating
    FROM movies.movie
    WHERE vote_average IS NOT NULL
),
qualified_movies AS (
    SELECT 
        mc.person_id,
        m.movie_id
    FROM movies.movie_cast mc
    JOIN movies.movie m ON mc.movie_id = m.movie_id
    CROSS JOIN global_avg g
    WHERE m.vote_average > g.avg_rating
),
actor_movie_counts AS (
    SELECT 
        qm.person_id,
        p.person_name,
        COUNT(qm.movie_id) AS movies_above_avg_count,
        DENSE_RANK() OVER (ORDER BY COUNT(qm.movie_id) DESC) as rnk
    FROM qualified_movies qm
    JOIN movies.person p ON qm.person_id = p.person_id
    GROUP BY qm.person_id, p.person_name
)
SELECT 
    person_id,
    person_name,
    movies_above_avg_count
FROM actor_movie_counts
WHERE rnk = 1;

WITH genre_movies AS (
    SELECT 
        g.genre_id,
        g.genre_name,
        m.movie_id,
        m.title,
        m.release_date,
        m.revenue
    FROM movies.genre g
    JOIN movies.movie_genre mg ON g.genre_id = mg.genre_id
    JOIN movies.movie m ON mg.movie_id = m.movie_id
    WHERE m.revenue IS NOT NULL
)
SELECT 
    genre_id,
    genre_name,
    movie_id,
    title,
    release_date,
    revenue,
    AVG(CAST(revenue AS DECIMAL)) OVER (
        PARTITION BY genre_id 
        ORDER BY release_date, movie_id
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_revenue
FROM genre_movies;

WITH keyword_revenue AS (
    SELECT 
        k.keyword_id,
        k.keyword_name,
        SUM(m.revenue) AS total_series_revenue,
        COUNT(m.movie_id) AS movie_count,
        DENSE_RANK() OVER (ORDER BY SUM(m.revenue) DESC) as revenue_rank
    FROM movies.keyword k
    JOIN movies.movie_keyword mk ON k.keyword_id = mk.keyword_id
    JOIN movies.movie m ON mk.movie_id = m.movie_id
    WHERE m.revenue IS NOT NULL
    GROUP BY k.keyword_id, k.keyword_name
)
SELECT 
    keyword_id,
    keyword_name,
    total_series_revenue,
    movie_count
FROM keyword_revenue
WHERE revenue_rank = 1;

