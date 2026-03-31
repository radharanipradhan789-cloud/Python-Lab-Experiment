1# Check if a string is a palindrome
s = input("Enter a string: ")

# Remove spaces and convert to lowercase
clean = s.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

2# Find the greatest among three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Greatest =", a)
elif b > a and b > c:
    print("Greatest =", b)
else:

    print("Greatest =", c)

4# Calculate percentage and grade based on marks for 5 subjects
marks = []

# Input marks for 5 subjects
for i in range(5):
    m = float(input(f"Enter marks for Subject {i+1} (0-50): "))
    
    if m < 0 or m > 50:
        print("Invalid marks! Should be between 0 and 50.")
        exit()
    
    marks.append(m)

# Calculate total and percentage
total = sum(marks)
percentage = (total / (5 * 50)) * 100

print("Percentage:", percentage)

# Grade calculation
if percentage >= 90:
    grade = "O"
elif percentage >= 80:
    grade = "E"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

5# Check if a letter is a vowel or consonant
ch = input("Enter a letter: ")

# Check valid input
if len(ch) != 1 or not ch.isalpha():
    print("Invalid input. Please enter a single alphabet.")
else:
    ch = ch.lower()
    
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("It is a vowel.")
    else:
        print("It is a consonant.")

6# Compare two strings for equality
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1 == str2:
    print("Both strings are equal.")
else:
    print("Strings are not equal.")