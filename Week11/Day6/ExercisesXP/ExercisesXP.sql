-- 👩‍🏫 👩🏿‍🏫 What You’ll learn
-- Techniques for data cleaning and transformation using SQL
-- Methods to handle and preprocess data for analysis
-- Steps to ensure data quality and consistency


-- 🛠️ What you will create
-- A cleaned and transformed dataset ready for analysis
-- SQL scripts to automate data cleaning tasks


-- Dataset
-- You will be using this dataset for the following exercises. Please download all of the .csv files : company.csv, employees.csv, functions.csv, and salaries.csv.

-- Before starting your exercises, to work with this dataset, we will have to upload it in SQLiteOnline. As we did for the previous days, go to **https://sqliteonline.com/ > Import > select all of the .csv files**. Then a window of import the file should appear, change from “New-Auto” to “First Line” in Column Name on all of them, and if needed, change the delimiter from “,” to “;”. You have a preview, make sure the cells are well delimited then hit “ok”.
-- You are ready to start !



-- 🌟 Exercise 1: Building a Comprehensive Dataset for Employee Analysis
-- Create a temporary table that join all tables and create a new one using LEFT JOIN.
-- Create an unique identifier code between the columns ‘employee_id’ and ‘date’ and call it ‘id’.
-- Convert the column ‘date’ to DATE type because it was previously configured as TIMESTAMP.
-- Transform this new table into a dataset “df_employee” for analysis.
-- Hint :


-- CREATE TABLE df_employee AS
-- SELECT 
--     employee_id || '_' || CAST(date AS TEXT) AS id,  -- Use || for concatenation and CAST date to TEXT
--     DATE(date) AS month_year,  -- Use DATE() function to cast the timestamp to a DATE format
--     employee_id, 
--     ..., 
--     `...` AS gender,  
--     ...,
--     ...,
--     ..., 
--     ..., 
--     ..., 
--     ..., 
--     ..., 
--     ...
-- FROM emp_dataset;


-- You should get a new df-employee table with the following columns : id, month_year, employee_id, employee_name, gender, age, salary, function_group, company_name, company_city, company_state, company_type, and const_site_category.


-- 1. Create a temporary table joining all tables using LEFT JOIN
SELECT *
INTO emp_dataset
FROM salaries
LEFT JOIN companies ON salaries.comp_name = companies.company_name
LEFT JOIN functions ON salaries.func_code = functions.function_code
LEFT JOIN employees ON salaries.employee_id = employees.employee_code_emp;

-- 2 & 3. Create unique identifier 'id', convert date, and create 'df_employee'
SELECT 
    employee_id || '_' || CAST(date AS TEXT) AS id,  
    DATE(date) AS month_year,  
    employee_id, 
    employee_name, 
    [GEN(M_F)] AS gender,  
    age,
    salary,
    function_group, 
    company_name, 
    company_city, 
    company_state, 
    company_type, 
    const_site_category
INTO df_employee
FROM emp_dataset;

-- Rename column if needed
EXEC sp_rename 'df_employee.[GEN(M_F)]', 'gender', 'COLUMN';





-- 🌟 Exercise 2: Cleaning Data for Consistency and Quality
-- 1. run the following SQLite request and observe your new table.

-- SELECT * FROM df_employee;


-- 2. Remove all unwanted spaces from all text columns using TRIM

-- Hint :

-- UPDATE df_employee
-- SET
-- id = TRIM(id),
-- ...
-- ...;


-- 3. Check for NULL values and empty values.

-- SELECT *
-- FROM df_employee
-- WHERE id IS NULL
-- OR month_year IS NULL
-- OR employee_id IS NULL
-- ...
-- ....;


-- 4. Delete rows of the detected missing values.

-- Hint :

-- DELETE FROM df_employee
-- WHERE salary = ' '
-- ;


-- 1. Create a temporary table joining all tables using LEFT JOIN
SELECT *
INTO emp_dataset
FROM salaries
LEFT JOIN companies ON salaries.comp_name = companies.company_name
LEFT JOIN functions ON salaries.func_code = functions.function_code
LEFT JOIN employees ON salaries.employee_id = employees.employee_code_emp;

-- 2 & 3. Create unique identifier 'id', convert date, and create 'df_employee'
SELECT 
    employee_id || '_' || CAST(date AS TEXT) AS id,  
    DATE(date) AS month_year,  
    employee_id, 
    employee_name, 
    [GEN(M_F)] AS gender,  
    age,
    salary,
    function_group, 
    company_name, 
    company_city, 
    company_state, 
    company_type, 
    const_site_category
INTO df_employee
FROM emp_dataset;

-- Rename column if needed
EXEC sp_rename 'df_employee.[GEN(M_F)]', 'gender', 'COLUMN';


-- 🌟 Exercise 3 : Calculating Current Employee Counts by Company
-- How many employees do the companies have today?
-- Group them by company

SELECT company_name, COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
WHERE pay_month = (SELECT MAX(pay_month) FROM df_employee)
GROUP BY company_name
ORDER BY employee_count DESC;





-- 🌟 Exercise 4 : Analyzing Employee Distribution by City and Over Time
-- What is the total number of employees each city? Add a percentage column
-- What is the total number of employees each month?
-- What is the average number of employees each month?

SELECT company_city, 
       COUNT(DISTINCT employee_id) AS employee_count,
       (CAST(COUNT(DISTINCT employee_id) AS FLOAT) * 100 / SUM(COUNT(DISTINCT employee_id)) OVER ()) AS percentage
FROM df_employee
WHERE pay_month = (SELECT MAX(pay_month) FROM df_employee)
GROUP BY company_city
ORDER BY employee_count DESC;

SELECT pay_month, COUNT(DISTINCT employee_id) AS employee_count 
FROM df_employee
GROUP BY pay_month
ORDER BY pay_month ASC;





-- 🌟 Exercise 5 : Analyzing Employment Trends and Salary Metrics
-- What is the minimum and maximum number of employees throughout all the months? In which months were they?
-- What is the monthly average number of employees by function group?
-- What is the annual average salary?


SELECT function_group, AVG(employee_count) AS avg_employees_per_month
FROM (
    SELECT function_group, pay_month, COUNT(DISTINCT employee_id) AS employee_count
    FROM df_employee
    GROUP BY function_group, pay_month
) t
GROUP BY function_group
ORDER BY avg_employees_per_month DESC;