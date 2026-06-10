"""
main.py
-------
Task Management System - CLI using separated modules.
"""

import os
import sys

try:
    from task_utils import add_task, complete_task, get_pending_tasks, calculate_progress
except ModuleNotFoundError:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    try:
        from task_utils import add_task, complete_task, get_pending_tasks, calculate_progress
    except ModuleNotFoundError:
        def add_task(tasks, title, description, due_date):
            from validation import validate_task_name, validate_task as validate_task_description

            is_valid, msg = validate_task_name(title)
            if not is_valid:
                return msg
            validate_task_description(description)

            title = title.strip()
            description = description.strip()
            due_date = due_date.strip() if isinstance(due_date, str) else str(due_date)

            new_id = max((task.get("id", 0) for task in tasks), default=0) + 1
            task = {
                "id": new_id,
                "title": title,
                "description": description,
                "due_date": due_date,
                "completed": False,
            }
            tasks.append(task)
            return "Task added successfully!"

        def complete_task(tasks, task_id):
            from validation import validate_task_id

            is_valid, msg = validate_task_id(task_id, tasks)
            if not is_valid:
                return msg
            task_id = int(task_id)
            for task in tasks:
                if task.get("id") == task_id:
                    if task.get("completed"):
                        return "Task already completed."
                    task["completed"] = True
                    return "Task marked as complete!"
            return "Task not found."

        def get_pending_tasks(tasks):
            return [task for task in tasks if not task.get("completed")]

        def calculate_progress(tasks):
            total = len(tasks)
            if total == 0:
                return 0.0
            completed = sum(1 for task in tasks if task.get("completed"))
            return (completed / total) * 100


def display_menu():
    print("\n===== Task Management System =====")
    print("1. Add a task")
    print("2. Mark a task as complete")
    print("3. View pending tasks")
    print("4. Track progress")
    print("5. Exit")
    print("==================================")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            print(add_task(tasks, title, description, due_date))

        elif choice == "2":
            pending = get_pending_tasks(tasks)
            if not pending:
                print("No pending tasks to complete.")
            else:
                print("\nPending Tasks:")
                for task in pending:
                    print(f"  ID: {task['id']} | {task['title']} | Due: {task['due_date']}")
                task_id = input("Enter the task ID to mark as complete: ")
                print(complete_task(tasks, task_id))

        elif choice == "3":
            pending = get_pending_tasks(tasks)
            if not pending:
                print("No pending tasks.")
            else:
                print("\nPending Tasks:")
                for task in pending:
                    print(f"  ID: {task['id']} | {task['title']} | Due: {task['due_date']}")

        elif choice == "4":
            print(f"Progress: {calculate_progress(tasks):.2f}%")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
