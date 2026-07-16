# 🌟 Exercise 1: Pets
# Key Python Topics:

# Inheritance
# Class instantiation
# Lists
# Polymorphism


# Instructions:

# Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.
# See the example below, before diving in.



# Step 1: Create the Siamese Class

# Create a class called Siamese that inherits from the Cat class.
# You can add any specific attributes or methods for the Siamese breed, or leave it as is if there are no unique behaviors.


# Step 2: Create a List of Cat Instances

# Create a list called all_cats that contains instances of Bengal, Chartreux, and Siamese cats.
# Example: all_cats = [bengal_obj, chartreux_obj, siamese_obj]
# Give each cat a name and age.


# Step 3: Create a Pets Instance

# Create an instance of the Pets class called sara_pets, passing the all_cats list as an argument.


# Step 4: Take Cats for a Walk

# Call the walk() method on the sara_pets instance.
# This should print the result of calling the walk() method on each cat in the list.


# Example:

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# Step 1: Create the Siamese class

# Step 2: Create a list of cat instances

# Step 3: Create a Pets instance of the list of cat instances

# sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
# sara_pets.walk()




class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    pass  

bengal_obj = Bengal("Garfield", 3)
chartreux_obj = Chartreux("Felix", 5)
siamese_obj = Siamese("Luna", 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]


sara_pets = Pets(all_cats)


sara_pets.walk()


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
     
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
     
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        
      
        if self_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}!"
        elif other_power > self_power:
            return f"{other_dog.name} won the fight against {self.name}!"
        else:
            return f"It's a tie between {self.name} and {other_dog.name}!"


dog1 = Dog("Rex", age=3, weight=30)      # Speed: 30/3*10 = 100. Power: 100*30 = 3000
dog2 = Dog("Buddy", age=5, weight=25)    # Speed: 25/5*10 = 50.  Power: 50*25  = 1250
dog3 = Dog("Zeus", age=2, weight=45)     # Speed: 45/2*10 = 225. Power: 225*45 = 10125


print("--- Testing Bark ---")
print(dog1.bark())
print(dog2.bark())

print("\n--- Testing Run Speed ---")
print(f"{dog1.name}'s speed: {dog1.run_speed()}")
print(f"{dog2.name}'s speed: {dog2.run_speed()}")
print(f"{dog3.name}'s speed: {dog3.run_speed()}")

print("\n--- Testing Fight ---")

print(dog1.fight(dog2))

print(dog2.fight(dog3))

# 🌟 Exercise 3: Dogs Domesticated
# Goal: Create a PetDog class that inherits from Dog and adds training and tricks.



# Key Python Topics:

# Inheritance
# super() function
# *args
# Random module


# Instructions:

# Step 1: Import the Dog Class

# In a new Python file, import the Dog class from the previous exercise.


# Step 2: Create the PetDog Class

# Create a class called PetDog that inherits from the Dog class.
# Add a trained attribute to the __init__ method, with a default value of False.
# trained means that the dog is trained to do some tricks.
# Implement a train() method that prints the output of bark() and sets trained to True.
# Implement a play(*args) method that prints “<dog_names> all play together”.
# *args on this method is a list of dog instances.
# Implement a do_a_trick() method that prints a random trick if trained is True.
# Use this list for the ramdom tricks:
# tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
# Choose a random index from it each time the method is called.


# Step 3: Test PetDog Methods

# Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.


# Example:

# # In a new file
# # import the Dog class

# class PetDog(Dog):
#     def __init__(self, name, age, weight): <mark> no need to put the details in the function, you are giving the solution</mark>
#         super().__init__(name, age, weight)
#         self.trained = False

#     def train(self): <mark> no need to put the details in the function, you are giving the solution</mark>
#         print(self.bark())
#         self.trained = True

#     def play(self, *args):
#         # ... code to print play message ...

