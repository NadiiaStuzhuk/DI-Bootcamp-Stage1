# 🌟 Exercise 1: Random Sentence Generator
# Goal: Create a program that generates a random sentence of a specified length from a word list.



# Key Python Topics:

# File handling (open(), read())
# Lists
# Random number generation (random.choice())
# String manipulation (split(), join(), lower())
# Error handling (try, except)
# Input validation


# Instructions:

# Download the provided word list and save it in your development directory.
# Create a function to read the words from the file.
# Create a function to generate a random sentence of a given length.
# Create a main function to handle user input and program flow.


# Step 1: Create the get_words_from_file function

# Create a function named get_words_from_file that takes the file path as an argument.
# Open the file in read mode ("r").
# Read the file content.
# Split the content into a list of words.
# Return the list of words.


# Step 2: Create the get_random_sentence function

# Create a function named get_random_sentence that takes the sentence length as an argument.
# Call get_words_from_file to get the list of words.
# Select a random word from the list length times.
# Create a sentence with the selected words.
# Convert the sentence to lowercase.
# Return the sentence.


# Step 3: Create the main function

# Create a function named main.
# Print a message explaining the program’s purpose.
# Ask the user for the desired sentence length.
# Validate the user input:
# Check if it is an integer.
# Check if it is between 2 and 20 (inclusive).
# If the input is invalid, print an error message and exit.
# If the input is valid, call get_random_sentence with the length and print the generated sentence.


import random


def get_words_from_file(file_path):

    with open(file_path, "r") as f:
        content = f.read()
    return content.split()


def get_random_sentence(length):

    words = get_words_from_file("C:\\Users\\Nadiia Stuzhuk\\DI-Bootcamp-Stage1\\Week3\\Day6\\ExercisesXP\\words.txt")
    chosen = [random.choice(words) for _ in range(length)]
    return " ".join(chosen)

def main():
    try:
        length = int(input("Enter sentence length (between 2 and 20): "))
        if length < 2 or length > 20:
            print("Error: Length must be between 2 and 20.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    
    if length < 2 or length > 20:
        print("Please enter a number between 2 and 20.")
        return    
    sentence = get_random_sentence(length)
    print(f"Generated sentence: {sentence}")
    
main()




