
"""Q1 :Create a list named temperatures containing five float values representing temperatures 
in Celsius. Write Python code to convert these temperatures to Fahrenheit using the formula: 
Fahrenheit = (Celsius * 9/5) + 32. Print the converted temperatures.  """

temperatures = [0.0, 25.0, 37.0, 100.0, -10.0]
fahrenheit_temperatures = [(celsius * 9/5) + 32 for celsius in temperatures]
print("Celsius temperatures:", temperatures)
print("Fahrenheit temperatures:", fahrenheit_temperatures)

"""Q2 :Define a complex number c1 with a real part of 2.5 and an imaginary part of -3.7. Create 
another complex number c2 with a real part of 1.8 and an imaginary part of 4.6. Write Python code to 
add these two complex numbers and print the result. """

c1 = 2.5 - 3.7j
c2 = 1.8 + 4.6j
result = c1 + c2
print("The result is:", result)

"""Q3 : Write a Python program to generate and print a random integer between 1 and 100 
(inclusive). """

import random
number = random.randint(1, 100)
print("Random integer between 1 and 100:", number)

"""Q4 : Write a Python program to print the first character of a given string text.  """

text = "hello world"
first_character = text[0]
print("The first character of the string is:", first_character)

"""Q5 :Write a Python program that takes a user input string and prints its length using the len() 
function."""

user_input = input("Enter a string: ")
length_of_string = len(user_input)
print("The length of the string is:", length_of_string)

"""Q6 :Define a string variable sentence and assign a sentence to it. Write a Python program that 
checks if the word "life" is present in the sentence using the in keyword. Print "Found" if it's present, 
otherwise print "Not found." """

sentence = "Life is beautiful."
if "life" in sentence.lower():
    print("Found")
else:
    print("Not found.")

"""Q7 :Define a string variable email and assign an email address to it. Write a Python program 
that checks if the email address contains the "@" symbol using the in keyword. Print "Valid email 
address" if it's present, otherwise print "Invalid email address." """

email = "user@example.com"
if "@" in email:
    print("Valid email address")
else:
    print("Invalid email address.")