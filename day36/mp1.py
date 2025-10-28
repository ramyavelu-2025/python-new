# Student Profile Card Generator

# Take inputs from user
name = input("Enter student's name: ")
age = input("Enter age: ")
course = input("Enter course name: ")
university = input("Enter university name: ")

# Display formatted profile card
print("\n" + "=" * 40)
print("🎓 STUDENT PROFILE CARD 🎓".center(40))
print("=" * 40)
print(f"👤 Name       : {name}")
print(f"🎂 Age        : {age}")
print(f"📚 Course     : {course}")
print(f"🏛️ University : {university}")
print("=" * 40)
