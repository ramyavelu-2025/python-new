# Student Management System

students = []  # List to store student records

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks (out of 100): "))
    students.append({"name": name, "roll": roll, "marks": marks})
    print(f"\n✅ Student '{name}' added successfully!\n")

def display_students():
    if not students:
        print("\n⚠️ No students to display.\n")
        return
    print("\n📋 Student Details:")
    print("-" * 40)
    for s in students:
        print(f"Name: {s['name']}, Roll No: {s['roll']}, Marks: {s['marks']}")
    print("-" * 40)

def calculate_average():
    if not students:
        print("\n⚠️ No student data available.\n")
        return
    total = sum(s['marks'] for s in students)
    avg = total / len(students)
    print(f"\n📊 Class Average Marks: {avg:.2f}\n")

# Main Menu
while True:
    print("=== 🏫 Student Management System ===")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Calculate Average Marks")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        calculate_average()
    elif choice == '4':
        print("\n👋 Exiting Student Management System. Goodbye!")
        break
    else:
        print("\n❌ Invalid choice! Please enter a number between 1 and 4.\n")
