# Daily Challenge : Comprehensive Mobile Price Analysis


# Mobile



# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Master advanced data manipulation and statistical analysis using NumPy and SciPy.
# Gain proficiency in data preprocessing and exploration with Pandas.
# Develop skills in creating detailed, informative visualizations with Matplotlib.
# Learn to synthesize complex analytical findings into clear, actionable insights.


# Project Tasks
# 1. Data Loading and Exploration:
# Utilize Pandas to load the dataset and explore its initial structure.
# Summarize features, target variable, and their respective data types.
# Conduct basic descriptive statistics for an overview of the dataset.


# 2. Data Cleaning and Preprocessing:
# Address missing or null values.
# Transform categorical data into numerical format using suitable methods.


# 3. Statistical Analysis with NumPy and SciPy:
# Execute detailed statistical analysis on each feature, including:
# Calculation of central tendency measures (mean, median, mode).
# Analysis of variability (range, variance, standard deviation).
# Evaluation of distribution shapes through skewness and kurtosis.
# Perform hypothesis testing for statistical significance between groups (e.g., different price ranges).
# Investigate feature-target correlations using SciPy.
# Apply advanced SciPy statistical functions for deeper insights.


# 4. Data Visualization with Matplotlib:
# Produce histograms, scatter plots, and box plots for data distribution and relationship insights.
# Employ heatmaps for correlation visualization.
# Ensure clarity in plots with appropriate titles, labels, and axis information.


# 5. Insight Synthesis and Conclusion:
# Derive conclusions from statistical tests and visualizations.
# Identify key determinants in mobile price classification.
# Highlight any unexpected or significant findings.


# 📖 Useful Resources
# Download the train dataset from this repository, it comes from the Mobile Price Classification Dataset

# Check out this page to understand the attributes | Noise-Resilient Mobile Price Classification



# Project Submission
# Submit the following in a GitHub repository:

# Data_Analysis.ipynb: A comprehensive Jupyter Notebook encapsulating:
# Clean, well-commented Python code.
# Distinct headings for each analysis phase.
# In-depth comments elucidating findings and the importance of each analytical step.


# Pro Tips
# Individually examine each feature to grasp its unique traits and influence.
# Utilize visualizations not just for data representation, but as pivotal supports for your analytical conclusions.
# Reference course materials for guidance on complex statistical functions and their practical uses.

import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns

warnings.filterwarnings('ignore')
sns.set_theme(style='whitegrid')


df = pd.read_csv('train.csv')


print(f'Dataset Dimensions: {df.shape[0]} rows, {df.shape[1]} columns\n')
print('Data Types and Non-Null Counts:')
print(df.info())


print('\nTarget Variable (price_range) Distribution:')
print(df['price_range'].value_counts().sort_index())


missing_vals = df.isnull().sum().sum()
duplicate_rows = df.duplicated().sum()

print(f'Total Missing Values: {missing_vals}')
print(f'Total Duplicate Rows: {duplicate_rows}')


non_numeric_cols = df.select_dtypes(exclude=[np.number]).columns
print(f'Non-numerical columns: {len(non_numeric_cols)}')


df.head()

stats_summary = []

for col in df.columns:
  series = df[col]
  mode_val = stats.mode(series, keepdims=True).mode[0]

  stats_summary.append({
      'Feature': col,
      'Mean': np.mean(series),
      'Median': np.median(series),
      'Mode': mode_val,
      'Min': np.min(series),
      'Max': np.max(series),
      'Range': np.ptp(series),
      'Variance': np.var(series, ddof=1),
      'Std Dev': np.std(series, ddof=1),
      'Skewness': stats.skew(series),
      'Kurtosis': stats.kurtosis(series),
  })

df_stats = pd.DataFrame(stats_summary).set_index('Feature')
display(df_stats.round(2))

hypothesis_results = []

for col in df.columns[:-1]:

  g0 = df[df['price_range'] == 0][col]
  g1 = df[df['price_range'] == 1][col]
  g2 = df[df['price_range'] == 2][col]
  g3 = df[df['price_range'] == 3][col]


  f_stat, p_val_anova = stats.f_oneway(g0, g1, g2, g3)


  p_corr, p_val_p = stats.pearsonr(df[col], df['price_range'])
  s_corr, p_val_s = stats.spearmanr(df[col], df['price_range'])

  hypothesis_results.append({
      'Feature': col,
      'Pearson r': p_corr,
      'Pearson p-val': p_val_p,
      'Spearman rho': s_corr,
      'ANOVA F-stat': f_stat,
      'ANOVA p-val': p_val_anova,
  })

df_hypo = (
    pd.DataFrame(hypothesis_results)
    .set_index('Feature')
    .sort_values('Pearson r', ascending=False)
)
display(df_hypo.round(4))

fig, axes = plt.subplots(2, 2, figsize=(16, 12))


sns.boxplot(data=df, x='price_range', y='ram', ax=axes[0, 0], palette='Purples')
axes[0, 0].set_title(
    '1. RAM (MB) Distribution across Price Ranges',
    fontsize=12,
    fontweight='bold',
)
axes[0, 0].set_xlabel('Price Range (0: Low, 1: Medium, 2: High, 3: Very High)')
axes[0, 0].set_ylabel('RAM (MB)')


sns.histplot(
    data=df,
    x='battery_power',
    hue='price_range',
    kde=True,
    ax=axes[0, 1],
    palette='Set2',
    alpha=0.4,
)
axes[0, 1].set_title(
    '2. Battery Power Distribution by Price Tier',
    fontsize=12,
    fontweight='bold',
)
axes[0, 1].set_xlabel('Battery Power (mAh)')


df['px_area'] = df['px_height'] * df['px_width']
sns.scatterplot(
    data=df,
    x='ram',
    y='px_area',
    hue='price_range',
    palette='viridis',
    alpha=0.7,
    ax=axes[1, 0],
    s=35,
)
axes[1, 0].set_title(
    '3. RAM vs. Pixel Area (Resolution) by Price Class',
    fontsize=12,
    fontweight='bold',
)
axes[1, 0].set_xlabel('RAM (MB)')
axes[1, 0].set_ylabel('Pixel Area ($px^2$)')


top_features = [
    'ram',
    'battery_power',
    'px_width',
    'px_height',
    'int_memory',
    'price_range',
]
corr_matrix = df[top_features].corr()
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    ax=axes[1, 1],
    cbar=True,
)
axes[1, 1].set_title(
    '4. Correlation Heatmap for Top Numerical Features',
    fontsize=12,
    fontweight='bold',
)

plt.tight_layout()
plt.show()

Summary of FindingsDominant Determinant: RAM capacity is the overwhelming predictor of smartphone price class ($r = 0.9171$, $F = 3520.11$, $p < 0.0001$). Price tiers segment almost linearly into distinct RAM ranges.Secondary Hardware Drivers: Battery Power ($r = 0.2007$, $p < 0.0001$) and Display Resolution (px_width: $r = 0.1658$, px_height: $r = 0.1488$) serve as statistically significant secondary features that separate premium tiers from budget models.Non-Differentiating Features: Commodity connectivity options (wifi, blue, touch_screen, four_g, three_g) show virtually zero correlation with the target class ($p > 0.05$). These features are baseline standards available across all market segments.