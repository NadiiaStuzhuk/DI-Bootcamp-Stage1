# Daily Challenge: NumPy, Pandas, and Matplotlib Integration


# Objective:
# To integrate your knowledge of NumPy with Pandas and Matplotlib, demonstrating your ability to manipulate and visualize data effectively.



# 🛠️ What you will create
# A comprehensive data analysis and visualization project, showcasing temperature trends across different regions using NumPy, Pandas, and Matplotlib.


# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# How to effectively integrate NumPy, Pandas, and Matplotlib for data manipulation and visualization.
# Techniques for analyzing and visualizing global weather trends using these libraries.


# Challenge Description:
# Scenario: You are a data analyst working with a dataset of global weather. Your task is to analyze temperature trends and visualize the results.

# Tasks:

# 1. Data Preparation:

# Hint 1: Use np.random.uniform(low, high, size) to generate the temperature data.
# Hint 2: Create a DataFrame using pd.DataFrame(data, index, columns) with appropriate index and columns.

# Use NumPy to generate a synthetic dataset representing average monthly temperatures (in degrees Celsius) for 12 months across 10 different cities. The temperatures should range from -5 to 35 degrees.

# Convert this NumPy array into a Pandas DataFrame, adding city names as index and months as columns.
# 2. Data Analysis:

# Hint 1: Calculate the annual average temperature using DataFrame.mean(axis).
# Hint 2: Find the city with the highest and lowest average temperature using idxmax() and idxmin() methods.

# Calculate the annual average temperature for each city.

# Identify the city with the highest and lowest average temperature for the year.
# 3. Data Visualization:



# Possible visualization might be:


# daily


# Deliverables:
# A Jupyter Notebook containing all the code for data generation, analysis, and visualization.
# A brief report within the notebook summarizing your findings, including the city with the highest and lowest average temperatures and any interesting trends observed in the data.


# Evaluation Criteria:
# Correctness and efficiency of NumPy and Pandas code used for data manipulation.
# Effectiveness of data visualization in conveying the temperature trends.
# Clarity and conciseness of the summary report.
# Good luck!

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


np.random.seed(42)

cities = [
    "New York", "London", "Tokyo", "Sydney", "Cairo",
    "Moscow", "Rio de Janeiro", "Toronto", "Paris", "Mumbai"
]
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]


temp_array = np.random.uniform(low=-5, high=35, size=(10, 12))


df_temp = pd.DataFrame(data=temp_array, index=cities, columns=months).round(1)

print("=== Monthly Temperature Dataset (°C) ===")
display(df_temp)


annual_avg = df_temp.mean(axis=1).round(2)


df_temp['Annual Avg'] = annual_avg


hottest_city = annual_avg.idxmax()
hottest_temp = annual_avg.max()

coldest_city = annual_avg.idxmin()
coldest_temp = annual_avg.min()

print("\n=== Annual Average Temperatures (°C) ===")
print(annual_avg.to_string())

print(f"\n🔥 Hottest City: {hottest_city} ({hottest_temp}°C)")
print(f"❄️ Coldest City: {coldest_city} ({coldest_temp}°C)")


sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 11))


sns.heatmap(
    df_temp.drop(columns=['Annual Avg']),
    annot=True,
    fmt=".1f",
    cmap="YlOrRd",
    ax=axes[0, 0],
    cbar_kws={'label': 'Temperature (°C)'}
)
axes[0, 0].set_title("1. Monthly Temperature Heatmap (°C) across Cities", fontsize=13, fontweight="bold")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("City")


cities_sorted = annual_avg.sort_values(ascending=True)
colors = [
    'skyblue' if city == coldest_city else ('crimson' if city == hottest_city else 'slategray')
    for city in cities_sorted.index
]
axes[0, 1].barh(cities_sorted.index, cities_sorted.values, color=colors)
axes[0, 1].set_title("2. Annual Average Temperature Ranking by City", fontsize=13, fontweight="bold")
axes[0, 1].set_xlabel("Average Temperature (°C)")
axes[0, 1].set_ylabel("City")


for i, v in enumerate(cities_sorted.values):
    axes[0, 1].text(v + 0.3, i, f"{v:.2f}°C", va='center', fontweight='bold', fontsize=10)


selected_cities = [hottest_city, coldest_city, "New York", "Tokyo", "Sydney"]
for city in selected_cities:
    axes[1, 0].plot(months, df_temp.loc[city, months], marker='o', linewidth=2, label=city)

axes[1, 0].set_title("3. Monthly Temperature Trends for Key Cities", fontsize=13, fontweight="bold")
axes[1, 0].set_xlabel("Month")
axes[1, 0].set_ylabel("Temperature (°C)")
axes[1, 0].legend()
axes[1, 0].grid(True, linestyle="--", alpha=0.6)


sns.boxplot(data=df_temp[months], ax=axes[1, 1], palette="coolwarm")
axes[1, 1].set_title("4. Monthly Temperature Spread & Global Distribution", fontsize=13, fontweight="bold")
axes[1, 1].set_xlabel("Month")
axes[1, 1].set_ylabel("Temperature (°C)")

plt.tight_layout()
plt.show()