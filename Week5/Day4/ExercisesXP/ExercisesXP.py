# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# The importance of data visualization in data analysis.
# How to use Python libraries such as Matplotlib and Seaborn for creating effective visualizations.
# Choosing the right graph for different data types and purposes.
# Hands-on experience with creating and customizing various types of plots.


# 🛠️ What you will create
# Line plots for time-series data.
# Bar charts for category-wise comparisons.
# Histograms for distribution analysis.
# Scatter plots for identifying relationships between variables.


# 🌟 Exercise 1: Understanding Data Visualization
# Task: Explain why data visualization is important in data analysis.
# Task: Describe the purpose of a line graph in data visualization.

Task 1: Why is data visualization important in data analysis?
Data visualization is crucial because human brains process visual information significantly faster and more effectively than raw numbers or text tables. Its primary benefits include:

Rapid Trend Identification: Allows analysts to spot patterns, seasonal trends, and correlations across thousands of data points at a glance.

Anomaly Detection: Makes outliers, missing data, and unusual spikes immediately noticeable.

Effective Storytelling & Communication: Simplifies complex statistical findings into intuitive visual formats that non-technical stakeholders can easily understand.

Task 2: What is the purpose of a line graph in data visualization?
The primary purpose of a line graph is to track changes, trends, and continuous metrics over a sequential interval, most commonly time (e.g., time-series data like stock prices, monthly revenues, or daily temperatures). By connecting individual data points with continuous line segments, line graphs effectively demonstrate direction (growth or decline), rate of change, and cyclical patterns over time.



# 🌟 Exercise 2: Creating a Line Plot for Temperature Variation
# Objective: Create a simple line plot using Matplotlib that represents temperature variations over a week.
# Tasks:
# Use a list of temperature values for each day of the week (e.g., [72, 74, 76, 80, 82, 78, 75]).
# Label the x-axis as “Day” and the y-axis as “Temperature (°F)”.
# Add a title to the plot.
# Display the plot.

import matplotlib.pyplot as plt


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [72, 74, 76, 80, 82, 78, 75]


plt.figure(figsize=(8, 5))
plt.plot(days, temperatures, marker='o', color='crimson', linewidth=2, linestyle='-')


plt.xlabel('Day', fontsize=12)
plt.ylabel('Temperature (°F)', fontsize=12)
plt.title('Weekly Temperature Variation', fontsize=14, fontweight='bold')


plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


# 🌟 Exercise 3: Visualizing Monthly Sales with a Bar Chart
# Objective: Generate a bar chart using Matplotlib to visualize monthly sales data for a retail store.
# Tasks:
# Create a list of sales values for each month (e.g., [5000, 5500, 6200, 7000, 7500]).
# Label the x-axis as “Month” and the y-axis as “Sales Amount ($)”.
# Add a title to the bar chart.
# Display the plot.

import matplotlib.pyplot as plt


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [5000, 5500, 6200, 7000, 7500]


plt.figure(figsize=(8, 5))
plt.bar(months, sales, color='royalblue', edgecolor='black', width=0.6)


plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales Amount ($)', fontsize=12)
plt.title('Monthly Sales Revenue', fontsize=14, fontweight='bold')


for i, v in enumerate(sales):
    plt.text(i, v + 100, f"${v:,}", ha='center', fontweight='bold')


plt.tight_layout()
plt.show()

# For exercises 4,5,6, you need to download this dataset:
# Student Mental health

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")


df = pd.read_csv("Student Mental health.csv")


# 🌟 Exercise 4: Visualizing the Distribution of CGPA
# Objective: Create a histogram to visualize the distribution of students’ CGPA.
# Dataset Overview: Assume the CGPA data is categorized into ranges and loaded in a DataFrame named df.
# Tasks:
# Import necessary libraries.
# Use Seaborn’s histplot to create a histogram of the CGPA categories.
# Customize the histogram with a specific color and add a title.
# Display the plot.

import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(10, 6))


sns.histplot(
    data=df,
    x="What is your CGPA?",
    color="teal",
    shrink=0.8, 
)


plt.title("Distribution of Students' CGPA", fontsize=14, fontweight="bold")
plt.xlabel("CGPA Range", fontsize=12)
plt.ylabel("Student Count", fontsize=12)
plt.xticks(rotation=15)


plt.tight_layout()
plt.show()


# 🌟 Exercise 5: Comparing Anxiety Levels Across Different Genders
# Objective: Use a bar plot to compare the proportion of students experiencing anxiety across different genders.
# Dataset Overview: The dataset includes columns: ‘Do you have Anxiety?’ and ‘Choose your gender’.
# Tasks:
# Import necessary libraries.
# Use Seaborn to create a bar plot comparing anxiety levels across genders from the dataset df.
# Customize the plot with an appropriate color palette and add a title.
# Display the plot.


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 6))


    data=df,
    x="Choose your gender",
    hue="Do you have Anxiety?",
    palette="Set2",
)

plt.title(
    "Comparison of Anxiety Occurrence Across Genders",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)
plt.legend(title="Has Anxiety?")


plt.tight_layout()
plt.show()


# 🌟 Exercise 6: Exploring the Relationship Between Age and Panic Attacks
# Objective: Create a scatter plot to explore the relationship between students’ age and the occurrence of panic attacks.
# Dataset Overview: The dataset includes columns: ‘Age’ and ‘Do you have Panic Attacks?’.
# Tasks:
# Import necessary libraries.
# Convert panic attack responses to numeric values (e.g., Yes=1, No=0).
# Use Seaborn’s scatterplot to create a scatter plot with ‘Age’ on the x-axis and numeric panic attack responses on the y-axis.
# Customize the plot to improve readability by adding labels, a title, and adjusting point styles.
# Display the plot.

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df["Panic_Attacks_Numeric"] = (
    df["Do you have Panic Attacks?"].map({"Yes": 1, "No": 0}).fillna(0)
)

plt.figure(figsize=(9, 6))


jitter = np.random.normal(0, 0.03, size=len(df))


sns.scatterplot(
    data=df,
    x="Age",
    y=df["Panic_Attacks_Numeric"] + jitter,
    hue="Do you have Panic Attacks?",
    palette={"Yes": "crimson", "No": "royalblue"},
    s=100,  # Marker size
    alpha=0.7,
)


plt.title(
    "Relationship Between Student Age and Panic Attacks",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Age (Years)", fontsize=12)
plt.ylabel("Panic Attack Occurrence (0 = No, 1 = Yes)", fontsize=12)
plt.yticks([0, 1], ["No (0)", "Yes (1)"])


plt.tight_layout()
plt.show()

