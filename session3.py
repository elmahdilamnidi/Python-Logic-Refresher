
"""Q1 :Define a string variable quote and assign the following quote to it: "The best things in life 
are free!" Write a Python program that checks if the word "expensive" is not present in the quote 
using the not in keyword. If "expensive" is not present, print "No, 'expensive' is NOT present." 
Otherwise, do nothing. """

quote = "The best things in life are free!"
if "expensive" not in quote:
    print("No, 'expensive' is NOT present.")

"""Q2 :Define a string variable text and assign a sentence to it, for example, "Python 
programming is fun!" Write a Python program that prints the substring of text starting from the third 
character to the end. In other words, print all characters in text from the third character onward"""

text = "python programming is fun !"
print (text[2:])

"""Q3 : Define a string variable text and assign any sentence to it. Write a Python program that 
converts all the characters in text to uppercase using the upper() method and then prints the result."""

text = 'iam programmer'
print(text.upper())

"""Q4 :Define a string variable text and assign a sentence to it with leading and trailing 
whitespace, for example, " Python is great! ". Write a Python program that removes the leading and 
trailing whitespace from text using the strip() method and then prints the result."""

text = " Python is great! "
print(text.strip())

"""Q5 :Create a string variable sentence containing a sentence. Write a Python program that 
replaces all occurrences of the word "apple" with "orange" in the sentence using the replace() method 
and then prints the modified sentence."""

sentence = "i eat apple"
print(sentence.replace("apple" ,"orange"))

"""Q6 :Define three variables quantity, itemno, and price with appropriate values. Write a 
Python program that uses the format() method to create a string like "I want 3 pieces of item 567 for 
49.95 dollars." using these variables and then prints the result. """

quantity = 12
itemno = 390
price = 195.95
myorder = "I want {} pieces of item {} for {} dollars."

print(myorder.format(quantity, itemno, price))

"""Q7 : Define three variables quantity, itemno, and price with appropriate values. Write a 
Python program that uses the format() method with index numbers to create a string like "I want to 
pay 49.95 dollars for 3 pieces of item 567." using these variables and then prints the result. """

quantity = 12
itemno = 390
price = 195.95
myorder = "I want to pay {} dollars for {} pieces of item {}."

print(myorder.format(price, quantity, itemno))

"""Q8 : Define three variables quantity, itemno, and price with appropriate values. Write a 
Python program that uses the format() method to create a string like "I want 3 pieces of item number 
567 for 49.00 dollars." using these variables, with the price value formatted to two decimal places, 
and then prints the result."""

uantity = 12
itemno = 390
price = 195
myorder = "I want {} pieces of item {} for {:.2f} dollars."

print(myorder.format(quantity, itemno, price))

"""Q9 :You want to create a personalized message about your car. Define a string variable 
myorder with the value "I have a {carname}, it is a {model}." Use the format() method to replace 
{carname} with "Ford" and {model} with "Mustang". Write a Python program that accomplishes this 
and prints the personalized message. """

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford",model = "Mustang"))

"""Q10 : Define a string variable txt and assign it the following sentence: "We are the so-called 
"Vikings" from the north." Use either single quotes or escape characters to ensure that the double 
quotes around "Vikings" do not cause a syntax error. Write a Python program that prints the value of 
txt. """

txt = "We are the so-called \"Vikings\" from the north."
print(txt)