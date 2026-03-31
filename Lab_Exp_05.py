1# This program generates Fibonacci numbers up to 1000 and calculates the sum of the even-valued terms.
fib = []
a, b = 0, 1

# Generate Fibonacci numbers up to 1000
while a <= 1000:
    fib.append(a)
    a, b = b, a + b

print("Fibonacci Series:", fib)

# Find sum of even values
sum_even = 0
for num in fib:
    if num % 2 == 0:
        sum_even += num

print("Sum of even-valued terms:", sum_even)

2# This program demonstrates how to loop through different collection types in Python, including lists, tuples, dictionaries, and sets.
# List
lst = [1, 2, 3, 4, 5]

# Tuple
tup = (10, 20, 30, 40, 50)

# Dictionary
d = {"name": "Radha", "roll": 278}

# Set
s = {1, 2, 3, 4, 5}

# Loop through list
for i in lst:
    print("List value:", i)

# Loop through tuple
for i in tup:
    print("Tuple value:", i)

# Loop through dictionary
for key, val in d.items():
    print("Dictionary:", key, ":", val)

# Loop through set
for i in s:
    print("Set value:", i)

3# This program converts a list of temperatures from Celsius to Fahrenheit using a loop.
celsius_list = [0, 10, 20, 30, 40]

fahrenheit = []

for c in celsius_list:
    f = (9/5) * c + 32
    fahrenheit.append(f)

print("Fahrenheit:", fahrenheit)

4# This program takes a list of numbers from the user, removes duplicates, and sorts the list in ascending order.
numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

# Remove duplicates and sort
unique_numbers = list(set(numbers))
unique_numbers.sort()

print("List after removing duplicates and sorting:")
print(unique_numbers)
