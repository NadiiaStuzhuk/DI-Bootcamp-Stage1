# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# OOP Concepts
# OOP Implementation (Classes, Methods)
# Data Structures (Lists)
# Random Number Generation


# Key Python Topics:

# OOP (Classes, Methods)
# Data Structures (Lists)
# Random Number Generation (random.shuffle())
# Instructions:



# Exercise 1: Quizz
# Answer the following questions:

# What is a class?
# What is an instance?
# What is encapsulation?
# What is abstraction?
# What is inheritance?
# What is multiple inheritance?
# What is polymorphism?
# What is method resolution order or MRO?

Exercise 1: OOP Concepts Quiz
1. What is a class?
A class is a blueprint or template for creating objects. It defines the attributes (data/properties) and methods (functions/behaviors) that objects created from it will possess.

2. What is an instance?
An instance is an individual object created from a specific class. While the class acts as the blueprint, an instance is the actual concrete entity created in memory (e.g., my_dog is an instance of the Dog class).

3. What is encapsulation?
Encapsulation is the practice of bundling data (attributes) and methods that operate on that data inside a single unit (a class), while restricting direct access to internal details from outside the class (often using private/protected variables like _ or __ in Python).

4. What is abstraction?
Abstraction means hiding complex underlying implementation details and exposing only essential interfaces to the user. This allows users to interact with an object without needing to understand how its internal logic works.

5. What is inheritance?
Inheritance is a mechanism where a new class (child/subclass) derives attributes and methods from an existing class (parent/superclass). It promotes code reuse and hierarchical relationships.

6. What is multiple inheritance?
Multiple inheritance occurs when a single subclass inherits directly from more than one parent class (e.g., class Smartphone(Camera, Phone) inherits features from both Camera and Phone).

7. What is polymorphism?
Polymorphism ("many forms") allows objects of different classes to respond to the exact same method call in their own specific ways (e.g., calling .speak() on a Dog outputs "Woof!", while on a Cat it outputs "Meow!").

8. What is Method Resolution Order (MRO)?
Method Resolution Order (MRO) is the deterministic order in which Python searches for a method or attribute across a class hierarchy, especially in complex multiple inheritance scenarios. Python uses the C3 Linearization algorithm to determine MRO, which can be inspected using ClassName.__mro__ or ClassName.mro().




# Exercise 2: Create a deck of cards class
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random

class Card:
    """Represents a single playing card with a suit and value."""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        """String representation of a card for friendly printing."""
        return f"{self.value} of {self.suit}"


class Deck:
    """Represents a deck of 52 playing cards. Does NOT inherit from Card."""
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):

        self.cards = []
        self._reset_deck()

    def _reset_deck(self):
        """Populates the deck with all 52 unique Card instances."""
        self.cards = [Card(suit, value) for suit in self.SUITS for value in self.VALUES]

    def shuffle(self):
        """
        Ensures the deck has all 52 cards, resets it if cards are missing,
        and rearranges them randomly.
        """
        if len(self.cards) != 52:
            print("Deck incomplete or cards were dealt. Resetting to 52 cards before shuffling...")
            self._reset_deck()
            
        random.shuffle(self.cards)
        print("Deck shuffled successfully!")

    def deal(self):
        """Deals (removes and returns) a single card from the top of the deck."""
        if not self.cards:
            print("No cards left in the deck to deal!")
            return None
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)


if __name__ == "__main__":
    deck = Deck()
    
    print(f"Initial deck size: {len(deck)} cards")
    deck.shuffle()
    
    dealt_card = deck.deal()
    print(f"Dealt card: {dealt_card}")
    print(f"Remaining cards in deck: {len(deck)}")  

    deck.shuffle()
    print(f"Deck size after re-shuffling: {len(deck)}")