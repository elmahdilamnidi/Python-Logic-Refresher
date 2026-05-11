"""Q1: You have a tuple named numbers containing the elements 1, 2, 3, and 4. Create a new
tuple named squared that contains the squares of each element in the numbers tuple. Then, print the
squared tuple."""

numbers = (1, 2, 3, 4)
squared = tuple(n**2 for n in numbers)
print(squared)

"""Q2: You are working on a project that involves keeping track of temperatures in different
cities. You have a tuple named city_temperatures where each element represents the temperature in
Celsius for a specific city. Write a Python program to calculate the average temperature for all the
cities and store it in a variable named average_temp. Finally, print the value of average_temp."""





"""Q3: You are given two sets, set1 and set2. Write a Python program to find the number of
common elements between these two sets and store the count in a variable named common_count.
Finally, print the value of common_count."""

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
common_count = len(set1&set2)

print(common_count)

"""Q4: You are given a set named fruits. Write a Python program to check if the string "banana"
is present in the set. Print True if it's present and False if it's not."""

fruits = {"apple", "banana", "cherry"}
if "banana" in fruits:
    print(True)
else :
    print(False)

"""Q5: You are given two sets, set1 and set2, each containing integers. Write a Python program
to find and print the union of these two sets without using the built-in union operator (|).
Additionally, print the length of the resulting union set."""

set1 = {10, 20, 30}
set2 = {40, 50, 60}
result = set1.copy()

for i in set2 :
    result.add(i)

print(result)
print(len(result))

"""Q6: You are given a set named myset containing unique integers. Write a Python program that
repeatedly removes and prints the last item from the set using the pop() method until the set is
empty. Additionally, calculate and print the sum of all the removed items."""

