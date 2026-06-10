from validation import (
    validate_task_name,
    validate_task_id,
    validate_task as validate_task_description,
)


def add_task(tasks, title, description, due_date):
    is_valid, msg = validate_task_name(title)
    if not is_valid:
        return msg
    is_valid, msg = validate_task_description(description)
    if not is_valid:
        return msg

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


def validate_input(task_id, tasks):
    try:
        int(task_id)
    except (ValueError, TypeError):
        return False, "Invalid task ID."
    if len(tasks) == 0:
        return False, "No tasks available."
    return True, "Valid."
