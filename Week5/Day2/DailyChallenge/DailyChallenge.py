# Daily Challenge: Analysis of Airplane Crashes and Fatalities


# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Comprehensive data analysis techniques using Python, Pandas, NumPy, and SciPy.
# Methods for data cleaning, exploratory analysis, statistical testing, and visualization.
# Insightful interpretation of complex datasets.


# 🛠️ What you will create
# A thorough analysis of the “Airplane Crashes and Fatalities up to 2023” dataset, including detailed visualizations and statistical insights.


# Objective:
# Utilize Python, Pandas, NumPy, and SciPy to conduct a thorough analysis of the “Airplane Crashes and Fatalities upto 2023” dataset. This challenge will encompass data cleaning, exploratory analysis, statistical testing, and visualization to draw meaningful insights.



# Dataset:
# Work with the “Airplane Crashes and Fatalities upto 2023” dataset, which provides comprehensive details about airplane crashes, including dates, locations, fatalities, and more. Access the dataset here.



# Tasks:
# 1. Data Import and Cleaning:

# Import the dataset using Pandas.
# Clean and preprocess the data, addressing missing values and categorizing data as needed.
# Convert dates and other relevant fields to appropriate formats.
# 2. Exploratory Data Analysis:

# Use Pandas to explore basic statistics such as the number of crashes, fatalities, and survival rates.
# Analyze the frequency of crashes over time to identify any trends.
# 3. Statistical Analysis:

# Apply SciPy to analyze the distribution of fatalities and survival rates. Calculate key statistics like mean, median, and standard deviation.
# Conduct a hypothesis test (e.g., comparing the average number of fatalities in different decades or regions).
# 4. Visualization:

# Create charts and graphs using Matplotlib and Seaborn to visualize the findings from your exploratory data analysis and statistical tests.
# Examples might include time series plots of crashes over years, bar charts of crashes by region, and histograms of fatalities.
# 5. Insight and Report:

# Summarize your findings and provide insights into the patterns or anomalies discovered in the data.
# Prepare a well-structured report including all code, visualizations, and interpretations.


# Submission:
# You should submit a comprehensive report encompassing their code, analysis, and visualizations. Articulate how you have applied NumPy, Pandas, and SciPy in your analysis, highlighting any significant patterns or insights discovered in the dataset.

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

dataset_path = "Airplane_Crashes_and_Fatalities_Since_1908.csv"

df = pd.read_csv(dataset_path)

print("--- Initial Data Summary ---")
print(f"Dataset Shape: {df.shape}")
print(df.info())

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

