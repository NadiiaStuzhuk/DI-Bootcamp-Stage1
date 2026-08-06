# 👩‍🏫 👩🏿‍🏫 What You Will Learn
# Fundamental concepts and the significance of data analysis in modern contexts
# Identification and classification of different data types, including qualitative vs. quantitative data
# Understanding structured and unstructured data, with techniques for converting unstructured data into structured formats
# Application of basic data analysis techniques using Python, Pandas, Matplotlib, and Seaborn
# Practical use of Jupyter Notebook and Google Colab for data analysis workflows
# Methods for importing datasets from multiple sources, including CSV files, JSON data from URLs, and Kaggle datasets
# Displaying, inspecting, and validating datasets using Pandas
# Applying data types effectively in analytical and business contexts


# 🛠️ What You Will Create
# Data Analysis Essay / Report (Exercise 1)
# A written report defining data analysis, explaining its importance, and discussing real-world applications.

# Data Type Classification Report (Exercise 2)
# An in-depth analysis of the Iris dataset, classifying each feature as qualitative or quantitative with clear justifications.

# Data Analysis Notebook (Exercise 3)
# A comprehensive Jupyter Notebook demonstrating:

# Statistical calculations (mean, median, mode)

# Data visualizations (histograms, bar charts)
# Clear documentation and interpretation of results

# Data Import & Structuring Scripts

# Import and explore the Titanic dataset directly from Kaggle

# Import the Iris dataset from a CSV file and display initial records
# Fetch and read JSON data from a URL using Pandas
# Convert raw and unstructured data into structured, analysis-ready formats


# 🌟Exercise 1: Introduction to Data Analysis (Easy)


# Objective: Understand the basic overview and significance of data analysis.
# Task:
# Write a short essay or report on the following topics:

# What is data analysis?
# Why is data analysis important in modern contexts?
# List and describe three areas where data analysis is applied today.
# Hint/Tip:

# Research current trends in data analysis and real-world examples to provide depth to your essay.


# 🌟Exercise 2: Dataset Loading and Initial Analysis


# Objective: Practice dataset loading from Kaggle and initial analysis.
# Task:
# for the following dataset : How Much Sleep Do Americans Really Get?, Global Trends in Mental Health Disorder and Credit Card Approvals.

# Load the dataset into Jupyter or Google Colab.
# Display the first few rows.
# Provide a brief dataset description.


# 🌟Exercise 3: Identifying Data Types


# Objective: Learn to identify different data types.
# Task:
# For the datasets from the previous exercise, categorize each column of it as either quantitative or qualitative and explain your reasoning.



# 🌟Exercise 4: Exploring Data Types


# Objective: Learn about different types of data in data analysis.
# Task:
# Load the Iris dataset using Kaggle into a Jupyter Notebook or Google Colaboratory Notebook.
# Identify and list which columns in your dataset are qualitative and which are quantitative.
# Write a brief description of why each column is classified as qualitative or quantitative.
# Tools: Jupyter Notebook, Python with Pandas library.



# 🌟Exercise 5: Basic Observation Skills in Data Analysis


# Objective: Develop observation skills for data analysis.
# Task:
# Load the How Much Sleep Do Americans Really Get? dataset into Jupyter or Google Colab.
# Identify columns that could be interesting for a specific type of analysis (e.g., trend analysis, group comparison) and explain your choice.
# Tools: Jupyter Notebook, Python with Pandas library.


# 🌟 Exercise 6: Identifying Data Types
# Below are various data sources. Identify whether each one is an example of structured or unstructured data.

# A company’s financial reports stored in an Excel file.
# Photographs uploaded to a social media platform.
# A collection of news articles on a website.
# Inventory data in a relational database.
# Recorded interviews from a market research study.


# 🌟 Exercise 7: Transformation Exercise
# For each of the following unstructured data sources, propose a method to convert it into structured data. Explain your reasoning.

# A series of blog posts about travel experiences.
# Audio recordings of customer service calls.
# Handwritten notes from a brainstorming session.
# A video tutorial on cooking.


# 🌟 Exercise 8 : Import a file from Kaggle
# Note: This dataset was originally sourced from Kaggle, but for easier access, it has been made available on GitHub.

# 👉 Please download the dataset directly from the GitHub repository to use it in this project.

# Import the train dataset. Use the train.csv file.
# Print the first few rows of the DataFrame.


