# Program to calculate discount based on total bill amount

# Ask user for the total bill amount
bill = float(input("Enter the total bill amount (₹): "))

# Apply discount based on conditions
if bill >= 5000:
    discount = bill * 0.20
elif bill >= 3000:
    discount = bill * 0.10
elif bill >= 1000:
    discount = bill * 0.05
else:
    discount = 0

# Calculate final amount after discount
final_amount = bill - discount

# Display the results
print("\n----- BILL SUMMARY -----")
print(f"Original Bill Amount : ₹{bill:.2f}")
print(f"Discount Applied     : ₹{discount:.2f}")
print(f"Final Amount to Pay  : ₹{final_amount:.2f}")
