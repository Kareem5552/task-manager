def add_task(task_list, task):
    task_list.append(task)
    print(f"Task '{task}' added!")


def remove_task(task_list, task):
    if task in task_list:
        task_list.remove(task)
        print(f"Task '{task}' deleted!")
    else:
        print("This task is not in the list.")


def view_tasks(task_list):
    if task_list:
        print("\nYour current tasks:")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")
        print()
    else:
        print("Your list is empty!")


def main():
    task_list = []
    print("---------- Hello, welcome to the task manager ----------\n")

    while True:
        choice = input("Add, delete, view tasks, or exit? ").lower().strip()

        if choice == "add":
            while True:
                task = input("Enter task to add (or type back): ").strip()

                if task == "back":
                    break

                if task == "":
                    print("Task cannot be empty.")
                    continue

                add_task(task_list, task)

        elif choice == "delete":
            if not task_list:
                print("Your list is empty.")
                continue

            while True:
                view_tasks(task_list)
                task = input("Enter task to delete (or type back): ").strip()

                if task == "back":
                    break

                remove_task(task_list, task)

        elif choice == "view":
            view_tasks(task_list)

        elif choice == "exit":
            break

        else:
            print("Invalid input! Please enter add, delete, view, or exit.")

    print("---------- Finished ----------")


main()