df['date'] = pd.to_datetime(df['date'], errors='coerce')

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['decade'] = (df['year'] // 10) * 10


df['fatalities'] = pd.to_numeric(df['fatalities'], errors='coerce').fillna(0)
df['aboard'] = pd.to_numeric(df['aboard'], errors='coerce').fillna(0)
df['ground'] = pd.to_numeric(df['ground'], errors='coerce').fillna(0)


df['survivors'] = np.maximum(df['aboard'] - df['fatalities'], 0)
df['survival_rate'] = np.where(df['aboard'] > 0, df['survivors'] / df['aboard'], 0)


df['operator'] = df['operator'].fillna('Unknown')
df['location'] = df['location'].fillna('Unknown')

print("\n--- Cleaned Data Overview ---")
print(df[['date', 'year', 'aboard', 'fatalities', 'survivors', 'survival_rate']].head())


total_incidents = len(df)
total_fatalities = int(df['fatalities'].sum())
total_aboard = int(df['aboard'].sum())
total_survivors = int(df['survivors'].sum())
overall_survival_rate = (total_survivors / total_aboard * 100) if total_aboard > 0 else 0

print("\n==========================================")
print("       EXPLORATORY DATA ANALYSIS           ")
print("==========================================")
print(f"Total Incidents Recorded: {total_incidents:,}")
print(f"Total Passengers/Crew Aboard: {total_aboard:,}")
print(f"Total Fatalities: {total_fatalities:,}")
print(f"Total Survivors: {total_survivors:,}")
print(f"Overall Survival Rate: {overall_survival_rate:.2f}%")


crashes_per_year = df.groupby('year').size()
peak_year_crashes = crashes_per_year.idxmax()
print(f"Year with Most Crashes: {peak_year_crashes} ({crashes_per_year.max()} crashes)")


top_operators = df['operator'].value_counts().head(5)
print("\nTop 5 Operators by Number of Incidents:")
print(top_operators)


print("\n==========================================")
print("         STATISTICAL ANALYSIS             ")
print("==========================================")


fatality_stats = stats.describe(df['fatalities'])
print(f"Fatalities Mean: {np.mean(df['fatalities']):.2f}")
print(f"Fatalities Median: {np.median(df['fatalities']):.2f}")
print(f"Fatalities Std Dev: {np.std(df['fatalities'], ddof=1):.2f}")
print(f"Fatalities Skewness: {stats.skew(df['fatalities']):.2f}")


fatalities_1970s = df[df['decade'] == 1970]['fatalities']
fatalities_2000s = df[df['decade'] == 2000]['fatalities']


u_stat, p_val = stats.mannwhitneyu(fatalities_1970s, fatalities_2000s)

print(f"\n1970s Mean Fatalities per Crash: {fatalities_1970s.mean():.2f}")
print(f"2000s Mean Fatalities per Crash: {fatalities_2000s.mean():.2f}")
print(f"Mann-Whitney U Statistic: {u_stat:.2f}")
print(f"p-value: {p_val:.6e}")

if p_val < 0.05:
    print("Conclusion: Reject Null Hypothesis. There is a statistically significant difference in fatalities per crash between the 1970s and 2000s.")
else:
    print("Conclusion: Fail to Reject Null Hypothesis. No statistically significant difference detected.")


fig, axes = plt.subplots(2, 2, figsize=(16, 10))


axes[0, 0].plot(crashes_per_year.index, crashes_per_year.values, color='firebrick', linewidth=2)
axes[0, 0].set_title('Annual Number of Aviation Accidents', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Year')
axes[0, 0].set_ylabel('Number of Incidents')


fatalities_by_decade = df.groupby('decade')['fatalities'].sum().reset_index()
sns.barplot(data=fatalities_by_decade, x='decade', y='fatalities', ax=axes[0, 1], palette='flare')
axes[0, 1].set_title('Total Fatalities by Decade', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Decade')
axes[0, 1].set_ylabel('Total Fatalities')
axes[0, 1].tick_params(axis='x', rotation=45)


sns.histplot(df['fatalities'], bins=30, kde=True, ax=axes[1, 0], color='teal')
axes[1, 0].set_title('Distribution of Fatalities per Incident', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Fatalities Count')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_yscale('log')


top_10_ops = df['operator'].value_counts().head(10).reset_index()
top_10_ops.columns = ['operator', 'count']
sns.barplot(data=top_10_ops, x='count', y='operator', ax=axes[1, 1], palette='crest')
axes[1, 1].set_title('Top 10 Operators by Total Incidents', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Incident Count')
axes[1, 1].set_ylabel('Operator')

plt.tight_layout()
plt.show()

1. Temporal Trends in Aviation SafetyPeak Accident Era: 
Aviation incidents rose significantly during the mid-20th century, reaching a peak in the 1970s. 
This surge corresponds to the rapid expansion of commercial aviation and increased air traffic volumes prior to modern automated safety systems.Sharp Modern Decline: Since the late 1990s and 2000s, total crashes and fatalities have shown a steady downward trajectory despite exponential growth in worldwide passenger volume, reflecting major advancements in radar technology, avionics, training protocols, and international regulatory standards.

2. Distribution & Skewness of FatalitiesExtreme Right Skew: The distribution of fatalities per crash exhibits a strong right skew ($\text{skewness} > 2.0$). 
Most incidents in the dataset involve small charter/military flights or localized incidents with under 20 fatalities, while rare commercial airline disasters account for extreme upper tail values.Mean vs. Median Discrepancy: The mean fatality count per crash is substantially higher than the median, confirming that a small number of catastrophic multi-engine jet airliner accidents disproportionately skew the arithmetic average.

3. Hypothesis Testing (1970s vs. 2000s)
Statistical Choice: Due to non-normality and severe right-skewness, the non-parametric Mann-Whitney U Test was applied rather than a standard $t$-test.Result: The test yielded $p < 0.001$, leading to a rejection of the null hypothesis. Aircraft capacity grew larger in the 1970s–2000s era, but improved airframe design and cabin evacuation protocols altered the fatality profiles per crash event.