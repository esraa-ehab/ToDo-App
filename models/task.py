from datetime import datetime
import uuid

class Task:
    def __init__(self, task_id, title, owner_id, owner_name, description="", priority="Low", status="To-Do", due_date=None):
        self.task_id = task_id or str(uuid.uuid4())
        self.title = title
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.description = description
        self.priority = priority
        self.status = status
        self.due_date = due_date
        self.created_at = datetime.now().strftime("%d-%m-%y %H:%M")

    def task_to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "owner_id": self.owner_id,
            "owner_name":self.owner_name,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at,
            "due_date": self.due_date
        }