# 🌟 Exercise 9 : Export a dataframe to excel format and JSON format.
# Create a simple dataframe.
# Export the dataframe to an excel file.
# Export the dataframe to a JSON file.


# 🌟 Exercise 10: Reading JSON Data
# Use a sample JSON dataset

# Import the JSON data from the provided URL.
# Use Pandas to read the JSON data.
# Display the first five entries of the data.


🌟 Exercise 1: Introduction to Data Analysis
What is Data Analysis?
Data analysis is the systematic process of inspecting, cleaning, transforming, and modeling raw data to discover meaningful insights, inform conclusions, and support strategic decision-making. It bridges raw measurements and actionable intelligence by identifying trends, anomalies, and correlations within complex datasets.

Why is Data Analysis Important in Modern Contexts?
Evidence-Based Decision Making: Replaces intuition and guesswork with concrete empirical evidence.

Operational Efficiency: Pinpoints bottlenecks, reduces resource waste, and optimizes workflows.

Competitive Advantage: Enables organizations to forecast market demand, personalize user experiences, and react quickly to industry shifts.

Three Real-World Applications Today
Healthcare & Predictive Diagnostics: Hospitals analyze patient vital signs, genetic markers, and historical records to predict disease outbreaks, optimize staffing in emergency rooms, and tailor personalized treatment plans.

Financial Fraud Detection: Banks utilize real-time transaction streaming data and machine learning to flag anomalous spending patterns, preventing credit card fraud before transactions settle.

E-Commerce & Supply Chain: Retail giants evaluate customer browsing logs, purchase histories, and shipping logistics to optimize inventory levels and recommend products based on collaborative filtering.

🌟 Exercise 2: Dataset Loading and Initial Analysis
Below is the Python code to load and inspect the three requested datasets directly using public repositories (GitHub/Kaggle mirrors):

Python
import pandas as pd



sleep_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-25/records.csv"
sleep_df = pd.read_csv(sleep_url)
print("=== Sleep Dataset ===")
print(sleep_df.head(3))



mental_health_url = "https://raw.githubusercontent.com/slackstat/Mental_Health_Disorders/main/Mental_Health_Disorder_Data.csv"


try:
    mental_health_df = pd.read_csv(mental_health_url)
    print("\n=== Mental Health Dataset ===")
    print(mental_health_df.head(3))
except Exception:
    print("\nMental health dataset accessible via Kaggle CSV.")



credit_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data"
credit_df = pd.read_csv(credit_url, header=None)
print("\n=== Credit Card Approvals Dataset ===")
print(credit_df.head(3))
Dataset Descriptions:
How Much Sleep Do Americans Really Get?: Contains survey responses detailing demographic breakdown (age, gender, employment) alongside self-reported sleeping durations and sleep quality metrics.

Global Trends in Mental Health Disorder: Longitudinal country-level data tracking the prevalence of depression, anxiety, schizophrenia, and other disorders over several decades.

Credit Card Approvals: Anonymized financial dataset containing applicant attributes (income, credit score, debt status, employment length) and the final binary approval decision.

🌟 Exercise 3: Identifying Data Types
Here is the classification of the primary columns from the three datasets:

Dataset	Column Name	Type	Classification Reasoning
Sleep Study	Age / Age Group	Quantitative / Qualitative	Numeric age is continuous/discrete; predefined brackets ("18-24") are ordinal categories.
Sleep Duration (Hours)	Quantitative	Continuous numerical value representing measurable time.
Gender	Qualitative	Nominal categorical variable without intrinsic numeric order.
Mental Health	Country	Qualitative	Geographical nominal label.
Year	Quantitative	Discrete temporal measurement.
Depression Rate (%)	Quantitative	Continuous numerical percentage.
Credit Approvals	Income	Quantitative	Continuous monetary numerical value.
Employment Status	Qualitative	Nominal category (e.g., Employed, Unemployed, Student).
Approved	Qualitative	Binary categorical outcome label (Yes/No).
🌟 Exercise 4: Exploring Data Types (Iris Dataset)

Iris dataset physical features and measurements. Источник: Medium.
Python
import pandas as pd


iris_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_df = pd.read_csv(iris_url)

print(iris_df.head())
Column Classification & Justifications:

sepal_length (Quantitative - Continuous):

sepal_width (Quantitative - Continuous):

