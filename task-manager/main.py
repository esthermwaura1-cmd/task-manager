from task_utils import (
    add_task,
    mark_complete,
    view_pending_tasks,
    check_progress
)

from validation import validate_task_name


while True:

    print("\nTask Management System")
    print("1. Add Task")
    print("2. Mark Task Complete")
    print("3. View Pending Tasks")
    print("4. Check Progress")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        task_name = input("Enter task name: ")

        if validate_task_name(task_name):
            add_task(task_name)

    elif choice == "2":

        task_name = input("Enter task name: ")
        mark_complete(task_name)

    elif choice == "3":

        view_pending_tasks()

    elif choice == "4":

        check_progress()

    elif choice == "5":

        print("Goodbye!")
        break

    else:

        print("Invalid option")