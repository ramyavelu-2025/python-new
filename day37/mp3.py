# 🎓 Student Grades Manager using Tuples

# Step 1: Create tuples for student names and their grades
students = ("Ramya", "Karthik", "Priya", "Vijay", "Anu")
grades = (85, 92, 76, 88, 95)

while True:
    print("\n===== 🧾 STUDENT GRADE MANAGER =====")
    print("1. View All Students and Grades")
    print("2. View Highest, Lowest, and Average Grade")
    print("3. Access Student Grade by Index")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # 1️⃣ View all students and grades
    if choice == "1":
        print("\n📋 Student Grades:")
        for i in range(len(students)):
            print(f"{i}. {students[i]} — {grades[i]} marks")

    # 2️⃣ Show highest, lowest, and average grade
    elif choice == "2":
        highest = max(grades)
        lowest = min(grades)
        average = sum(grades) / len(grades)
        print("\n📊 Grade Summary:")
        print(f"Highest Grade : {highest}")
        print(f"Lowest Grade  : {lowest}")
        print(f"Average Grade : {average:.2f}")

    # 3️⃣ Access student grade by index
    elif choice == "3":
        try:
            index = int(input("Enter student index (0 to 4): "))
            print(f"{students[index]}'s Grade: {grades[index]}")
        except (ValueError, IndexError):
            print("❌ Invalid index! Please enter a number between 0 and 4.")

    # 4️⃣ Exit
    elif choice == "4":
        print("👋 Exiting Student Grade Manager. Goodbye!")
        break

    # Invalid input
    else:
        print("⚠️ Invalid choice! Please enter 1–4.")
