def individual_task(todo):
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "priority": todo["priority"],
        "is_done": todo["is_done"],
        "is_deleted": todo["is_deleted"],
        "created_at": todo["created_at"],
    }


def list_task(todos):
    return [individual_task(todo) for todo in todos]
