# Simple Password Generator

# Step 1: Get user inputs
name = input("Enter your name: ").strip()
keyword = input("Enter a secret keyword: ").strip()

# Step 2: Generate password using string manipulations
part1 = name[:3].capitalize()          # First 3 letters of name
part2 = keyword[-3:].upper()           # Last 3 letters of keyword in uppercase
part3 = str(len(name) + len(keyword))  # Sum of lengths as a number
part4 = keyword[::-1][:2].lower()      # First 2 letters of reversed keyword
special_chars = "!@#"                   # Add some special characters

# Combine all parts to form the password
password = part1 + part2 + part3 + part4 + special_chars

# Step 3: Display the generated password
print("\n" + "="*50)
print("🔐 GENERATED PASSWORD".center(50))
print("="*50)
print(f"Name     : {name}")
print(f"Keyword  : {keyword}")
print(f"Password : {password}")
print("="*50)
