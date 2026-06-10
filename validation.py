def validate_task_name(title):
    """Validate a task title.
    
    Returns:
        tuple: (is_valid, message)
    """
    if not isinstance(title, str) or not title.strip():
        return False, "Title must be a non-empty string."
    title = title.strip()
    if len(title) < 3:
        return False, "Title must be at least 3 characters long."
    return True, "Valid."


def validate_task_id(task_id, tasks):
    """Validate a task ID against the existing tasks list.
    
    Returns:
        tuple: (is_valid, message)
    """
    try:
        task_id = int(task_id)
    except (ValueError, TypeError):
        return False, "Invalid task ID."
    if not isinstance(tasks, list) or len(tasks) == 0:
        return False, "No tasks available."
    if not any(task.get("id") == task_id for task in tasks):
        return False, "Task not found."
    return True, "Valid."


def validate_task(description):
    """Validate a task description.
    
    Args:
        description (str): The task description to validate.
        
    Raises:
        ValueError: If description is not a string or exceeds 500 characters.
    """
    if not isinstance(description, str):
        return False, "Description must be a string."

    if len(description) > 500:
        return False, "Description must be 500 characters or fewer."

    return True, "Valid."