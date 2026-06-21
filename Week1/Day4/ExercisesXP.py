# 🌟Exercise 1: Favorite Numbers
# Key Python Topics:
#Sets
# Adding/removing items in a set
# Set concatenation (using union)
# Instructions:
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.
my_fav_numbers = {3, 7, 21}
my_fav_numbers.add(5)
my_fav_numbers.add(13)
my_fav_numbers.remove(13)
friend_fav_numbers = {2, 8, 21}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)



# 🌟 Exercise 2: Tuple
# Key Python Topics:
# Tuples (immutability)
# Instructions:
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
print("Tuples are immutable, so we cannot add more integers to the tuple. You can only create a new tuple with the additional integers.")
tuple_of_integers = (1, 2, 3, 4, 5)
additional_tuple_integers = (6, 7, 8)
print(f"tuple_of_integers: {tuple_of_integers} and additional_tuple_integers: {additional_tuple_integers}")



# 🌟 Exercise 3: List Manipulation
# Key Python Topics:
# Lists
# List methods: append, remove, insert, count, clear
# Instructions:
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
basket.clear()
print(f"Final state of the list: {basket}")



# 🌟 Exercise 4: Floats
# Key Python Topics:
# Lists
# Floats and integers
# Range generation
# Instructions:
# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?
print("A float is a number that has a decimal point, while an integer is a whole number without a decimal point.")
mixed_numbers = [x * 0.5 for x in range(3, 11)]
print(f"List of mixed types (floats and integers): {mixed_numbers}")
print("This sequence could be generated using a loop or another method.")



# 🌟 Exercise 5: For Loop
# Key Python Topics:
# Loops (for)
# Range and indexing
# Instructions:
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.
for i in range(1, 21):
    print(i) 
for i in range(1, 21):
    if i % 2 == 0:
        print(i) 



# 🌟 Exercise 6: While Loop
# Key Python Topics:
# Loops (while)
# Conditionals
# Instructions:
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop
# Example:
# Enter your name: 1234
# Give the correct name: Hi
# Give the correct name: Ana
# Thank you
while True:
    input_name = input("Enter your name: ")
    if any(char.isdigit() for char in input_name) or len(input_name) < 3:
        print("Give the correct name:")
    else:
        print("Thank you")
        break




