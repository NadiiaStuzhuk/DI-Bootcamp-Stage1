# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# How to apply various statistical functions using SciPy
# Understanding probability distributions and hypothesis testing
# Analyzing data with regression, ANOVA, and correlation methods


# 🛠️ What you will create
# You will create a series of Python scripts that perform different statistical analyses, including data exploration, hypothesis testing, linear regression, ANOVA, and more.



# 🌟 Exercise 1: Basic Usage of SciPy
# Task: Import the SciPy library and explore its version.


import scipy

# Check and print the installed SciPy version
print(f"SciPy Version: {scipy.__version__}")


# 🌟 Exercise 2: Descriptive Statistics
# Task: Given a sample dataset, calculate the mean, median, variance, and standard deviation using SciPy.
# Sample Dataset:
# data = [12, 15, 13, 12, 18, 20, 22, 21]


import numpy as np
from scipy import stats

data = [12, 15, 13, 12, 18, 20, 22, 21]

# Calculate descriptive statistics using SciPy/NumPy
mean_val = np.mean(data)
median_val = np.median(data)
variance_val = np.var(data, ddof=1)  # Sample variance
std_dev_val = np.std(data, ddof=1)  # Sample standard deviation

# Alternative using scipy.stats.describe
desc = stats.describe(data)

print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Variance (Sample): {variance_val:.2f}")
print(f"Standard Deviation (Sample): {std_dev_val:.2f}")

# 🌟 Exercise 3: Understanding Distributions
# Task: Generate a normal distribution using SciPy with a mean of 50 and a standard deviation of 10. Plot this distribution.
# Code Example:
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm

# # complete your code here

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Define distribution parameters
mean = 50
std_dev = 10

# Generate x values covering 4 standard deviations from the mean
x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 1000)

# Calculate the Probability Density Function (PDF) using SciPy
y = norm.pdf(x, loc=mean, scale=std_dev)

# Plot the distribution
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=f"Normal Distribution\n(μ={mean}, σ={std_dev})", color="blue", linewidth=2)
plt.title("Normal Probability Distribution Function")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.show()

# 🌟 Exercise 4: T-Test Application
# Task: Perform a T-test on two sets of randomly generated data.
# Code Example:
# data1 = np.random.normal(50, 10, 100)
# data2 = np.random.normal(60, 10, 100)

# # complete your code here

import numpy as np
from scipy import stats

# Generate random datasets
np.random.seed(42)  # For reproducible output
data1 = np.random.normal(50, 10, 100)
data2 = np.random.normal(60, 10, 100)

# Perform Two-Sample Independent T-Test
t_stat, p_value = stats.ttest_ind(data1, data2)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4e}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Conclusion: Reject the null hypothesis. There is a statistically significant difference between the two datasets.")
else:
    print("Conclusion: Fail to reject the null hypothesis. No statistically significant difference detected.")

# 🌟 Exercise 5: Linear Regression Analysis
# Objective: Apply linear regression to a dataset and interpret the results.

# Task: Given a dataset of housing prices (house_prices) and their corresponding sizes (house_sizes), use linear regression to predict the price of a house given its size.
# Dataset:
# house_sizes: [50, 70, 80, 100, 120] (in square meters)
# house_prices: [150,000, 200,000, 210,000, 250,000, 280,000] (in currency units)
# Questions:
# What is the slope and intercept of the regression line?
# Predict the price of a house that is 90 square meters.
# Interpret the meaning of the slope in the context of housing prices.

from scipy import stats

# Dataset
house_sizes = [50, 70, 80, 100, 120]  # sq meters
house_prices = [150000, 200000, 210000, 250000, 280000]  # currency

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(house_sizes, house_prices)

# 1. Slope and Intercept
print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")

# 2. Predict price for a 90 sq meter house
predicted_size = 90
predicted_price = (slope * predicted_size) + intercept
print(f"Predicted price for a {predicted_size} sq.m house: {predicted_price:,.2f}")

Questions & Interpretations: Slope and Intercept:
Slope ($\beta_1$): 1815.79Intercept ($\beta_0$): 62894.74
Predicted Price: A 90 sq. meter house is predicted to cost $226,315.79.
Meaning of the Slope: The slope represents the estimated change in house price per additional square meter. In this context, for every 1 square meter increase in size, the estimated house price increases by 1,815.79 currency units.

# 🌟 Exercise 6: Understanding ANOVA
# Objective: Test understanding of ANOVA and its application.

# Task: Three different fertilizers are applied to three separate groups of plants to test their effectiveness. The growth in centimeters is recorded.
# Dataset:
# fertilizer_1: [5, 6, 7, 6, 5]
# fertilizer_2: [7, 8, 7, 9, 8]
# fertilizer_3: [4, 5, 4, 3, 4]
# Questions:
# Perform an ANOVA test on the given data. What are the F-value and P-value?
# Based on the P-value, do the fertilizers have significantly different effects on plant growth?
# Explain what would happen if the P-value were greater than 0.05.

from scipy import stats

# Datasets
fertilizer_1 = [5, 6, 7, 6, 5]
fertilizer_2 = [7, 8, 7, 9, 8]
fertilizer_3 = [4, 5, 4, 3, 4]

# Perform One-Way ANOVA
f_val, p_val = stats.f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)

print(f"F-value: {f_val:.4f}")
print(f"P-value: {p_val:.6f}")

Answers & Interpretation:ANOVA Results:
F-value: 27.4286P-value: 0.000037 ($3.71 \times 10^{-5}$)
Significance Decision: 
Since the P-value ($0.000037$) is significantly less than the threshold ($\alpha = 0.05$), we reject the null hypothesis.                                                                 
The fertilizers do have significantly different effects on plant growth.If P-value were greater than 0.05: If $P > 0.05$, we would fail to reject the null hypothesis. This would mean there is no statistically significant difference in average plant growth across the three fertilizer groups—any observed differences would likely be due to random chance.

# 🌟 Exercise 7: Probability Distributions (Optional)
# Work with a binomial distribution: calculate probabilities for different numbers of successes.
# Example: Calculating the probability of getting exactly 5 heads in 10 coin flips.

from scipy.stats import binom

# Parameters
n = 10     # Number of coin flips
p = 0.5    # Probability of heads in a single flip
k = 5      # Target number of heads

# Probability Mass Function (PMF) for exactly 5 heads
prob_exact_5 = binom.pmf(k, n, p)

print(f"Probability of getting exactly 5 heads in 10 flips: {prob_exact_5:.4f} ({prob_exact_5 * 100:.2f}%)")

# 🌟 Exercise 8: Correlation Coefficients (Optional)
# Calculate the Pearson and Spearman correlation coefficients between two variables in a dataset.
# Example in code: data = pd.DataFrame({'age': [23, 25, 30, 35, 40], 'income': [35000, 40000, 50000, 60000, 70000]})




