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
    def __init__(self, text):
        """Step 1: Initialize the Text class with a string."""
        self.text = text

    def _get_clean_words(self):
        """Helper method to split text into lowercase words, ignoring punctuation."""
        # Lowercase and extract raw words using regular expressions
        return re.findall(r'\b\w+\b', self.text.lower())

    def word_frequency(self, word):
        """Step 2: Count occurrences of a specific word."""
        words = self._get_clean_words()
        target = word.lower()
        count = words.count(target)
        
        if count == 0:
            return f"The word '{word}' was not found in the text."
        return count

    def most_common_word(self):
        """Step 3: Find the word with the highest frequency using a dictionary."""
        words = self._get_clean_words()
        if not words:
            return "No words found in the text."
            
        frequencies = {}
        for w in words:
            frequencies[w] = frequencies.get(w, 0) + 1
            
        most_common = max(frequencies, key=frequencies.get)
        return most_common

    def unique_words(self):
        """Step 4: Use a set to return unique words as a list."""
        words = self._get_clean_words()
        return list(set(words))

    @classmethod
    def from_file(cls, file_path):
        """Step 5: Class method to open a file and return a Text instance."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            return cls(content)
        except FileNotFoundError:
            print(f"[Error] The file '{file_path}' could not be found.")
            return cls("")



class TextModification(Text):
    """Step 6: Class that inherits from Text to handle data cleaning."""
    
    def remove_punctuation(self):
        """Step 7: Remove punctuation characters using the string module."""

        translator = str.maketrans("", "", string.punctuation)
        cleaned_text = self.text.translate(translator)
        return cleaned_text

    def remove_stop_words(self):
        """Step 8: Filter out common English stop words."""
        stop_words = {
            "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", 
            "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", 
            "below", "between", "both", "but", "by", "can", "can't", "cannot", "could", 
            "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", 
            "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", 
            "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", 
            "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", 
            "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", 
            "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", 
            "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", 
            "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", 
            "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", 
            "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", 
            "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", 
            "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", 
            "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", 
            "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", 
            "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", 
            "you're", "you've", "your", "yours", "yourself", "yourselves"
        }
        
        words = self.text.split()
        filtered_words = [w for w in words if w.lower() not in stop_words]
        return " ".join(filtered_words)

    def remove_special_characters(self):
        """Step 9: Use regular expressions to keep only letters, numbers, and spaces."""
        cleaned_text = re.sub(r'[^a-zA-Z0-9 \n]', '', self.text)
        return cleaned_text


if __name__ == "__main__":
    sample_phrase = "The quick brown fox jumps over the lazy dog. The dog was not amused, really!"
    
    print("--- Part I: Analyzing a Simple String ---")
    analyzer = Text(sample_phrase)
    
    print(f"Frequency of 'dog': {analyzer.word_frequency('dog')}")
    print(f"Frequency of 'cat': {analyzer.word_frequency('cat')}")
    print(f"Most common word:    {analyzer.most_common_word()}")
    print(f"Unique words count:  {len(analyzer.unique_words())}")
    
    print("\n--- Part III: Text Modification (Bonus) ---")
    messy_phrase = "Hello World! @2026 #Python coding is awesome... right?"
    modifier = TextModification(messy_phrase)
    
    print(f"Original:           {messy_phrase}")
    print(f"No Punctuation:     {modifier.remove_punctuation()}")
    print(f"No Stop Words:      {modifier.remove_stop_words()}")
    print(f"No Special Chars:   {modifier.remove_special_characters()}")