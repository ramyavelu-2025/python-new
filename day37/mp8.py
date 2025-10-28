# 🧺 Tuple Creation
cart = ("Milk", "Bread", "Eggs", "Butter", "Milk", "Cheese")

while True:
    print("\n=== Shopping Cart Menu ===")
    print("1. View all products")
    print("2. Add a new product")
    print("3. Remove a product")
    print("4. Count a specific product")
    print("5. Display first three items")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # 1️⃣ View all products
    if choice == "1":
        print("\n🛍️ Products in cart:")
        for item in cart:  # Tuple Iteration
            print("-", item)

    # 2️⃣ Add a new product
    elif choice == "2":
        new_product = input("Enter the product name to add: ")
        cart_list = list(cart)           # Convert tuple to list
        cart_list.append(new_product)    # Add product
        cart = tuple(cart_list)          # Convert back to tuple
        print(f"✅ '{new_product}' added successfully!")

    # 3️⃣ Remove a product
    elif choice == "3":
        remove_product = input("Enter the product name to remove: ")
        if remove_product in cart:
            cart_list = list(cart)
            cart_list.remove(remove_product)
            cart = tuple(cart_list)
            print(f"🗑️ '{remove_product}' removed successfully!")
        else:
            print(f"❌ '{remove_product}' not found in cart.")

    # 4️⃣ Count how many times a product appears
    elif choice == "4":
        product_name = input("Enter product name to count: ")
        count = cart.count(product_name)
        print(f"🔢 '{product_name}' appears {count} time(s) in the cart.")

    # 5️⃣ Display first three items (Tuple Slicing)
    elif choice == "5":
        print("\n📦 First three products:", cart[:3])

    # 6️⃣ Exit
    elif choice == "6":
        print("👋 Thank you for using the shopping cart system!")
        break

    else:
        print("⚠️ Invalid choice! Please try again.")
