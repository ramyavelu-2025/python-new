# Number Pyramid Generator

rows = int(input("Enter number of rows for the pyramid: "))

if rows < 0:
    print("Invalid input. Exiting...")
else:
    print("\nNumber Pyramid:")
    for i in range(1, rows + 1):
        if i % 2 == 0:
            continue  # Skip even rows
        for j in range(i):
            print(i, end=" ")
        print()  # Move to next line after each row

