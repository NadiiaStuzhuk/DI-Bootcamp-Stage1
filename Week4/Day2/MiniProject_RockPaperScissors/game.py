import random


class Game:

    def get_user_item(self):
        """Asks the user to select an item with data validation.

        Keeps asking until a valid choice ('r', 'p', or 's') is entered.
        Returns the full name of the choice ('rock', 'paper', or 'scissors').
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

    from game import Game


def get_user_menu_choice():
    """Displays the menu, gets user input, and validates it.

    Returns '1', '2', or '3', or None if invalid.
    """
    print("=== Menu ===")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")

    choice = input("Enter your choice (1, 2, or 3): ").strip()
    if choice in ["1", "2", "3"]:
        return choice

    print("Invalid option! Please select 1, 2, or 3.\n")
    return None


def print_results(results):
    """Displays the game results summary in a user-friendly format."""
    print("\n=============================")
    print("         GAME SCORES         ")
    print("=============================")
    print(f"  Wins:   {results.get('win', 0)}")
    print(f"  Losses: {results.get('loss', 0)}")
    print(f"  Draws:  {results.get('draw', 0)}")
    print("=============================")
    print("Thank you for playing!\n")


def main():
    """Main program flow controller."""
    results = {"win": 0, "loss": 0, "draw": 0}

    print("Welcome to Rock, Paper, Scissors!\n")

    while True:
        choice = get_user_menu_choice()

        # Explicitly handle invalid choice returned by get_user_menu_choice()
        if choice is None:
            continue

        if choice == "1":
            # Play a new game
            game_instance = Game()
            result = game_instance.play()
            results[result] += 1

        elif choice == "2":
            # Show current scores and pause for better UX
            print_results(results)
            input("Press Enter to continue back to the menu...")
            print()

        elif choice == "3":
            # Display summary and exit
            print_results(results)
            break


if __name__ == "__main__":
    main()