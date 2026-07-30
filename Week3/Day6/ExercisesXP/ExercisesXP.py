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


# import random


# def get_words_from_file(file_path):

#     with open(file_path, "r") as f:
#         content = f.read()
#     return content.split()


# def get_random_sentence(length):

#     words = get_words_from_file("C:\\Users\\Nadiia Stuzhuk\\DI-Bootcamp-Stage1\\Week3\\Day6\\ExercisesXP\\words.txt")
#     chosen = [random.choice(words) for _ in range(length)]
#     return " ".join(chosen)

# def main():
#     try:
#         length = int(input("Enter sentence length (between 2 and 20): "))
#         if length < 2 or length > 20:
#             print("Error: Length must be between 2 and 20.")
#             return
#     except ValueError:
#         print("Invalid input! Please enter a number.")
#         return
    
#     if length < 2 or length > 20:
#         print("Please enter a number between 2 and 20.")
#         return    
#     sentence = get_random_sentence(length)
#     print(f"Generated sentence: {sentence}")
    
# main()


import random


def get_words_from_file(file_path):
    """
    Opens a file, reads its content, splits it into words, and returns the list.
    """
    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split()
            return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []


def get_random_sentence(length, file_path="words.txt"):
    """
    Generates a sentence of a given length using random words from the word list.
    """
    words = get_words_from_file(file_path)
    

    if not words:
        return "Could not generate sentence due to missing word list."
    

    selected_words = []
    for _ in range(length):
        selected_words.append(random.choice(words))


    sentence = " ".join(selected_words).lower()
    return sentence


def main():
    """
    Handles user interaction, input validation, and output.
    """
    print("--- Random Sentence Generator ---")
    print("This program generates a random sentence of a specified length using a word list file.\n")
    
    user_input = input("Enter the desired sentence length (between 2 and 20): ")
    

    try:
        length = int(user_input)
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")
        return

    if length < 2 or length > 20:
        print("Error: The sentence length must be between 2 and 20 (inclusive).")
        return


    sentence = get_random_sentence(length)
    print("\nGenerated Sentence:")
    print(sentence)


if __name__ == "__main__":
    main()




# 🌟 Exercise 2: Working with JSON
# Goal: Access a nested key in a JSON string, add a new key, and save the modified JSON to a file.



# Key Python Topics:

# JSON parsing (json.loads())
# JSON serialization (json.dump())
# Dictionaries
# File handling (open())


# Instructions:

# Using the follow code:

# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"


# Access the nested “salary” key.
# Add a new key “birth_date” wich value is of format “YYYY-MM-DD”, to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Save the modified JSON to a file.


# Step 1: Load the JSON string

# Import the json module.
# Use json.loads() to parse the JSON string into a Python dictionary.


# Step 2: Access the nested “salary” key

# Access the “salary” key using nested dictionary access (e.g., data["company"]["employee"]["payable"]["salary"]).
# Print the value of the “salary” key.


# Step 3: Add the “birth_date” key

# Add a new key-value pair to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Replace "YYYY-MM-DD" with an actual date.


# Step 4: Save the JSON to a file

# Open a file in write mode ("w").
# Use json.dump() to write the modified dictionary to the file in JSON format.
# Use the indent parameter to make the JSON file more readable.


import json


sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data = json.loads(sampleJson)


salary = data["company"]["employee"]["payable"]["salary"]
print(f"Salary: {salary}")


data["company"]["employee"]["birth_date"] = "1995-04-12"


file_path = "modified_employee.json"
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print(f"Successfully updated JSON and saved to '{file_path}'.")