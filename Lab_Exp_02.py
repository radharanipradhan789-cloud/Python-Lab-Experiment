1# Simple Interest and Compound Interest Calculator
import math

from numpy import full

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate: "))
t = float(input("Enter the time: "))

# Simple Interest
si = (p * r * t) / 100

# Compound Interest
ci = p * (1 + r/100) ** t - p
print("Simple Interest:", si)
print("Compound Interest:", ci)

2# Calculate the area and perimeter of a circle
r = float(input("Enter the radius of the circle: "))
area = math.pi * r ** 2
perimeter = 2 * math.pi * r
print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)

print("My name is:", full)

3#creat a list of intializing with 5 different fruits and print the list 
fruits = ["apple", "banana", "mango", "lemon", "pineapple"]
print("List of fruits:", fruits)

4#Create a tuple with 4 different data types and print the tuple
t = (1, "aditi", "python", 89)
print("Tuple elements:", t)

5#Create a dictionary with 3 key-value pairs and print the keys, values, and key-value pairs
d = {
    "name": "Aditi",
    "roll": 93,
    "subject": "Python"
}

# Display keys
print("Keys:", d.keys())

# Display values
print("Values:", d.values())

# Display key-value pairs
for key, value in d.items():
    print(key, ":", value)

6#Write a program to reverse a string entered by the user and print the reversed string
sent = input("Enter your sentence: ")
print("Reversed sentence:", sent[::-1])

7#Create variables of different data types (integer, string, list, float, boolean) and print their values and types
i = 10
stn = "hello"
com = [2]
f = 3.14
b = True

print(i, type(i))
print(stn, type(stn))
print(com, type(com))
print(f, type(f))
print(b, type(b))

8#Write a program to demonstrate string manipulation by converting a string to uppercase, lowercase, and capitalized form, and also find the length of the string
stn = "hello world"
print("Upper case:", stn.upper())
print("Lower case:", stn.lower())
print("Capitalized:", stn.capitalize())
print("Length:", len(stn))

9#Write a program to demonstrate string slicing and splitting by reversing a sentence and splitting it into words
tn = "Good morning friends, how are you all"

# Reverse sentence
print("Reverse:", stn[::-1])

# Split into words
words = stn.split()
print("List of words:", words)

10#Write a program to demonstrate string manipulation by removing leading and trailing spaces, and replacing a substring with another substring in a given string
stn = " hi nam hi shyam hi mam "

# Remove leading & trailing spaces
stn = stn.strip()

# Replace "hi" with "Hello"
stn = stn.replace("hi", "Hello")

print("The sentence is:", stn)
