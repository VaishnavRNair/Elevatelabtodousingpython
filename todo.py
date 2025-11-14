import os

TASK_FILE = "tasks.txt"


# Load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return [task.strip() for task in file.readlines()]


# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Add a new task
def add_task(tasks):
    task = input("Enter task name: ").strip()
    if task == "":
        print("Task cannot be empty!")
        return
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
        return

    print("\n--- Your Tasks ---")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")


# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


# Main program (menu)
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Enter 1-4.")


if __name__ == "__main__":
    main()
