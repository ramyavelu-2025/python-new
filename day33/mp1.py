# Simple Calculator Program

# Take input from the user
num1 = float(input("Enter the first number: "))
operator = input("Enter operator (+, -, *, /, %): ")
num2 = float(input("Enter the second number: "))

# Perform operation based on operator
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
elif operator == '%':
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Error! Modulo by zero."
else:
    result = "Invalid operator!"

# Display the result
print(f"Result: {result}")
