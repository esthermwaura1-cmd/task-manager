tasks = []


def add_task(task_name):

    task = {
        "name": task_name,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully")


def mark_complete(task_name):

    for task in tasks:

        if task["name"] == task_name:

            task["completed"] = True
            print("Task marked as complete")
            return

    print("Task not found")


def view_pending_tasks():

    pending = []

    for task in tasks:

        if task["completed"] == False:
            pending.append(task)

    if len(pending) == 0:
        print("No pending tasks")

    else:

        for task in pending:
            print(task["name"])


def check_progress():

    if len(tasks) == 0:
        print("No tasks available")
        return

    completed = 0

    for task in tasks:

        if task["completed"]:
            completed += 1

    progress = (completed / len(tasks)) * 100

    print(f"Progress: {progress:.0f}%")