FILENAME = "tasks.txt"

# Load tasks from the file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to the file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Show menu
def show_menu():
    print("\n--- TO-DO LIST APP ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Main program
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nYour Tasks:")
            if not tasks:
                print("No tasks available.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == "2":
            new_task = input("Enter a task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task added.")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                deleted = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Removed: {deleted}")
            else:
                print("Invalid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
