#Exercise 1: Hello World
#Instructions
#Print the following output using one line of code:
from inspect import Traceback
print("Hello World\n"*4)


#Exercise 2: Some Math
#Instructions
#Write code that calculates the result of:
#(99^3)*8 (meaning 99 to the power of 3, times 8).

result = (99**3) * 8
print(result)
print("The result of (99**3) * 8 is", result,".")


#Exercise 3: What is the output?
#Instructions
#Predict the output of the following code snippets:
#Comment what is your guess, then run the code and compare
#Example:
#>>> 15 < 8 #False

5 < 3
False
3 == 3
True
3 == "3"
False
"3" > 3

#Exercise 4: Your computer brand
#Traceback (most recent call last):
#File "<python-input-55>", line 1, in <module>
#"3" > 3
#TypeError: '>' not supported between instances of 'str' and 'int'
#"Hello" == "hello"
#False
# Create the variable with your computer's brand
#computer_brand = "Apple"  # You can change "Apple" to "Dell", "HP", "Lenovo", etc.
# Print the sentence using an f-string
#print(f"I have a {computer_brand} computer.")
# Create a variable called computer_brand

computer_brand = "Lenovo"
print(f"I have a {computer_brand} computer.")