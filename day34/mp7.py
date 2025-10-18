# Triangle Pattern Generator

# Ask the user for number of rows
rows = int(input("Enter the number of rows for the triangle: "))

# Check for valid input
if rows <= 0:
    print("Please enter a positive number!")
else:
    print("\nTriangle Pattern:")
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()  # Move to the next line after each row
