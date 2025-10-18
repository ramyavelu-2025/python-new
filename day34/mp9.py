# Simple Banking System

balance = 10000  # Initial balance

print("🏦 Welcome to the Python Bank!")
print("Your starting balance is ₹10,000.")
print("Available options: deposit | withdraw | balance | quit\n")

while True:
    action = input("Enter your choice: ").lower()

    if action == "deposit":
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"✅ Deposited ₹{amount:.2f}")
        else:
            print("❌ Invalid amount. Please enter a positive value.")
        print(f"💰 Current Balance: ₹{balance:.2f}\n")

    elif action == "withdraw":
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("❌ Invalid amount. Please enter a positive value.")
        elif amount > balance:
            print("⚠️ Insufficient funds!")
        else:
            balance -= amount
            print(f"✅ Withdrawn ₹{amount:.2f}")
        print(f"💰 Current Balance: ₹{balance:.2f}\n")

    elif action == "balance":
        print(f"💰 Your current balance is ₹{balance:.2f}\n")

    elif action == "quit":
        print("👋 Thank you for banking with us! Have a great day!")
        break

    else:
        print("❌ Invalid option. Please choose: deposit, withdraw, balance, or quit.\n")


