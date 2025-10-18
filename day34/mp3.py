# ATM PIN Verification System

correct_pin = "1234"  # You can change this to any 4-digit PIN
attempts = 3  # Total allowed attempts

print("🔐 Welcome to the Secure Access System")

while attempts > 0:
    user_pin = input("Enter your 4-digit PIN: ")

    # Check if input is 4 digits
    if len(user_pin) != 4 or not user_pin.isdigit():
        print("❌ Invalid input! Please enter a 4-digit number.\n")
        continue

    # Check PIN correctness
    if user_pin == correct_pin:
        print("\n✅ Access Granted! Welcome!")
        break
    else:
        attempts -= 1
        print(f"❌ Incorrect PIN. Attempts remaining: {attempts}\n")

# If all attempts used up
if attempts == 0:
    print("🚫 Access Denied! Too many incorrect attempts.")
