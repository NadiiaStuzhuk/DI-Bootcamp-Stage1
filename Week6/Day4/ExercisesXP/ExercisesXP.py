# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Understanding and calculating the determinant and inverse of matrices.
# Application of these concepts in linear algebra and their significance.


# 🛠️ What you will create
# Practical examples demonstrating the computation of matrix determinants and inverses using NumPy, applying these concepts to solve real-world problems.


# 🌟 Exercise 1 : Matrix Operations
# Instructions
# In this exercise, you’ll work with a 3x3 matrix. Here’s a brief explanation of the concepts:

# Determinant: The determinant is a value that can be computed from the elements of a square matrix. It provides important information about the matrix, such as whether it has an inverse, and is used in various areas like linear algebra and calculus. To understand more about it you can watch this video.
# Inverse of a Matrix: The inverse of a matrix is a matrix that, when multiplied with the original matrix, results in an identity matrix. Not all matrices have inverses. The inverse is crucial in solving systems of linear equations.
# Create a 3x3 matrix and perform the following operations:

# Calculate the determinant.
# Find the inverse of the matrix.

import numpy as np

# Create a 3x3 square matrix
A = np.array([
    [2, 1, 3],
    [0, 5, 6],
    [7, 8, 9]
])


det_A = np.linalg.det(A)


inv_A = np.linalg.inv(A)

print("Matrix A:\n", A)
print("Determinant:", round(det_A, 2))
print("Inverse Matrix:\n", np.round(inv_A, 4))

# 🌟 Exercise 2 : Statistical Analysis
# Instructions
# In this exercise, you’ll calculate statistical measures for a dataset:

# Mean: The average value of a dataset.
# Median: The middle value in a dataset when it is arranged in ascending or descending order.
# Standard Deviation: A measure of the amount of variation or dispersion in a set of values.
# Using NumPy, generate an array of 50 random numbers and compute:

# The mean and median.
# The standard deviation.

import numpy as np


np.random.seed(42)
data = np.random.randn(50)


mean_val = np.mean(data)
median_val = np.median(data)
std_dev = np.std(data)

print(f"Mean: {mean_val:.4f}")
print(f"Median: {median_val:.4f}")
print(f"Standard Deviation: {std_dev:.4f}")

# 🌟 Exercise 3 : Date Manipulation
# Instructions
# Create a NumPy array of dates for the month of January 2023. Convert these dates to another format (e.g., YYYY/MM/DD).

import numpy as np


dates = np.arange('2023-01-01', '2023-02-01', dtype='datetime64[D]')


formatted_dates = np.array([np.datetime_as_string(d, unit='D').replace('-', '/') for d in dates])

print("First 5 formatted dates:", formatted_dates[:5])

# 🌟 Exercise 4 : Data Manipulation with NumPy and Pandas
# Instructions
# Create a DataFrame with random numbers and perform:

# Conditional selection of data.
# Aggregation functions like sum and average.

import pandas as pd
import numpy as np

# Create a DataFrame with random numbers
np.random.seed(42)
df = pd.DataFrame(np.random.randint(10, 100, size=(5, 4)), columns=['A', 'B', 'C', 'D'])


filtered_df = df[df['A'] > 50]


column_sums = df.sum()
column_means = df.mean()

print("Original DataFrame:\n", df)
print("\nConditional Selection (A > 50):\n", filtered_df)
print("\nColumn Sums:\n", column_sums)
print("\nColumn Means:\n", column_means)

# 🌟 Exercise 5 : Image Representation
# Instructions
# Explain how images are represented in NumPy arrays and demonstrate with a simple example (e.g., creating a 5x5 grayscale image).

import numpy as np


image_5x5 = np.array([
    [0,   64, 128, 192, 255],
    [64, 128, 192, 255, 128],
    [128, 192, 255, 128, 64],
    [192, 255, 128,  64,  0],
    [255, 128,  64,   0,  0]
], dtype=np.uint8)

print("5x5 Grayscale Image Matrix:\n", image_5x5)

