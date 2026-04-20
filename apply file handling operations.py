FILE_NAME = "tasks.txt"

def add_task():
    task_id = input("Enter Task ID: ")
    desc = input("Enter Description: ")
    status = "Pending"

    with open(FILE_NAME, "a") as f:
        f.write(f"{task_id}|{desc}|{status}\n")

    print("Task added successfully!\n")


def view_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            tasks = f.readlines()

            if not tasks:
                print(" No tasks found.\n")
                return

            print("\n Task List:")
            for task in tasks:
                task_id, desc, status = task.strip().split("|")
                print(f"ID: {task_id} | {desc} | Status: {status}")
            print()

    except FileNotFoundError:
        print("No task file found.\n")


def update_task():
    task_id = input("Enter Task ID to update: ")
    updated = False

    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

    with open(FILE_NAME, "w") as f:
        for task in tasks:
            tid, desc, status = task.strip().split("|")

            if tid == task_id:
                print("1. Change Description")
                print("2. Mark as Completed")
                choice = input("Enter choice: ")

                if choice == "1":
                    desc = input("Enter new description: ")
                elif choice == "2":
                    status = "Completed"

                updated = True

            f.write(f"{tid}|{desc}|{status}\n")

    if updated:
        print("Task updated successfully!\n")
    else:
        print(" Task not found.\n")


def delete_task():
    task_id = input("Enter Task ID to delete: ")
    deleted = False

    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

    with open(FILE_NAME, "w") as f:
        for task in tasks:
            tid, desc, status = task.strip().split("|")

            if tid != task_id:
                f.write(task)
            else:
                deleted = True

    if deleted:
        print("Task deleted successfully!\n")
    else:
        print("Task not found.\n")


def search_task():
    keyword = input("Enter ID or keyword: ").lower()
    found = False

    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

        for task in tasks:
            if keyword in task.lower():
                print(task.strip())
                found = True

    if not found:
        print("No matching task found.\n")


def main():
    while True:
        print("====== TO-DO NOTES BUILDER ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            search_task()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")


main()