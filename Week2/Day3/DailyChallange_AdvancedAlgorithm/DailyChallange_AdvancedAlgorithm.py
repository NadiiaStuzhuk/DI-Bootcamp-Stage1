# What You will learn :
# Python Basics
# Conditionals
# Loops
# Functions


# Instructions
# Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.

# import random

# list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

# target_number   = 3728


# Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number

# For example

# 1000 and 2728 sums to the target_number 3728
# 1864 and 1864 sums to the target_number 3728


# One Last Thing: Good luck!


import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

def find_sum_pairs(numbers, target):
    seen_numbers = set()
    found_pairs = set() 

    for number in numbers:

        complement = target - number
        
        if complement in seen_numbers:
            
            pair = tuple(sorted((number, complement)))
            found_pairs.add(pair)
     
        seen_numbers.add(number)
        
    return found_pairs

pairs = find_sum_pairs(list_of_numbers, target_number)

print(f"Found {len(pairs)} unique pairs that sum up to {target_number}:\n")
for p in list(pairs)[:10]: 
    print(f"{p[0]} + {p[1]} = {target_number}")