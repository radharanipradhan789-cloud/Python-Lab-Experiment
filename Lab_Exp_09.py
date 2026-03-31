1# This program defines a function to add two numbers and then takes user input to display the result.
def add(a, b):
    return a + b
result = add(5, 10)
print("Sum =", result)

2# This program defines a function to calculate the product of two numbers and then calls the function with specific values to display the result.
def product(a, b):
    print("Product =", a * b)

product(4, 6)

4# This program demonstrates the use of keyword arguments in a function to display student details.
def Student(name, course):
    print("Name:", name)
    print("Course:", course)

Student(course="Python", name="Rani")

5# This program demonstrates the use of default arguments in a function to greet a person by name, with a default greeting for guests.
def greet(name="Guest"):
    print("Hello,", name)

6# This program demonstrates the use of default arguments in a function to display a bill amount, with a default value if no amount is provided.
def bill(amount=100):
    print("Bill Amount:", amount)

bill(500)   # Passed value overrides default
bill()      # Uses default value

8# This program demonstrates the use of arbitrary arguments in a function to calculate the sum of multiple numbers.
def total(*nums):
    print("Sum =", sum(nums))

total(10, 20, 30)
total(5, 15)

9# This program demonstrates the use of keyword arguments in a function to display employee details.
def employee(**details):
    # Loop through all keyword arguments
    for k, v in details.items():
        print(k, ":", v)

# Calling the function with keyword arguments
employee(name="Kindi", id=101, dept="IT")