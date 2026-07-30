import random


class Game:

    def get_user_item(self):
        """Asks the user to select an item with data validation.

        Keeps asking until a valid choice ('r', 'p', or 's') is entered.
        Returns the full name of the choice.
        """
        valid_choices = {
            "r": "rock",
            "p": "paper",
            "s": "scissors",
            "rock": "rock",
            "paper": "paper",
            "scissors": "scissors",
        }

        while True:
            user_input = (
                input("Select an item ((r)ock, (p)aper, or (s)cissors): ")
                .strip()
                .lower()
            )
            if user_input in valid_choices:
                return valid_choices[user_input]
            print(
                "Invalid input! Please enter 'rock' ('r'), 'paper' ('p'), or 'scissors' ('s').\n"
            )

    def get_computer_item(self):
        """Selects rock, paper, or scissors at random for the computer."""
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        """Determines the result of the game from the user's perspective.

        Returns 'draw', 'win', or 'loss'.
        """
        if user_item == computer_item:
            return "draw"


        winning_combos = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper",
        }

        if winning_combos[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        """Plays a single round of Rock, Paper, Scissors and prints the output.

        Returns 'win', 'draw', or 'loss'.
        """
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)


        if result == "win":
            outcome_text = "You win!"
        elif result == "loss":
            outcome_text = "You lose!"
        else:
            outcome_text = "You drew!"

        print(
            f"You selected {user_item}. The computer selected {computer_item}. {outcome_text}\n"
        )
        return result