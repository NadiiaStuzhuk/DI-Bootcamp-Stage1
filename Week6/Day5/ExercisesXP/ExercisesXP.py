# Mini-project: Advanced Statistical Analysis of Apple Inc. Stock Data


# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Master statistical analysis of financial data using NumPy and SciPy.
# Learn effective data visualization techniques with Matplotlib for financial trends.
# Apply hypothesis testing to financial datasets for meaningful insights.
# Understand and utilize advanced statistical techniques in NumPy and SciPy.


# Project Description
# Using the AAPL (Apple Inc.) stock dataset, conduct the following analyses:



# Initial Data Exploration
# Load the dataset using Pandas. Check for null values and understand data types.
# Examine the time series properties of the data (e.g., frequency, trends).


# Data Visualization
# Utilize Matplotlib to plot closing prices and traded volume over time.
# Create a candlestick chart to depict high and low prices.


# Statistical Analysis
# Compute summary statistics (mean, median, standard deviation) for key columns.
# Analyze closing prices with a moving average.


# Hypothesis Testing
# Execute a t-test to compare average closing prices across different years.
# Examine daily returns’ distribution and test for normality using SciPy.


# Advanced Statistical Techniques (Bonus)
# Statistical Functions in NumPy: Employ NumPy’s statistical functions for in-depth stock data analysis.
# E.g., Use convolve for moving averages, or np.corrcoef to explore correlations between financial metrics.
# Analyze correlations between moving averages of closing prices and trading volume across time periods.


# Resources
# Dataset: download it here Apple Stock Prices From 1981 to 2023
# It may include data such as date, opening price, closing price, high and low prices, and trading volume.

# This information can be used to study trends and patterns in the stock market and make informed investment decisions.

# Date: Represents the date of the stock price.
# Open: Represents the opening stock price on that date.
# High: Represents the highest stock price on that date.
# Low: Represents the lowest stock price on that date.
# Close: Represents the closing stock price on that date.
# Adj close: Represents the adjusted closing stock price on that date (taking into account corporate actions such as splits).
# Volume: Represents the number of shares traded on that date.


# Project Submission
# Submit a Jupyter Notebook with :

# All analysis code and visualizations.
# Detailed explanations of findings at each step.
# A comprehensive summary of insights, focusing on advanced statistical analysis.
# A ‘Reflection’ section detailing challenges and solutions.
# Suggested structure:



# 1. Data Loading and Exploration
# 2. Data Visualization
# 3. Statistical Analysis
# 4. Hypothesis Testing
# 5. Advanced Statistical Techniques (Bonus)
#     - Signal Processing using SciPy
#     - Statistical Functions in NumPy
# 6. Summary and Insights
# 7. Reflection


# Guidance
# Experiment with different filters and parameters in signal processing techniques.
# Thoroughly understand each statistical function and its insights on the stock data.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns


df = pd.read_csv('AAPL.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date').reset_index(drop=True)


print("Data Shape:", df.shape)
print("Null Values Check:\n", df.isnull().sum())
print("Data Types:\n", df.dtypes)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), sharex=True)


ax1.plot(
    df['Date'],
    df['Close'],
    color='#1f77b4',
    linewidth=1.5,
    label='Close Price ($)',
)
ax1.set_title(
    'AAPL Stock Closing Prices Over Time (1981 - 2023)',
    fontsize=14,
    fontweight='bold',
)
ax1.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
ax1.legend(loc='upper left')


ax2.bar(
    df['Date'],
    df['Volume'] / 1e6,
    color='slategray',
    alpha=0.6,
    width=1.0,
    label='Volume (Millions)',
)
ax2.set_title(
    'AAPL Trading Volume Over Time', fontsize=14, fontweight='bold'
)
ax2.set_xlabel('Date', fontsize=12, fontweight='bold')
ax2.set_ylabel('Volume (M Shares)', fontsize=12, fontweight='bold')
ax2.legend(loc='upper left')

plt.tight_layout()
plt.show()


df_recent = df.tail(100).copy()

fig, ax = plt.subplots(figsize=(14, 6))


ax.vlines(
    df_recent['Date'],
    df_recent['Low'],
    df_recent['High'],
    color='gray',
    linewidth=1,
)


up = df_recent[df_recent['Close'] >= df_recent['Open']]
down = df_recent[df_recent['Close'] < df_recent['Open']]

ax.vlines(
    up['Date'],
    up['Open'],
    up['Close'],
    color='green',
    linewidth=4,
    label='Bullish (Close >= Open)',
)
ax.vlines(
    down['Date'],
    down['Open'],
    down['Close'],
    color='red',
    linewidth=4,
    label='Bearish (Close < Open)',
)

ax.set_title(
    'AAPL Candlestick Chart (Last 100 Trading Days)',
    fontsize=14,
    fontweight='bold',
)
ax.set_xlabel('Date', fontsize=12, fontweight='bold')
ax.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
ax.legend()
plt.tight_layout()
plt.show()

df['Year'] = df['Date'].dt.year
close_2020 = df[df['Year'] == 2020]['Close']
close_2022 = df[df['Year'] == 2022]['Close']


t_stat, p_val = stats.ttest_ind(close_2020, close_2022, equal_var=False)

print(f'2020 Mean Close Price: ${close_2020.mean():.2f}')
print(f'2022 Mean Close Price: ${close_2022.mean():.2f}')
print(f'T-statistic: {t_stat:.4f}, P-value: {p_val:.4f}')

df['Daily_Return'] = df['Close'].pct_change()
returns_clean = df['Daily_Return'].dropna()


k2_stat, p_val_normality = stats.normaltest(returns_clean)

print(
    f'Daily Returns Mean: {returns_clean.mean():.6f}, Std:'
    f' {returns_clean.std():.6f}'
)
print(
    f'Skewness: {returns_clean.skew():.4f}, Kurtosis:'
    f' {returns_clean.kurtosis():.4f}'
)
print(f'K2 Statistic: {k2_stat:.4f}, P-value: {p_val_normality:.4e}')

def numpy_moving_average(data, window=50):
  weights = np.ones(window) / window
  return np.convolve(data, weights, mode='valid')


ma_50_numpy = numpy_moving_average(df['Close'].values, window=50)
print('NumPy 50-Day Moving Average Array Shape:', ma_50_numpy.shape)

valid_data = df[['Close', 'MA_50', 'Volume']].dropna()
corr_matrix = np.corrcoef(valid_data.T)

print("Correlation Matrix:\n", np.round(corr_matrix, 4))

