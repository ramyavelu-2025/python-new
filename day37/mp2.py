# 📝 Simple To-Do List Manager

# Step 1: Create an empty list to store tasks
tasks = []

while True:
    print("\n===== 🧾 TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Remove Task")
    print("4. View Pending Tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # 1️⃣ Add Task
    if choice == "1":
        task = input("Enter a new task: ").strip().capitalize()
        tasks.append({"task": task, "completed": False})
        print(f"✅ '{task}' added to your To-Do List.")

    # 2️⃣ Mark Task as Completed
    elif choice == "2":
        if not tasks:
            print("⚠️ No tasks available to mark.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                status = "✅" if t["completed"] else "❌"
                print(f"{i}. {t['task']} - {status}")
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index]["completed"] = True
                    print(f"🎯 Task '{tasks[index]['task']}' marked as completed!")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

    # 3️⃣ Remove Task
    elif choice == "3":
        if not tasks:
            print("⚠️ No tasks available to remove.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']}")
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    removed_task = tasks.pop(index)
                    print(f"🗑️ Task '{removed_task['task']}' removed successfully.")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

    # 4️⃣ View Pending Tasks
    elif choice == "4":
        if not tasks:
            print("🪶 Your To-Do List is empty.")
        else:
            print("\n📋 Pending Tasks:")
            for i, t in enumerate(tasks, start=1):
                if not t["completed"]:
                    print(f"{i}. {t['task']} - ❌ Pending")
            print("\n✅ Completed Tasks:")
            for i, t in enumerate(tasks, start=1):
                if t["completed"]:
                    print(f"{i}. {t['task']} - ✅ Done")

    # 5️⃣ Exit
    elif choice == "5":
        print("👋 Exiting To-Do List Manager. Have a productive day!")
        break

    # Invalid Option
    else:
        print("❌ Invalid choice! Please enter a number between 1-5.")
