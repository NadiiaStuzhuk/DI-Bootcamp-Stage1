# What You Will Learn:
# Core NumPy operations including array creation, manipulation, and basic array operations.
# Skills in handling one-dimensional and multi-dimensional arrays.


# What You Will Create:
# A series of NumPy arrays demonstrating different operations, ranging from simple array creation to more complex manipulations.


# 🌟 Exercise 1 : Array Creation and Manipulation
# Instructions
# Create a 1D NumPy array containing numbers from 0 to 9.

# Expected Output:

# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

import numpy as np

arr = np.arange(10)
print(arr)

# 🌟 Exercise 2 : Type Conversion and Array Operations
# Instructions
# Convert a list [3.14, 2.17, 0, 1, 2] into a NumPy array and convert its data type to integer.

# Expected Output:

# array([3, 2, 0, 1, 2])

lst = [3.14, 2.17, 0, 1, 2]
arr_int = np.array(lst, dtype=int)

print(arr_int)

# 🌟 Exercise 3 : Working with Multi-Dimensional Arrays
# Instructions
# Create a 3x3 NumPy array with values ranging from 1 to 9.

# Expected Output:

# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])

arr_3x3 = np.arange(1, 10).reshape(3, 3)
print(arr_3x3)

# 🌟 Exercise 4 : Creating Multi-Dimensional Array with Random Numbers
# Instructions
# Create a 2D NumPy array of shape (4, 5) filled with random numbers.

# Expected Output:

# array([[0.56, 0.85, 0.01, 0.42, 0.68],
#        [0.22, 0.37, 0.73, 0.93, 0.39],
#        [0.44, 0.03, 0.87, 0.02, 0.83],
#        [0.78, 0.87, 0.98, 0.80, 0.46]])

random_arr = np.random.rand(4, 5)
print(random_arr)

# 🌟 Exercise 5 : Indexing Arrays
# Instructions
# Select the second row from a given 2D NumPy array.

# Expected Output:

# array = np.array([[21,22,23,22,22],[20, 21, 22, 23, 24],[21,22,23,22,22]])

array = np.array([[21, 22, 23, 22, 22], [20, 21, 22, 23, 24], [21, 22, 23, 22, 22]])

# Select row at index 1 (second row)
second_row = array[1]
print(second_row)

# 🌟 Exercise 6 : Reversing elements
# Instructions
# Reverse the order of elements in a given 1D NumPy array (first element becomes last).

# Expected Output:

# array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

arr = np.arange(10)
reversed_arr = arr[::-1]
print(reversed_arr)

# 🌟 Exercise 7 : Identity Matrix
# Instructions
# Create a 4x4 identity matrix using NumPy.

# Expected Output:

# array([[1., 0., 0., 0.],
#        [0., 1., 0., 0.],
#        [0., 0., 1., 0.],
#        [0., 0., 0., 1.]])

identity_mat = np.eye(4)
print(identity_mat)

# 🌟 Exercise 8 : Simple Aggregate Funcs
# Instructions
# Find the sum and average of a given 1D array.

# Expected Output:

# Sum: 45, Average: 4.5

arr = np.arange(10)

total_sum = np.sum(arr)
average_val = np.mean(arr)

print(f"Sum: {total_sum}, Average: {average_val}")

# 🌟 Exercise 9 : Create Array and Change its Structure
# Instructions
# Create a NumPy array with elements from 1 to 20; then reshape it into a 4x5 matrix.

# Expected Output:

# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20]])

reshaped_arr = np.arange(1, 21).reshape(4, 5)
print(reshaped_arr)

# 🌟 Exercise 10 : Conditional Selection of Values
# Instructions
# Extract all odd numbers from a given NumPy array.

# Expected Output:

# array([1, 3, 5, 7, 9])

arr = np.arange(10)

# Boolean masking to pick odd numbers
odd_numbers = arr[arr % 2 != 0]
print(odd_numbers)