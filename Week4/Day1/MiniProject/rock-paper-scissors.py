import Game


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


        if choice is None:
            continue

        if choice == "1":
        
            game_instance = Game()
            result = game_instance.play()
            results[result] += 1

        elif choice == "2":
    
            print_results(results)
            input("Press Enter to continue back to the menu...")
            print()

        elif choice == "3":
        
            print_results(results)
            break


if __name__ == "__main__":
    main()