"""Q1: Define a list fruits containing the elements "apple," "banana," "cherry," "orange," "kiwi,"
"melon," and "mango." Write a Python program that uses list slicing with negative indices to print the
elements from "orange" to, but NOT including "mango." """

list_fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list_fruits[:-1])

"""Q2: Define a list fruits containing the elements "apple," "banana," and "cherry." Write a
Python program that checks if the string "apple" is present in the list. If it is, print "Yes, 'apple' is in
the fruits list. """

list_fruits = ["apple", "banana", "cherry"]
if "apple" in list_fruits :
    print("Yes, 'apple' is inthe fruits list.")

"""Q3: Define a list fruits containing the elements "apple," "banana," and "cherry." Write a
Python program that inserts the string "watermelon" as the third item in the list. Then, print the
modified list. """

list_fruits = ["apple", "banana", "cherry"]
list_fruits.insert(2,"watermelon")
print(list_fruits)


"""Q4: Define a list fruits containing the elements "apple," "banana," and "cherry." Write a
Python program that appends the string "orange" to the end of the list using the append() method.
Then, print the modified list. """

list_fruits = ["apple", "banana", "cherry"]
list_fruits.append("orange")
print(list_fruits)

"""Q5: Define a list numbers containing the integers from 1 to 10. Write a Python program that
creates two new lists:
even_numbers: Contains all even numbers from the numbers list.
odd_squares: Contains the squares of all odd numbers from the numbers list.
Then, print both the even_numbers and odd_squares lists. """

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list_numbers[1::2]
odd_squares = list_numbers[::2]
print("even_numbers:", even_numbers,"odd_squares:", odd_squares)



"""Q6: Define a list colors containing the elements "red," "green," "blue," "yellow," and
"orange." Write a Python program that repeatedly removes the last item from the colors list using the
pop() method until the list is empty. After each removal, print the modified colors list. """

colors = ["red", "green", "blue", "yellow", "orange"]
colors.pop()
print(colors)

"""Q7: Define a list colors containing the elements "red," "green," "blue," "yellow," and
"orange." Write a Python program that removes the first two items from the colors list using the del
statement and then prints the modified colors list. """

colors = ["red", "green", "blue", "yellow", "orange"]
del colors[0:2]
print(colors)

"""Q8: Define a list numbers containing the integers from 1 to 5. Write a Python program that
uses a for loop to calculate the square of each number in the numbers list and prints the result. """

list_numbers = [1, 2, 3, 4, 5]
for num in list_numbers:
    square = num**2
print(square)


"""Q9: Define a list numbers containing the integers from 1 to 5. Write a Python program that
uses a while loop to calculate the cube of each number in the numbers list and prints the result. """

list_numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(list_numbers):
    cube = list_numbers[i] ** 3
    print(cube)
    i += 1


"""Q10: Define a list numbers containing a mix of integers and floating-point numbers, such as [5,
1.2, 3, 0.5, 2.8, 4.7]. Write a Python program that sorts the numbers list in descending order (from
largest to smallest) and prints the sorted list. """

list_mix = [5,1.2, 3, 0.5, 2.8, 4.7]
list_mix.sort()
print(list_mix)


"""Q11: Define two lists, list1 and list2, with the following content:
list1 contains the integers from 1 to 5 (inclusive).
list2 contains the integers from 3 to 7 (inclusive).
Write a Python program that combines these two lists into a new list named combined_list, sorts
combined_list in ascending order, and then removes any duplicate elements from combined_list.
Finally, print the sorted and de-duplicated combined_list. """

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
combined_list = list1 + list2
combined_list = list(set(combined_list))
print(combined_list)



"""Q12: Define a list original_list containing the strings "apple," "banana," and "cherry." Write a
Python program that creates a copy of original_list using the copy() method and assigns it to a new list
named copied_list. Then, add a new element, "kiwi," to copied_list and print both original_list and
copied_list to see the differences. """

original_list = ["apple", "banana", "cherry"]
copied_list = original_list.copy()
copied_list.append("kiwi")
print(original_list)
print(copied_list)
