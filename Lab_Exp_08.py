1# This program defines a function to calculate the square of a number and then takes user input to display the result.
def square(n):
    return n * n

num = int(input("Enter a number: "))
print("Square =", square(num))

2# This program defines a function to determine if a number is even or odd, and then takes user input to display the result.
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(even_odd(num))

3# This program defines a function to add two numbers and then takes user input to display the result.
def add(a, b):
    return a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum =", add(x, y))

4# This program defines a function to calculate the factorial of a number and then takes user input to display the result.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

5# This program defines a function to check if a number is prime and then takes user input to display the result.
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")

6# This program defines a function to reverse a string and then takes user input to display the result.
def reverse_string(s):
    return s[::-1]

text = input("Enter a string: ")
print(reverse_string(text))  

7# This program defines a function to count the number of vowels in a given string and then takes user input to display the result.
def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":
            count += 1
    return count

text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))

8# This program defines a function to calculate simple interest and then takes user input to display the result.
def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

si = simple_interest(p, r, t)

print("Simple Interest =", si)
