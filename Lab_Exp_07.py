1# This program performs various operations on a list of integers from 1 to n, including calculating the sum, average, largest and smallest values, and creating a new list of numbers that are not divisible by 3.
n = int(input("Enter the value of n: "))

list1 = []

for i in range(1, n + 1):
    list1.append(i)

total = 0
largest = list1[0]
smallest = list1[0]

for num in list1:
    total += num

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

average = total / n

list2 = []
for num in list1:
    if num % 3 != 0:
        list2.append(num)

print("First list:", list1)
print("Sum =", total)
print("Average =", average)
print("Largest =", largest)
print("Smallest =", smallest)
print("Second list (not divisible by 3):", list2)

2# This program takes two numbers as input and prints all prime numbers between them.
m = int(input("Enter starting number: "))
n = int(input("Enter ending number: "))

print("Prime numbers between", m, "and", n, "are:")

for num in range(m, n + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

3# This program takes a paragraph as input and performs the following operations:
import string

para = input("Enter a paragraph: ")

# Remove punctuation
for ch in string.punctuation:
    para = para.replace(ch, "")

# Split into words
words = para.split()

# Count words
word_count = len(words)

# Count palindrome words
pal_count = 0
for w in words:
    w = w.lower()
    if w == w[::-1] and len(w) > 1:
        pal_count += 1

# Print each word in reverse order
print("Each word in reverse order:")
for w in words:
    print(w[::-1])

# Output
print("\nTotal number of words:", word_count)
print("Number of palindrome words:", pal_count)