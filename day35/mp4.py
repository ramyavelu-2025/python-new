from functools import reduce

# 1️⃣ Function to calculate average marks using *args
def calculate_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

# 2️⃣ Lambda + map() to convert marks to grades
def convert_to_grades(marks):
    # map each mark to a grade
    return list(map(lambda m: "A" if m >= 90 else
                              "B" if m >= 80 else
                              "C" if m >= 70 else "F", marks))

# 3️⃣ Filter function to find students who passed (grade != "F")
def get_passed_students(students):
    return list(filter(lambda s: s["grade"] != "F", students))

# 4️⃣ Use reduce() to find highest score among all students
def find_highest_score(students):
    if not students:
        return None
    return reduce(lambda a, b: a if a > b else b,
                  [s["marks"] for s in students])

# 5️⃣ Recursive function to print first n students’ details
def print_students_recursively(students, n, index=0):
    if index == n or index >= len(students):
        return
    s = students[index]
    print(f"Name: {s['name']}, Age: {s['age']}, Marks: {s['marks']}, Grade: {s['grade']}")
    print_students_recursively(students, n, index + 1)

# 6️⃣ Function using **kwargs to store student details dynamically
def create_student(**kwargs):
    return kwargs

# ------------------------------------
# 📊 Demonstration Section
# ------------------------------------
if __name__ == "__main__":
    # Create a few student records dynamically using **kwargs
    student1 = create_student(name="Ramya", age=20, marks=95)
    student2 = create_student(name="Karthik", age=21, marks=82)
    student3 = create_student(name="Meena", age=19, marks=67)
    student4 = create_student(name="Ajay", age=22, marks=74)
    students = [student1, student2, student3, student4]

    # Calculate grades using lambda + map
    marks_list = [s["marks"] for s in students]
    grades = convert_to_grades(marks_list)

    # Add grades to each student
    for i, s in enumerate(students):
        s["grade"] = grades[i]

    # Display average marks
    avg = calculate_average(*marks_list)
    print(f"\n📘 Class Average Marks: {avg:.2f}")

    # Show all students
    print("\n🎓 All Student Details:")
    print_students_recursively(students, len(students))

    # Filter passed students
    passed_students = get_passed_students(students)
    print("\n✅ Passed Students:")
    print_students_recursively(passed_students, len(passed_students))

    # Highest score using reduce
    highest = find_highest_score(students)
    print(f"\n🏆 Highest Marks in Class: {highest}")
