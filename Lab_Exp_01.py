1# Print a welcome message to the user
print("welcome to python world")

2# Get user input for name, age, and address
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

print("my Name is :", name)
print("my Age is:", age)
print("my Address is:", address)

3# Calculate the area and perimeter of a circle
r = 5
pi = 3.14

area = pi * r * r
perimeter = 2 * pi * r

print("Area:", area)
print("Perimeter:", perimeter)

4# Calculate the sum and product of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

s = a + b
p = a * b

print("Sum:", s)
print("Product:", p)

5# Swap the values of two variables without using a third variable
a=10
b=20
a=a+b
b=a-b
a=a-b
print ("The number after swapping is:",a,b)

6#Swap the values of two variables using a temporary variable
a=10
b=20
print ("The number before swapping is :",a ,b)
temp =a
a =b 
b =temp
print ("The number after swapping is:",a,b)

7# Calculate the sum and percentage of marks obtained in three subjects
physics = 80
chemistry = 79
maths =90
sum_marks = physics + chemistry + maths
percentage = (sum_marks / 300) * 100

print("\n--- Marks Details ---")
print("Physics:", physics)
print("Chemistry:", chemistry)
print("Maths:", maths)
print("Sum:", sum_marks)
print("Percentage:", percentage)

8# Calculate the area and perimeter of a triangle using Heron's formula
import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

perimeter = a + b + c
s = perimeter / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("The perimeter of triangle:", perimeter)
print("The area of triangle:", area)



