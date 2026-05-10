"""Q1: Define two lists, first_list and second_list, with the following content:
first_list contains the integers 1, 2, and 3.
second_list contains the strings "apple," "banana," and "cherry."
Write a Python program to append all the elements from second_list into first_list using a loop. After
the loop, print the combined first_list to see the result."""

first_list = [1, 2, 3]
second_list = ["apple", "banana", "cherry"]
for x in second_list:
        first_list.append(x)
print(first_list)

"""Q2: Define two tuples, first_tuple and second_tuple, with the following content:
first_tuple contains the integers 1, 2, and 3.
second_tuple contains the strings "apple," "banana," and "cherry."
Write a Python program to calculate and print the total number of items in both first_tuple and
second_tuple combined."""

first_tuple = (1, 2, 3)
second_tuple = ("apple", "banana", "cherry")
combined_tuple = first_tuple + second_tuple
print(len(combined_tuple))

"""Q3: Define a tuple named fruits containing the following elements: "apple," "banana,"
"cherry," "date," "elderberry," "fig," and "grape." Write a Python program to extract and print the
third, fourth, and fifth items from the fruits tuple using slicing."""

fruits = ("apple", "banana", "cherry", "date", "elderberry", "fig", "grape")
print(fruits[2:5])

"""Q4: Create a tuple named fruits containing the following elements: "apple," "banana,"
"cherry," "date," "elderberry," "fig," and "grape." Write a Python program to check if "apple" is
present in the fruits tuple. If it is, print "Yes, 'apple' is in the fruits tuple," otherwise, print "No, 'apple'
is not in the fruits tuple. """

fruits = ("apple", "banana", "cherry", "date", "elderberry", "fig", "grape")
if "apple" in fruits :
    print("Yes, 'apple' is in the fruits tuple. ")
else :
    print("No, 'apple'is not in the fruits tuple.") 

"""Q5: You have a tuple named fruits containing the elements "apple," "banana," and "cherry."
Write a Python program to convert this tuple into a list, change the second element to "kiwi," and
then convert it back to a tuple. Print the final tuple."""

fruits = ("apple", "banana", "cherry")
new_fruits = list(fruits)
new_fruits.insert(1,"kiwi")
fruits = tuple(new_fruits)
print(fruits)
