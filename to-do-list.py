# Task 1: To-Do List
def display_menu():
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")


def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def delete_task(tasks):
    task_number = int(input("Enter the task number to delete: "))
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted!")
    else:
        print("Invalid task number!")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
