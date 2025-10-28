# 🏪 Simple Inventory Management System using Tuples

# Step 1: Create tuples for items and prices
items = ("Laptop", "Mouse", "Keyboard", "Monitor", "Headphones")
prices = (55000, 800, 1500, 12000, 2000)

while True:
    print("\n===== 🧾 INVENTORY MANAGEMENT SYSTEM =====")
    print("1. View All Items and Prices")
    print("2. Search for an Item")
    print("3. Remove an Item from Inventory")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # 1️⃣ View all items and prices
    if choice == "1":
        print("\n📦 Available Inventory:")
        for i in range(len(items)):
            print(f"{i+1}. {items[i]} — ₹{prices[i]}")

    # 2️⃣ Search for a specific item
    elif choice == "2":
        search_item = input("Enter the item name to search: ").strip().title()
        if search_item in items:
            index = items.index(search_item)
            print(f"✅ {search_item} found! Price: ₹{prices[index]}")
        else:
            print("❌ Item not found in inventory.")

    # 3️⃣ Remove an item (by creating a new tuple)
    elif choice == "3":
        remove_item = input("Enter the item name to remove: ").strip().title()
        if remove_item in items:
            index = items.index(remove_item)
            # Reassigning a new tuple excluding the removed item
            items = items[:index] + items[index+1:]
            prices = prices[:index] + prices[index+1:]
            print(f"🗑️ {remove_item} removed successfully!")
        else:
            print("❌ Item not found in inventory.")

    # 4️⃣ Exit the program
    elif choice == "4":
        print("👋 Exiting Inventory Manager. Have a great day!")
        break

    # Invalid choice
    else:
        print("⚠️ Invalid choice! Please enter a number between 1–4.")
