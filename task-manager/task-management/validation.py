def validate_task_name(task_name):

    try:

        if len(task_name.strip()) == 0:
            raise ValueError("Task name cannot be empty")

        return True

    except ValueError as e:
        print(e)
        return False