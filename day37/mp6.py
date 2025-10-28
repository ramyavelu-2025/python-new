# Initialize an empty shopping cart
cart = []

# Function to add a product
def add_product(name, price):
    cart.append([name, price])
    print(f"✅ '{name}' added to the cart for ₹{price}.")

# Function to remove a product by name
def remove_product(name):
    for item in cart:
        if item[0].lower() == name.lower():
            cart.remove(item)
            print(f"🗑️ '{name}' removed from the cart.")
            return
    print(f"⚠️ '{name}' not found in the cart.")

# Function to view all items
def view_cart():
    if not cart:
        print("🛍️ Your cart is empty.")
    else:
        print("\n🛒 Items in your cart:")
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item[0]} - ₹{item[1]}")
        total_items = len(cart)
        total_price = sum([item[1] for item in cart])
        print(f"\nTotal Items: {total_items}")
        print(f"Total Price: ₹{total_price}\n")

# Function to display menu
def menu():
    print("\n==== SHOPPING CART MENU ====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Exit")
    print("============================")

# Main loop
while True:
    menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter product name: ")
        price = float(input("Enter product price: ₹"))
        add_product(name, price)

    elif choice == '2':
        name = input("Enter product name to remove: ")
        remove_product(name)

    elif choice == '3':
        view_cart()

    elif choice == '4':
        print("🛒 Thank you for shopping! Have a great day!")
        break

    else:
        print("❌ Invalid choice. Please select a valid option (1–4).")
