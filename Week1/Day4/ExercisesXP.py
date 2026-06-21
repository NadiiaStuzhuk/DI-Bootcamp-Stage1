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