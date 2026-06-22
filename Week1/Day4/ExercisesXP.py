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




# 🌟 Exercise 7: Favorite Fruits
# Key Python Topics:
# Input/output
# Strings and lists
# Conditionals
# Instructions:
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

favorite_fruits_input = input("Please enter your favorite fruits, separated by spaces: ")
favorite_fruits = favorite_fruits_input.split()
fruit_to_check = input("Please enter the name of any fruit: ")
if fruit_to_check in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")



    # 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:
#
# Loops
# Lists
# String formatting
# Instructions:
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.
toppings = []
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")
total_cost = 10 + len(toppings) * 2.5
print(f"Your pizza has the following toppings: {', '.join(toppings)}.")     
print(f"Total cost: ${total_cost:.2f}")



# 🌟 Exercise 9: Cinemax Tickets
# Key Python Topics:
# Conditionals
# Lists
# Loops
# Instructions:
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

# Bonus:
# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.


ages = []
while True:
    age_input = input("Enter the age of a family member (or type 'done' to finish): ")
    if age_input.lower() == 'done':
        break
    try:
        age = int(age_input)
        ages.append(age)
    except ValueError:
        print("Please enter a valid number.")

total_cost = 0
for age in ages:
    if age < 3:
        total_cost += 0
    elif 3 <= age <= 12:
        total_cost += 10
    else:
        total_cost += 15

print(f"Total ticket cost: ${total_cost}")

allowed_attendees = [age for age in ages if 16 <= age <= 21]
print(f"Final list of attendees for the restricted movie: {allowed_attendees}")




