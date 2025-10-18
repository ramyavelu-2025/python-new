# To-Do List Manager

tasks = []  # Empty list to store tasks

print("📝 Welcome to the To-Do List Manager!")
print("You can add, view, remove tasks, or type 'exit' to quit.\n")

while True:
    print("\nOptions: add | view | remove | exit")
    action = input("What would you like to do? ").lower()

    if action == "add":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ Task added: '{task}'")

    elif action == "view":
        if not tasks:
            print("📭 No tasks in your list.")
        else:
            print("\n🗒️ Your To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif action == "remove":
        if not tasks:
            print("⚠️ No tasks to remove.")
        else:
            print("\n🗒️ Your To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            try:
                num = int(input("Enter the task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed_task = tasks.pop(num - 1)
                    print(f"🗑️ Removed task: '{removed_task}'")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")

    elif action == "exit":
        print("👋 Exiting To-Do List Manager. Goodbye!")
        break

    else:
        print("❌ Invalid option. Please choose: add, view, remove, or exit.")