# 🌟 Exercise 6 : Basic Hypothesis Testing
# Instructions
# Create a sample dataset to test the effectiveness of a new training program on employee productivity:


# import numpy as np

# # Productivity scores of employees before the training program
# productivity_before = np.random.normal(loc=50, scale=10, size=30)

# # Productivity scores of the same employees after the training program
# productivity_after = productivity_before + np.random.normal(loc=5, scale=3, size=30)

# # Your task is to formulate a hypothesis regarding the training program's effectiveness 
# # and test it using basic statistical functions in NumPy.


# Given a dataset, formulate a simple hypothesis and test it using basic statistical functions in NumPy.

import numpy as np

np.random.seed(42)
productivity_before = np.random.normal(loc=50, scale=10, size=30)
productivity_after = productivity_before + np.random.normal(loc=5, scale=3, size=30)

# Formulate Hypothesis:
# Null Hypothesis (H0): The training program has no effect (mean difference <= 0).
# Alternative Hypothesis (H1): The training program increases productivity (mean difference > 0).


diff = productivity_after - productivity_before
mean_diff = np.mean(diff)
std_diff = np.std(diff, ddof=1)
n = len(diff)


t_stat = mean_diff / (std_diff / np.sqrt(n))

print(f"Mean Productivity Increase: {mean_diff:.2f}")
print(f"Calculated t-statistic: {t_stat:.2f}")


if t_stat > 2.0:
    print("Result: Reject H0. The training program significantly improved productivity.")
else:
    print("Result: Fail to reject H0.")

# 🌟 Exercise 7 : Complex Array Comparison
# Instructions
# Create two arrays and perform element-wise comparison to find which elements are greater in the first array.

# The expected output is a boolean array showing which elements in the first array are greater than the corresponding elements in the second array.

import numpy as np

array1 = np.array([12, 45, 67, 89, 23])
array2 = np.array([15, 40, 67, 70, 30])

is_greater = array1 > array2

print("Array 1:", array1)
print("Array 2:", array2)
print("Is Array 1 > Array 2?:", is_greater)

# 🌟 Exercise 8 : Time Series Data Manipulation
# Instructions
# Generate time series data for the year 2023. Demonstrate slicing for the following intervals:

# January to March
# April to June
# July to September
# October to December
# Generate a time series data for a specific period and demonstrate how to slice this data for different intervals.

import pandas as pd
import numpy as np


date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
np.random.seed(42)
ts_data = pd.Series(np.random.randn(len(date_range)), index=date_range)


jan_to_mar = ts_data['2023-01-01':'2023-03-31']
apr_to_jun = ts_data['2023-04-01':'2023-06-30']
jul_to_sep = ts_data['2023-07-01':'2023-09-30']
oct_to_dec = ts_data['2023-10-01':'2023-12-31']

print(f"Jan - Mar records: {len(jan_to_mar)}")
print(f"Apr - Jun records: {len(apr_to_jun)}")
print(f"Jul - Sep records: {len(jul_to_sep)}")
print(f"Oct - Dec records: {len(oct_to_dec)}")

# 🌟 Exercise 9 : Data Conversion
# Instructions
# Demonstrate how to convert a NumPy array to a Pandas DataFrame and vice versa.

import pandas as pd
import numpy as np


np_array = np.array([[10, 20, 30], [40, 50, 60]])
df_from_np = pd.DataFrame(np_array, columns=['Col1', 'Col2', 'Col3'])

print("Converted Pandas DataFrame:\n", df_from_np)


np_from_df = df_from_np.to_numpy()

print("\nConverted NumPy Array:\n", np_from_df)


# 🌟 Exercise 10 : Basic Visualization
# Instructions
# Use Matplotlib to visualize a simple dataset created with NumPy (e.g., a line graph of random numbers).

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 50)
np.random.seed(42)
y = np.sin(x) + np.random.normal(0, 0.1, 50)


plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Sine Wave + Noise', color='blue', marker='o', linestyle='-')
plt.title('Line Visualization Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()