# User Profile and Favorite Quote Display

# Take inputs from the user
full_name = input("Enter your full name: ").strip().title()  # Title-case formatting
age = input("Enter your age: ").strip()
favorite_quote = input("Enter your favorite quote: ").strip()

# Using string concatenation
intro_line = "Hello, " + full_name + "! Welcome to your profile."

# Using f-string for clean formatting
profile_info = f"""
============================================
          🌟 USER PROFILE CARD 🌟
============================================
👤 Name          : {full_name}
🎂 Age           : {age}
💬 Favorite Quote: "{favorite_quote}"
============================================
"""

# Using string method for emphasis
thank_you = "thank you for sharing your thoughts!".upper()

# Displaying the formatted output
print("\n" + intro_line)
print(profile_info)
print(thank_you)
