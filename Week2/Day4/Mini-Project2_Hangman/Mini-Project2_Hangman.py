
# What you will learn
# Conditionals
# Loops
# Functions
# Modules


# What you will create
# Use python to create a Hangman game.



# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.




import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 


HANGMAN_STAGES = [
    """
       --------
       |      |
       |      
       |     
       |      
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |     
       |      
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |     /|
       |      |
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |     
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |     / 
    - - - - -
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |     / \\
    - - - - -
    """
]

def display_game_state(word, guessed_letters, wrong_attempts):
  
    print(HANGMAN_STAGES[wrong_attempts])
    

    display_word = []
    for letter in word:
        if letter == " ":
            display_word.append(" ")
        elif letter in guessed_letters:
            display_word.append(letter)
        else:
            display_word.append("*")
            
    print("Word to guess: " + " ".join(display_word))
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Remaining lives: {6 - wrong_attempts}\n")
    

    return "".join(display_word)

def play_hangman():
    print("Welcome to Hangman!")
    
  
    guessed_letters = set()
    wrong_attempts = 0
    max_attempts = 6
    
    while wrong_attempts < max_attempts:
    
        current_display = display_game_state(word, guessed_letters, wrong_attempts)
        
   
        if "*" not in current_display:
            print("Congratulations! You saved the hangman and guessed the word!")
            return
            
        
        guess = input("Guess a letter: ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.\n")
            continue
            
        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try a different one.\n")
            continue
            
      
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Oops! '{guess}' is not in the word.")
            wrong_attempts += 1
            

    print(HANGMAN_STAGES[wrong_attempts])
    print(f"Game Over! You ran out of lives. The hidden word was: '{word}'")

play_hangman()