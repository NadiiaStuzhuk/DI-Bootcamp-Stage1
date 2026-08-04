# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# OOP (Classes, Class Methods, Inheritance)
# Modules (File Handling, String Manipulation, Data Structures)
# Text Analysis Techniques


# Key Python Topics:

# OOP (Classes, Class Methods, Inheritance)
# File handling (open())
# String manipulation (split(), join(), translate(), regular expressions)
# Dictionaries
# Sets
# Lists
# string module
# re module (regular expressions)


# Instructions:

# Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning.



# Part I: Analyzing a Simple String

# Step 1: Create the Text Class

# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g: self.text).


# Step 2: Implement word_frequency Method

# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.


# Step 3: Implement most_common_word Method

# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.


# Step 4: Implement unique_words Method

# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.


# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method

# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.


# Bonus: Text Modification

# Step 6: Create the TextModification Class

# Create a class called TextModification that inherits from Text.


# Step 7: Implement remove_punctuation Method

# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.


# Step 8: Implement remove_stop_words Method

# Create a method called remove_stop_words().
# Search online for a list of English stop words (common words like “a”, “the”, “is”).
# Split the text into a list of words.
# Filter out stop words from the list.
# Join the remaining words back into a string.
# Return the modified text.


# Step 9: Implement remove_special_characters Method

# Create a method called remove_special_characters().
# Use regular expressions to remove special characters from the text attribute.
# Return the modified text.


from collections import Counter
import re
import string


class Text:
    """Class to analyze text data from a string or file."""

    def __init__(self, text):
        self.text = text

    def _get_words(self):
        """Helper method to normalize and split text into a list of words."""
  
        return self.text.lower().split()

    def word_frequency(self, word):
        """Counts occurrences of a specific word in the text.

        Returns the count, or a message if the word is not found.
        """
        words = self._get_words()
        target_word = word.lower().strip()
        count = words.count(target_word)

        if count == 0:
            return f"The word '{word}' was not found in the text."
        return count

    def most_common_word(self):
        """Finds and returns the word with the highest frequency in the text."""
        words = self._get_words()
        if not words:
            return None

        word_counts = Counter(words)

        most_common, _ = word_counts.most_common(1)[0]
        return most_common

    def unique_words(self):
        """Returns a list of all unique words present in the text."""
        words = self._get_words()

        return list(set(words))

    @classmethod
    def from_file(cls, file_path):
        """Class method to instantiate a Text object by reading content from a file."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            return cls(content)
        except FileNotFoundError:
            print(f"Error: File at '{file_path}' was not found.")
            return None


class TextModification(Text):
    """Subclass of Text providing text cleaning and modification methods."""

    def remove_punctuation(self):
        """Removes all punctuation characters defined in string.punctuation."""
        # str.maketrans maps each punctuation character to None
        translator = str.maketrans("", "", string.punctuation)
        cleaned_text = self.text.translate(translator)
        return cleaned_text

    def remove_stop_words(self):
        """Removes common English stop words from the text attribute."""
        stop_words = {
            "a",
            "about",
            "above",
            "after",
            "again",
            "against",
            "all",
            "am",
            "an",
            "and",
            "any",
            "are",
            "aren't",
            "as",
            "at",
            "be",
            "because",
            "been",
            "before",
            "being",
            "below",
            "between",
            "both",
            "but",
            "by",
            "can't",
            "cannot",
            "could",
            "couldn't",
            "did",
            "didn't",
            "do",
            "does",
            "doesn't",
            "doing",
            "don't",
            "down",
            "during",
            "each",
            "few",
            "for",
            "from",
            "further",
            "had",
            "hadn't",
            "has",
            "hasn't",
            "have",
            "haven't",
            "having",
            "he",
            "he'd",
            "he'll",
            "he's",
            "her",
            "here",
            "here's",
            "hers",
            "herself",
            "him",
            "himself",
            "his",
            "how",
            "how's",
            "i",
            "i'd",
            "i'll",
            "i'm",
            "i've",
            "if",
            "in",
            "into",
            "is",
            "isn't",
            "it",
            "it's",
            "its",
            "itself",
            "let's",
            "me",
            "more",
            "most",
            "mustn't",
            "my",
            "myself",
            "no",
            "nor",
            "not",
            "of",
            "off",
            "on",
            "once",
            "only",
            "or",
            "other",
            "ought",
            "our",
            "ours",
            "ourselves",
            "out",
            "over",
            "own",
            "same",
            "shan't",
            "she",
            "she'd",
            "she'll",
            "she's",
            "should",
            "shouldn't",
            "so",
            "some",
            "such",
            "than",
            "that",
            "that's",
            "the",
            "their",
            "theirs",
            "them",
            "themselves",
            "then",
            "there",
            "there's",
            "these",
            "they",
            "they'd",
            "they'll",
            "they're",
            "they've",
            "this",
            "those",
            "through",
            "to",
            "too",
            "under",
            "until",
            "up",
            "very",
            "was",
            "wasn't",
            "we",
            "we'd",
            "we'll",
            "we're",
            "we've",
            "were",
            "weren't",
            "what",
            "what's",
            "when",
            "when's",
            "where",
            "where's",
            "which",
            "while",
            "who",
            "who's",
            "whom",
            "why",
            "why's",
            "with",
            "won't",
            "would",
            "wouldn't",
            "you",
            "you'd",
            "you'll",
            "you're",
            "you've",
            "your",
            "yours",
            "yourself",
            "yourselves",
        }

        words = self.text.split()
        filtered_words = [
            word for word in words if word.lower() not in stop_words
        ]
        return " ".join(filtered_words)

    def remove_special_characters(self):
        """Removes special characters (non-alphanumeric and non-whitespace) using regex."""
        # Replaces anything that is NOT a letter, number, or space with an empty string
        cleaned_text = re.sub(r"[^\w\s]", "", self.text)
        return cleaned_text



if __name__ == "__main__":
    sample_phrase = "A good book has no ending. A good book is a good friend!"

    print("=== Part I: Text Class Analysis ===")
    text_obj = Text(sample_phrase)

    print("Original Text:", text_obj.text)
    print("Frequency of 'good':", text_obj.word_frequency("good"))
    print("Frequency of 'python':", text_obj.word_frequency("python"))
    print("Most common word:", text_obj.most_common_word())
    print("Unique words count:", len(text_obj.unique_words()))

    print("\n=== Part II: Class Method (from_file) ===")

    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write("Hello world! Hello Python. Python is great and world is big.")

    file_text_obj = Text.from_file("sample.txt")
    if file_text_obj:
        print("File Content:", file_text_obj.text)
        print("Most common word in file:", file_text_obj.most_common_word())

    print("\n=== Bonus: TextModification Class ===")
    dirty_text = "Hello @World! This is an example, #python text with stop words & punctuation."
    mod_obj = TextModification(dirty_text)

    print("Original:", mod_obj.text)
    print("No Punctuation:", mod_obj.remove_punctuation())
    print("No Stop Words:", mod_obj.remove_stop_words())
    print("No Special Chars:", mod_obj.remove_special_characters())