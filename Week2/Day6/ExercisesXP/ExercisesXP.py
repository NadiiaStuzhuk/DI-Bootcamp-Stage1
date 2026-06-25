# 🌟 Exercise 1: Converting Lists into Dictionaries
# Key Python Topics:

# Creating dictionaries
# Zip function or dictionary comprehension


# Instructions
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.


# Lists:
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# Expected Output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result_dict = dict(zip(keys, values))

print(result_dict)



# 🌟 Exercise 2: Cinemax #2
# Key Python Topics:

# Looping through dictionaries
# Conditionals
# Calculations

# Instructions
# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15


# Family Data:
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.

# Bonus:


family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

def calculate_tickets(family_data):
    total_cost = 0
    print("--- Ticket Breakdown ---")
   
    for name, age in family_data.items():
     
        if age < 3:
            price = 0
        elif 3 <= age <= 12:
            price = 10
        else:
            price = 15
            
        print(f"{name.title()}: ${price}")
        total_cost += price
        
    print("------------------------")
    print(f"Total Cost for the family: ${total_cost}\n")


calculate_tickets(family)

# BONUS SECTION 
print("--- Create Your Own Family Group ---")
custom_family = {}
while True:
    name = input("Enter family member's name (or type 'done' to finish): ").strip()
    if name.lower() == 'done':
        break
    
    try:
        age = int(input(f"Enter age for {name}: "))
        custom_family[name] = age
    except ValueError:
        print("Invalid age. Please enter a valid number.")

if custom_family:
    calculate_tickets(custom_family)
