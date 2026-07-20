
from game import Game

def get_user_menu_choice():
    """Displays choices and captures user option routing flags."""
    print("=== Main Menu ===")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    
    choice = input("Enter option choice (1/2/3): ").strip()
    return choice

def print_results(results):
    """Summarizes tracked game histories in clean key-value structures."""
    print("\n===============================")
    print("      FINAL GAME SUMMARY       ")
    print("===============================")
    print(f" Wins:   {results['win']}")
    print(f" Losses: {results['loss']}")
    print(f" Draws:  {results['draw']}")
    print("===============================")
    print("Thank you for playing! Goodbye.\n")

def main():

    results = {"win": 0, "loss": 0, "draw": 0}
    
    print("Welcome to Rock, Paper, Scissors!\n")
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == "1":
        
            current_game = Game()
            result = current_game.play()
            
            results[result] += 1
            
        elif choice == "2":
            print("\n--- Current Standings ---")
            print(f"Wins: {results['win']} | Losses: {results['loss']} | Draws: {results['draw']}\n")
            
        elif choice == "3":
            print_results(results)
            break
        else:
            print("\n[Invalid Selection] Please choose 1, 2, or 3.\n")

if __name__ == "__main__":
    main()