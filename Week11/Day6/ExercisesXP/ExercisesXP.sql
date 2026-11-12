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


-- Create df_employee table in SQLite by joining tables and formatting dates/columns
CREATE TABLE df_employee AS
SELECT 
    s.employee_id || '_' || SUBSTR(s.date, 7, 4) || '-' || SUBSTR(s.date, 4, 2) || '-' || SUBSTR(s.date, 1, 2) AS id,
    SUBSTR(s.date, 7, 4) || '-' || SUBSTR(s.date, 4, 2) || '-' || SUBSTR(s.date, 1, 2) AS month_year,
    SUBSTR(s.date, 7, 4) || '-' || SUBSTR(s.date, 4, 2) AS pay_month,
    s.employee_id,
    s.employee_name,
    CASE e.[GEN(M_F)]
        WHEN 'M' THEN 'Male'
        WHEN 'F' THEN 'Female'
        ELSE e.[GEN(M_F)]
    END AS gender,
    e.age,
    CAST(REPLACE(s.salary, ',', '.') AS REAL) AS salary,
    f.function_group,
    c.company_name,
    c.company_city,
    c.company_state,
    c.company_type,
    c.const_site_category
FROM salaries s
LEFT JOIN companies c ON s.comp_name = c.company_name
LEFT JOIN functions f ON s.func_code = f.function_code
LEFT JOIN employees e ON s.employee_id = e.employee_code_emp;




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


-- 1. Observe your new table
SELECT * FROM df_employee LIMIT 10;

-- 2. Remove all unwanted spaces from text columns using TRIM
UPDATE df_employee
SET id = TRIM(id),
    employee_id = TRIM(employee_id),
    employee_name = TRIM(employee_name),
    gender = TRIM(gender),
    function_group = TRIM(function_group),
    company_name = TRIM(company_name),
    company_city = TRIM(company_city),
    company_state = TRIM(company_state),
    company_type = TRIM(company_type),
    const_site_category = TRIM(const_site_category);

-- 3. Check for NULL and empty values
SELECT * 
FROM df_employee
WHERE id IS NULL 
   OR month_year IS NULL 
   OR employee_id IS NULL 
   OR salary IS NULL;

-- 4. Delete rows with missing values or HR test salaries (1,000,000)
DELETE FROM df_employee 
WHERE salary IS NULL 
   OR salary = 1000000 
   OR TRIM(const_site_category) = '' 
   OR const_site_category IS NULL;

-- 5. Standardize typos and formatting
UPDATE df_employee SET company_city = 'Goiania' WHERE company_city = 'Goianiaa';
UPDATE df_employee SET company_state = 'Goias' WHERE company_state = 'GOIAS';
UPDATE df_employee SET company_type = 'Construction Site' WHERE company_type = 'Construction Sites';
UPDATE df_employee SET const_site_category = 'Commercial' WHERE const_site_category = 'Commerciall';

-- 6. Remove duplicate rows (keeping the first occurrence per employee per month)
DELETE FROM df_employee
WHERE rowid NOT IN (
    SELECT MIN(rowid)
    FROM df_employee
    GROUP BY pay_month, employee_id
);

-- 🌟 Exercise 3 : Calculating Current Employee Counts by Company
-- How many employees do the companies have today?
-- Group them by company

-- How many employees do the companies have today? (Latest month: 2023-01)
SELECT COUNT(DISTINCT employee_id) AS total_active_employees 
FROM df_employee
WHERE pay_month = (SELECT MAX(pay_month) FROM df_employee);

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

-- 1. What is the total number of employees in each city? Add a percentage column
SELECT company_city, 
       COUNT(DISTINCT employee_id) AS employee_count,
       (CAST(COUNT(DISTINCT employee_id) AS REAL) * 100 / (SELECT COUNT(DISTINCT employee_id) FROM df_employee WHERE pay_month = (SELECT MAX(pay_month) FROM df_employee))) AS percentage
FROM df_employee
WHERE pay_month = (SELECT MAX(pay_month) FROM df_employee)
GROUP BY company_city
ORDER BY employee_count DESC;

-- 2. What is the total number of employees each month?
SELECT pay_month, COUNT(DISTINCT employee_id) AS employee_count 
FROM df_employee
GROUP BY pay_month
ORDER BY pay_month ASC;

-- 3. What is the average number of employees each month?
SELECT AVG(monthly_count) AS avg_employees_per_month
FROM (
    SELECT pay_month, COUNT(DISTINCT employee_id) AS monthly_count
    FROM df_employee
    GROUP BY pay_month
);





-- 🌟 Exercise 5 : Analyzing Employment Trends and Salary Metrics
-- What is the minimum and maximum number of employees throughout all the months? In which months were they?
-- What is the monthly average number of employees by function group?
-- What is the annual average salary?


-- 1. What is the minimum number of employees throughout all the months? In which month was it?
SELECT pay_month, COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY pay_month
ORDER BY employee_count ASC
LIMIT 1;

-- What is the maximum number of employees throughout all the months? In which month was it?
SELECT pay_month, COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY pay_month
ORDER BY employee_count DESC
LIMIT 1;

-- 2. What is the monthly average number of employees by function group?
SELECT function_group, AVG(emp_count) AS avg_employees_per_month
FROM (
    SELECT function_group, pay_month, COUNT(DISTINCT employee_id) AS emp_count
    FROM df_employee
    GROUP BY function_group, pay_month
)
GROUP BY function_group
ORDER BY avg_employees_per_month DESC;

-- 3. What is the annual average salary?
SELECT SUBSTR(pay_month, 1, 4) AS year, ROUND(AVG(salary), 2) AS average_salary
FROM df_employee
GROUP BY SUBSTR(pay_month, 1, 4)
ORDER BY year;