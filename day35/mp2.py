# To-Do List Manager using Recursion

tasks = []  # Global list to store tasks

def show_menu():
    print("\n=== 📝 To-Do List Manager ===")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    handle_choice(choice)

def handle_choice(choice):
    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("\n👋 Exiting To-Do List Manager. Goodbye!")
        return
    else:
        print("\n❌ Invalid choice! Please enter a number between 1 and 4.")
    
    # Recursive call to continue the menu
    show_menu()

def add_task():
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"✅ '{task}' added successfully!")

def remove_task():
    if not tasks:
        print("⚠️ No tasks to remove.")
        return
    display_tasks()
    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑️ Task '{removed}' removed successfully!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number.")

def display_tasks():
    if not tasks:
        print("⚠️ No tasks available.")
        return
    print("\n📋 Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Start the recursive menu
show_menu()
