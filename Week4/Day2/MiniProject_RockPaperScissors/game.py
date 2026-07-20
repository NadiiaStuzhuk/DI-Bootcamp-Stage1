
import random

class Game:
    def __init__(self):

        self.valid_items = ["rock", "paper", "scissors"]

    def get_user_item(self):
        """Asks the user to select an item, with validation loops."""
        while True:
            user_choice = input("Select an item (rock/paper/scissors): ").strip().lower()
            if user_choice in self.valid_items:
                return user_choice
            print("Invalid selection. Please type exactly 'rock', 'paper', or 'scissors'.")

    def get_computer_item(self):
        """Selects rock/paper/scissors at random for the computer."""
        return random.choice(self.valid_items)

    def get_game_result(self, user_item, computer_item):
        """Determines if the user gets a win, draw, or loss outcome."""
        if user_item == computer_item:
            return "draw"
        

        winning_moves = {
            "rock": "scissors", 
            "paper": "rock",    
            "scissors": "paper"
        }
        
        if winning_moves[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        """Executes a complete single round flow and tracks results."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        

        if result == "win":
            outcome_text = "You win!"
        elif result == "loss":
            outcome_text = "You lose."
        else:
            outcome_text = "You drew!"
            
        print(f"\nYou selected {user_item}. The computer selected {computer_item}. {outcome_text}\n")
        return result