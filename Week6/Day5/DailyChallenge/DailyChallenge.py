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


print('Dataset Shape:', df.shape)
print('Missing Values Count:\n', df.isnull().sum().sum())
print('\nFeature Data Types:\n', df.dtypes.value_counts())


stats_list = []
for col in df.columns:
  col_data = df[col]
  mode_val = stats.mode(col_data, keepdims=True).mode[0]
  stats_list.append({
      'Feature': col,
      'Mean': np.mean(col_data),
      'Median': np.median(col_data),
      'Mode': mode_val,
      'Range': np.ptp(col_data),
      'Variance': np.var(col_data),
      'Std Dev': np.std(col_data),
      'Skewness': stats.skew(col_data),
      'Kurtosis': stats.kurtosis(col_data),
  })

df_desc = pd.DataFrame(stats_list).set_index('Feature')
display(df_desc.round(2))


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


sns.boxplot(data=df, x='price_range', y='ram', ax=axes[0, 0], palette='Blues')
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
    palette='tab10',
    alpha=0.4,
)
axes[0, 1].set_title(
    '2. Battery Power Distribution by Price Class',
    fontsize=12,
    fontweight='bold',
)
axes[0, 1].set_xlabel('Battery Power (mAh)')


sns.scatterplot(
    data=df,
    x='ram',
    y='px_height',
    hue='price_range',
    palette='Set1',
    alpha=0.7,
    ax=axes[1, 0],
    s=30,
)
axes[1, 0].set_title(
    '3. RAM vs. Pixel Height by Price Range', fontsize=12, fontweight='bold'
)
axes[1, 0].set_xlabel('RAM (MB)')
axes[1, 0].set_ylabel('Pixel Height')


top_cols = [
    'ram',
    'battery_power',
    'px_height',
    'px_width',
    'int_memory',
    'price_range',
]
corr_matrix = df[top_cols].corr()
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    ax=axes[1, 1],
    cbar=True,
)
axes[1, 1].set_title(
    '4. Feature Correlation Matrix Heatmap', fontsize=12, fontweight='bold'
)

plt.tight_layout()
plt.show()