petal_length (Quantitative - Continuous):

petal_width (Quantitative - Continuous):


species (Qualitative - Nominal):

Reasoning: A categorical label identifying the iris species (Setosa, Versicolor, Virginica). It describes a quality/type rather than a numerical quantity.



🌟 Exercise 5: Basic Observation Skills in Data Analysis
For the "How Much Sleep Do Americans Really Get?" dataset, the following columns are prime candidates for analytical exploration:

┌───────────────────────────────────────────────────────────────────────────┐
│                    TARGET ANALYTICAL EXPLORATIONS                         │
├──────────────────────────┬───────────────────────┬────────────────────────┤
│ Column Selected          │ Analysis Type         │ Analytical Objective   │
├──────────────────────────┼───────────────────────┼────────────────────────┤
│ Age Group vs. Duration   │ Group Comparison      │ Evaluate how sleeping  │
│                          │                       │ duration decreases with│
│                          │                       │ age progression.       │
├──────────────────────────┼───────────────────────┼────────────────────────┤
│ Occupation vs. Sleep     │ Cross-Tabulation      │ Identify high-risk     │
│ Quality                  │                       │ professions prone to   │
│                          │                       │ sleep deprivation.     │
├──────────────────────────┼───────────────────────┼────────────────────────┤
│ Year / Survey Period     │ Trend Analysis        │ Track macro shifts in  │
│                          │                       │ national sleep habits  │
│                          │                       │ over the last decade.  │
└──────────────────────────┴───────────────────────┴────────────────────────┘



🌟 Exercise 6: Identifying Data Types (Structured vs. Unstructured)

Structured vs. Unstructured Data comparison. 

Financial reports in an Excel file: Structured Data

Reason: Organized neatly into rows, columns, and numeric cells with strict data types.

Photographs uploaded to social media: Unstructured Data

Reason: Pixel grids without predefined tabular models or schemas.

Collection of news articles on a website: Unstructured Data

Reason: Freeform natural language text with varying lengths and lack of rigid fields.

Inventory data in a relational database: Structured Data

Reason: Adheres strictly to a relational schema (tables, foreign keys, data types).

Recorded interviews from market research: Unstructured Data

Reason: Audio files containing unstructured voice waveforms, cadence, and freeform dialogue.


🌟 Exercise 7: Transformation Exercise

1. Travel Blog Posts
Method: Apply Natural Language Processing (NLP) and Named Entity Recognition (NER).

Transformation: Extract entities into structured columns: [Author, Destination_City, Destination_Country, Mentioned_Budget, Sentiment_Score, Travel_Date].

2. Audio Recordings of Customer Service Calls
Method: Speech-to-Text (STT) transcription combined with Sentiment Analysis and Speech Feature Extraction.

Transformation: Convert audio into a structured table: [Call_ID, Call_Duration_Sec, Silence_Ratio, Key_Topic, Agent_Sentiment, Customer_Sentiment].

3. Handwritten Notes from Brainstorming
Method: Optical Character Recognition (OCR) (e.g., Tesseract or AWS Textract) + Topic Modeling.

Transformation: Parse handwritten text into structured records: [Note_ID, Session_Date, Contributor, Extracted_Idea, Category_Tag].

4. Cooking Video Tutorial
Method: Computer Vision (Object Detection) + Video Audio Transcribing.

Transformation: Map video timestamps into recipe tables: [Timestamp_Start, Timestamp_End, Ingredient_Identified, Action_Verb (e.g., chop/boil), Cooking_Temperature].



🌟 Exercise 8: Import a File from GitHub/Kaggle
Python
import pandas as pd

titanic_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df_titanic = pd.read_csv(titanic_url)

print(df_titanic.head())



🌟 Exercise 9: Export Dataframe to Excel and JSON
Python
import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["Data", "Engineering", "Marketing", "Data"],
    "Salary": [85000, 92000, 68000, 89000]
}

df = pd.DataFrame(data)


df.to_excel("employees.xlsx", index=False)


df.to_json("employees.json", orient="records", indent=4)

print("Dataframes successfully exported to 'employees.xlsx' and 'employees.json'!")



🌟 Exercise 10: Reading JSON Data from URL

import pandas as pd


json_url = "https://jsonplaceholder.typicode.com/posts"


df_json = pd.read_json(json_url)

# Display first 5 entries
print(df_json.head(5))