1# This program calculates the value of 1/n for n from 2 to 100 and prints the results.
for i in range(2, 101):
    value = 1 / i
    print(f"1/{i} = {value}")

2# This program checks if a given number is prime or not.
num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
else:
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

3# This program calculates the greatest common divisor (GCD) of three numbers entered by the user.
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

g = gcd(gcd(a, b), c)

print("GCD =", g) 

4# This program calculates the sum of the digits of a positive integer entered by the user.
n = int(input("Enter a positive integer: "))

s = 0

while n > 0:
    digit = n % 10
    s += digit
    n //= 10

print("Sum of digits =", s)


