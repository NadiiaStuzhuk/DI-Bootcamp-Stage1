
# from game import Game

# def get_user_menu_choice():
#     """Displays choices and captures user option routing flags."""
#     print("=== Main Menu ===")
#     print("1. Play a new game")
#     print("2. Show scores")
#     print("3. Quit")
    
#     choice = input("Enter option choice (1/2/3): ").strip()
#     return choice

# def print_results(results):
#     """Summarizes tracked game histories in clean key-value structures."""
#     print("\n===============================")
#     print("      FINAL GAME SUMMARY       ")
#     print("===============================")
#     print(f" Wins:   {results['win']}")
#     print(f" Losses: {results['loss']}")
#     print(f" Draws:  {results['draw']}")
#     print("===============================")
#     print("Thank you for playing! Goodbye.\n")

# def main():

#     results = {"win": 0, "loss": 0, "draw": 0}
    
#     print("Welcome to Rock, Paper, Scissors!\n")
    
#     while True:
#         choice = get_user_menu_choice()
        
#         if choice == "1":
        
#             current_game = Game()
#             result = current_game.play()
            
#             results[result] += 1
            
#         elif choice == "2":
#             print("\n--- Current Standings ---")
#             print(f"Wins: {results['win']} | Losses: {results['loss']} | Draws: {results['draw']}\n")
            
#         elif choice == "3":
#             print_results(results)
#             break
#         else:
#             print("\n[Invalid Selection] Please choose 1, 2, or 3.\n")

# if __name__ == "__main__":
#     main()

from game import Game


def get_user_menu_choice():
    """Displays the menu and gets a validated single choice from the user.

    Returns '1', '2', or '3'.
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
    """Controls the overall execution flow of the game."""

    results = {"win": 0, "loss": 0, "draw": 0}

    print("Welcome to Rock, Paper, Scissors!\n")

    while True:
        choice = get_user_menu_choice()

        if choice == "1":
        
            game_instance = Game()
            result = game_instance.play()
            results[result] += 1

        elif choice == "2":
        
            print_results(results)

        elif choice == "3":

            print_results(results)
            break


if __name__ == "__main__":
    main()