#     def do_a_trick(self): <mark> no need to put the details in the function, you are giving the solution</mark>
#         if self.trained:
#             tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
#             print(f"{self.name} {random.choice(tricks)}")

# # Test PetDog methods
# my_dog = PetDog("Fido", 2, 10)
# my_dog.train()
# my_dog.play("Buddy", "Max")
# my_dog.do_a_trick()

import random

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"


class PetDog(Dog):
    def __init__(self, name, age, weight):
    
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
    
        print(self.bark())
        self.trained = True

    def play(self, *args):
      
        dog_names = [other_dog.name for other_dog in args]
        
    
        all_names = [self.name] + dog_names
        names_string = ", ".join(all_names)
        
        print(f"{names_string} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll", 
                "stands on his back legs", 
                "shakes your hand", 
                "plays dead"
            ]
            
            chosen_trick = random.choice(tricks)
            print(f"{self.name} {chosen_trick}")
        else:
            print(f"{self.name} is not trained yet and stares at you blankly.")


my_dog = PetDog("Fido", age=2, weight=12)

friend1 = PetDog("Buddy", age=4, weight=20)
friend2 = PetDog("Max", age=3, weight=15)

print("--- Testing play() ---")

my_dog.play(friend1, friend2)

print("\n--- Testing do_a_trick() before training ---")
my_dog.do_a_trick()

print("\n--- Testing train() ---")
my_dog.train()

print("\n--- Testing do_a_trick() after training ---")
my_dog.do_a_trick()
my_dog.do_a_trick() 



# 🌟 Exercise 4: Family and Person Classes
# Goal:

# Practice working with classes and object interactions by modeling a family and its members.



# Key Python Topics:

# Classes and objects
# Instance methods
# Object interaction
# Lists and loops
# Conditional statements (if/else)
# String formatting (f-strings)


# Instructions:

# Step 1: Create the Person Class

# Define a Person class with the following attributes:
# first_name
# age
# last_name (string, should be initialized as an empty string)
# Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.


# Step 2: Create the Family Class

# Define a Family class with:
# A last_name attribute
# A members list that will store Person objects (should be initialized as an empty list)


# Add a method called born(first_name, age):
# It should create a new Person object with the given first name and age.
# It should assign the family’s last name to the person.
# It should add this new person to the members list.


# Add a method called check_majority(first_name):
# It should search the members list for a person with that first_name.
# If the person exists, call their is_18() method.
# If the person is over 18, print:
# "You are over 18, your parents Jane and John accept that you will go out with your friends"
# Otherwise, print:
# "Sorry, you are not allowed to go out with your friends."


# Add a method called family_presentation():
# It should print the family’s last name.
# Then, it should print each family member’s first name and age.


# Expected Behavior:

# Once implemented, your program should allow you to:

# Create a family with a last name.
# Add members to the family using the born() method.
# Use check_majority() to see if someone is allowed to go out.
# Display family information with family_presentation().
# Don’t forget to test your classes by creating an instance of Family, adding members, and calling each method to see the expected output.


class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
      
        return self.age >= 18



class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
    
        new_person = Person(first_name, age)
    
        new_person.last_name = self.last_name
      
        self.members.append(new_person)
        print(f"Congratulations! {first_name} {self.last_name} was added to the family.")

    def check_majority(self, first_name):
        
        for person in self.members:
            if person.first_name == first_name:
                
                if person.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        
    
        print(f"No family member named {first_name} was found.")

    def family_presentation(self):
        print(f"\n--- The {self.last_name} Family Presentation ---")
        for person in self.members:
            print(f"Name: {person.first_name} {person.last_name} | Age: {person.age}")



my_family = Family("Smith")


my_family.born("Jane", 42)
my_family.born("John", 44)
my_family.born("David", 20)
my_family.born("Lily", 15)


my_family.family_presentation()

print("\n--- Testing Majority Checks ---")

print("Checking David:")
my_family.check_majority("David")

print("\nChecking Lily:")
my_family.check_majority("Lily")