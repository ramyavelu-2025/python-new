# Student Management System

def display_menu():
    print("\n=== Student Management System ===")
    print("1. Add a new student")
    print("2. Remove a student")
    print("3. Update a student's name")
    print("4. Display all students")
    print("5. Exit")

def add_student(students):
    name = input("Enter student name to add: ").strip()
    if name:
        students.append(name)
        print(f"✅ '{name}' has been added.")
    else:
        print("⚠️ Name cannot be empty.")

def remove_student(students):
    name = input("Enter student name to remove: ").strip()
    if name in students:
        students.remove(name)
        print(f"✅ '{name}' has been removed.")
    else:
        print("⚠️ Student not found.")

def update_student(students):
    old_name = input("Enter current student name: ").strip()
    if old_name in students:
        new_name = input("Enter new student name: ").strip()
        if new_name:
            index = students.index(old_name)
            students[index] = new_name
            print(f"✅ '{old_name}' has been updated to '{new_name}'.")
        else:
            print("⚠️ New name cannot be empty.")
    else:
        print("⚠️ Student not found.")

def display_students(students):
    if students:
        print("\n📋 List of Students:")
        for i, name in enumerate(students, start=1):
            print(f"{i}. {name}")
    else:
        print("\n⚠️ No students in the list.")

# Main program loop
def main():
    students = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            remove_student(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            display_students(students)
        elif choice == '5':
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
