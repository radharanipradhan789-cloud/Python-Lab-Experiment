1# This program demonstrates how to display a list of fruits from last to first,
# Original list of fruits
fruits = ["apple", "banana", "mango", "orange", "grapes"]

# Display original list
print("Original list:", fruits)

# Display elements from last to first
print("\nList from last to first:")
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i])

# Display length of each element
print("\nLength of each element:")
for fruit in fruits:
    print(f"{fruit} = {len(fruit)}")

# Create another list with reverse of each element
reverse_list = []
for fruit in fruits:
    reverse_list.append(fruit[::-1])

print("\nList with reverse of each element:")
print(reverse_list)

2# This program creates two dictionaries based on user input and then creates a new dictionary
# Create the first dictionary
dict1 = {}
n1 = int(input("Enter number of elements for the first dictionary: "))

for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

# Create the second dictionary
dict2 = {}
n2 = int(input("\nEnter number of elements for the second dictionary: "))

for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

# Display both dictionaries
print("\nFirst Dictionary:", dict1)
print("Second Dictionary:", dict2)

# Create new dictionary: values of dict1 as keys, values of dict2 as values
new_dict = {}
values1 = list(dict1.values())
values2 = list(dict2.values())
min_len = min(len(values1), len(values2))

for i in range(min_len):
    new_dict[values1[i]] = values2[i]

print("\nNew Dictionary (values of dict1 as keys, values of dict2 as values):")
print(new_dict)

3# This program demonstrates the use of the enumerate() function to display words in a sentence along with their index, and also combines two lists using the zip() function.
# Input sentence
sentence = input("Enter a sentence: ")  # Example: "Python is easy"

# Split sentence into words
list1 = sentence.split()
print("\nWords in the sentence:", list1)

# Display words with index using enumerate
print("\nWords with their index:")
for index, word in enumerate(list1):
    print(index, word)

# Create another list of numbers
list2 = list(range(1, len(list1)+1))  # e.g., [1, 2, 3, ...] for each word
print("\nList of numbers:", list2)

# Combine the two lists using zip
combined_list = list(zip(list1, list2))
print("\nCombined list using zip():", combined_list)