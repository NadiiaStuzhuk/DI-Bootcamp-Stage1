from anagram_checker import AnagramChecker


def validate_input(user_input):
    """Validates that user input is a single word containing only alphabetic characters.

    Returns the cleaned word if valid, or raises a ValueError with an appropriate message.
    """
    cleaned_input = user_input.strip()


    if not cleaned_input:
        raise ValueError("Error: Input cannot be empty.")


    words = cleaned_input.split()
    if len(words) > 1:
        raise ValueError("Error: Only a single word is allowed. You entered multiple words.")


    if not cleaned_input.isalpha():
        raise ValueError("Error: Only alphabetic characters (letters) are allowed. No numbers or symbols.")

    return cleaned_input


def show_menu():
    """Displays the main menu and prompts user for choice."""
    print("\n===============================")
    print("      ANAGRAM CHECKER MENU     ")
    print("===============================")
    print("1. Input a word to check")
    print("2. Exit")
    return input("Choose an option (1 or 2): ").strip()


def main():
    """Main application loop."""

    checker = AnagramChecker("sowpods.txt")

    print("Welcome to the Anagram Checker!")

    while True:
        choice = show_menu()

        if choice == "1":
            raw_word = input("\nEnter a single word: ")


            try:
                valid_word = validate_input(raw_word)
            except ValueError as error:
                print(f"\n❌ {error}")
                continue


            upper_word = valid_word.upper()
            is_valid = checker.is_valid_word(valid_word)

            print("\n-------------------------------")
            print(f'YOUR WORD : "{upper_word}"')

            if is_valid:
                print("This is a valid English word.")
                anagrams = checker.get_anagrams(valid_word)

                if anagrams:
                    anagram_list_str = ", ".join(anagrams)
                    print(f"Anagrams for your word: {anagram_list_str}.")
                else:
                    print("No anagrams found for your word.")
            else:
                print("This is NOT a valid English word according to the dictionary.")
            print("-------------------------------")

        elif choice == "2":
            print("\nThank you for using Anagram Checker! Goodbye! 👋\n")
            break
        else:
            print("\n❌ Invalid choice! Please enter '1' or '2'.")


if __name__ == "__main__":
    main()