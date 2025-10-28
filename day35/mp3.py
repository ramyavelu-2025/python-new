# 1. Function that prints a greeting message
def greet_user():
    print("Hello, User!")

# 2. Function that returns the sum of two numbers
def calculate_sum(a, b):
    return a + b

# 3. Function that checks if a number is positive
def check_positive(num):
    if num > 0:
        return "Positive"
    else:
        pass  # Does nothing if number is not positive

# 4. Function that finds the maximum among three numbers
def find_max(a, b, c):
    return max(a, b, c)

# 5. Demonstrate global and local variables
count = 10  # Global variable
def modify_count():
    global count
    count += 5
    print("Inside function, count =", count)

# 6. Local variable scope demonstration
def modify_variable():
    message = "Local Scope"
    print("Inside function:", message)

# 7. Recursive function to find factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 8. Recursive function to find nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 9. Function with *args to sum multiple numbers
def sum_numbers(*args):
    return sum(args)

# 10. Function with **kwargs to print student details
def print_student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

# 11. Function that applies another function as an argument
def apply_operation(func, a, b):
    return func(a, b)

# 12. Function containing an inner function
def outer_function():
    def inner():
        return "Hello from Inner Function"
    return inner()

# 13. Using map() to double each element in a list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))

# -------------------------
# 📊 Demonstration Section
# -------------------------
if __name__ == "__main__":
    print("1.", end=" "); greet_user()
    print("2. Sum =", calculate_sum(5, 10))
    print("3.", check_positive(8))
    print("4. Max =", find_max(12, 45, 33))
    modify_count()
    print("5. Outside function, count =", count)
    modify_variable()
    try:
        print("Outside function:", message)  # Will cause NameError
    except NameError:
        print("6. Outside function: message not accessible (local scope only)")
    print("7. Factorial(5) =", factorial(5))
    print("8. Fibonacci(6) =", fibonacci(6))
    print("9. Sum of multiple numbers =", sum_numbers(2, 4, 6, 8))
    print("10. Student Details:")
    print_student_details(name="Ramya", age=20, grade="A")
    print("11. Apply Operation (lambda x+y):", apply_operation(lambda x, y: x + y, 7, 3))
    print("12.", outer_function())
    print("13. Doubled List:", doubled)
