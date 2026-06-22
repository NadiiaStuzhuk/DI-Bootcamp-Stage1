# 1. Ask the user for two inputs:

# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

# Example 1:
# Input:
# number: 7
# length: 5
# Output:
# [7, 14, 21, 28, 35]

number = int(input("Enter a number (integer): "))
length = int(input("Enter a length (integer): "))

multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)
print(multiples)
