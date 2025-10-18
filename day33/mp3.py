a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
print("Remainder:", a % b)
#task2
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("First number is greater.")
elif a < b:
    print("First number is smaller.")
else:
    print("Both numbers are equal.")
#task3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, " b =", b)
#task 4
# Program to check if a year is a leap year

# Take input from user
year = int(input("Enter a year: "))

# Check leap year condition using modulus operator
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#task 5
# Ask the user for three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Determine the largest using comparison operators
if a >= b and a >= c:
    print(f"The largest number is {a}")
elif b >= a and b >= c:
    print(f"The largest number is {b}")
else:
    print(f"The largest number is {c}")

    #task6
    # Take radius as input
radius = float(input("Enter the radius of the circle: "))

# Calculate area using π * r² (use 3.14 for π)
area = 3.14 * radius ** 2

print(f"The area of the circle is {area}")
#task7
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#task8

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

#task9
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")

#task10
balance = 5000  # initial account balance

withdraw = float(input("Enter withdrawal amount: "))

if withdraw > balance:
    print("Insufficient funds.")
else:
    balance -= withdraw
    print(f"Withdrawal successful! Remaining balance: {balance}")


#task11
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by both 5 and 11.")
else:
    print("The number is not divisible by both 5 and 11.")

#task12
ch = input("Enter a single character: ").lower()

if ch in ('a', 'e', 'i', 'o', 'u'):
    print(f"{ch} is a vowel.")
else:
    print(f"{ch} is a consonant.")

#task13
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

