# Student Grade Manager

# Step 1: Create two lists — one for student names and one for grades
students = []
grades = []

# Step 2: Define a menu-driven system
while True:
    print("\n===== 🏫 STUDENT GRADE MANAGER =====")
    print("1. Add New Student")
    print("2. Update Student Grade")
    print("3. Remove Student")
    print("4. Display All Students and Grades")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    # 1️⃣ Add new student
    if choice == "1":
        name = input("Enter student name: ").strip().title()
        grade = input("Enter student grade: ").strip()
        students.append(name)
        grades.append(grade)
        print(f"✅ {name} added successfully!")

    # 2️⃣ Update student grade
    elif choice == "2":
        name = input("Enter student name to update: ").strip().title()
        if name in students:
            index = students.index(name)
            new_grade = input("Enter new grade: ").strip()
            grades[index] = new_grade
            print(f"🔄 Grade updated for {name}.")
        else:
            print("❌ Student not found!")

    # 3️⃣ Remove student
    elif choice == "3":
        name = input("Enter student name to remove: ").strip().title()
        if name in students:
            index = students.index(name)
            students.pop(index)
            grades.pop(index)
            print(f"🗑️ {name} removed successfully.")
        else:
            print("❌ Student not found!")

    # 4️⃣ Display all students and grades
    elif choice == "4":
        if students:
            print("\n📋 STUDENT LIST:")
            print("-" * 30)
            for i in range(len(students)):
                print(f"{i+1}. {students[i]} — Grade: {grades[i]}")
            print("-" * 30)
        else:
            print("⚠️ No students available.")

    # 5️⃣ Exit
    elif choice == "5":
        print("👋 Exiting program. Goodbye!")
        break

    # Invalid input
    else:
        print("❌ Invalid choice! Please enter 1-5.")
