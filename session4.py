
"""Q1 : Define a variable x and assign it the value 5. Write a Python program that uses the and
logical operator to check if x is greater than 3 and less than 10. Print the result."""

x = 5
result = x > 3 , x < 10
print(result)

"""Q2 : Define two lists x and y, both containing the elements "apple" and "banana." Then, assign 
the reference of x to a variable z. Write a Python program that uses the is identity operator to check if 
x and z refer to the same object. Print the result. Next, use the is identity operator to check if x and y 
refer to the same object. Print the result."""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x == y)



"""Q3 : Define a list fruits containing the elements "apple," "banana," and "cherry." Write a 
Python program that uses the len() function to determine the number of items in the list and then 
prints the result. """

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

"""Q4 : Create a list fruits using the list() constructor with the elements "apple," "banana," and 
"cherry." Write a Python program that uses the list() constructor to create this list and then prints the 
resulting list. """

fruits = list(("apple", "banana", "cherry"))
print(fruits)

"""Q5 : Create a list colors using the list() constructor with the elements "red," "green," and 
"blue." Write a Python program that uses the list() constructor to create this list and then prints the 
resulting list. """

colors = list(("red", "green", "bleu"))
print(colors)

"""Q6 :  Define a list fruits containing the elements "apple," "banana," and "cherry." Write a 
Python program that prints the second item of the list. """

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

"""Q7 : Define a list numbers containing the integers from 1 to 10. Write a Python program that 
uses list slicing to print the elements from the 3rd to the 7th (inclusive) in the list.  """

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_numbers[2:8])

"""Q8 : Define a list numbers containing the integers from 1 to 10. Write a Python program that 
replaces the elements at even indices (0, 2, 4, etc.) with the corresponding square of that index. Then, 
print the modified list. """

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list_numbers[1::2]
print(even)