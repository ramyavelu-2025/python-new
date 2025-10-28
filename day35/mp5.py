# 🌍 Global variable to count total number of transactions
total_transactions = 0


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    # 🏧 Deposit method
    def deposit(self, amount):
        global total_transactions
        if amount > 0:
            self.balance += amount
            total_transactions += 1
            print(f"✅ {self.name} deposited ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("❌ Deposit amount must be positive.")

    # 💸 Withdraw method with inner function and lambda for fees
    def withdraw(self, amount):
        global total_transactions
        # Lambda function for transaction fee (2%)
        fee = (lambda amt: amt * 0.02)(amount)

        # Inner function to check if withdrawal is possible
        def can_withdraw():
            return self.balance >= (amount + fee)

        if can_withdraw():
            self.balance -= (amount + fee)
            total_transactions += 1
            print(f"💰 {self.name} withdrew ₹{amount} (Fee ₹{fee:.2f}). New Balance: ₹{self.balance:.2f}")
        else:
            print("❌ Insufficient funds for this withdrawal.")

    # 💵 Get balance
    def get_balance(self):
        print(f"📊 {self.name}'s Current Balance: ₹{self.balance:.2f}")
        return self.balance

    # 💡 Apply interest using a first-class function
    def apply_interest(self, interest_function):
        """
        interest_function: a function that takes balance and returns updated balance
        """
        old_balance = self.balance
        self.balance = interest_function(self.balance)
        print(f"📈 Interest Applied: ₹{self.balance - old_balance:.2f}, New Balance: ₹{self.balance:.2f}")


# ------------------------------------
# 📊 Demonstration Section
# ------------------------------------
if __name__ == "__main__":
    # Create two bank accounts
    acc1 = BankAccount("Ramya", 5000)
    acc2 = BankAccount("Karthik", 3000)

    # Perform some operations
    acc1.deposit(1500)
    acc1.withdraw(2000)
    acc1.get_balance()

    acc2.withdraw(3200)  # Should fail (insufficient funds)
    acc2.deposit(1000)
    acc2.withdraw(2500)

    # Apply interest using a first-class function
    def interest_rate(balance):
        return balance * 1.05  # 5% interest

    acc1.apply_interest(interest_rate)
    acc2.apply_interest(interest_rate)

    # Show global vs local variable example
    print(f"\n🌍 Total Transactions (Global Variable): {total_transactions}")
