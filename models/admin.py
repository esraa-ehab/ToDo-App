from utils.helpers import *
from models.user import User
from services.task_manager import taskManager

class Admin(User):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.task_man = taskManager()

    def view_all_users(self):
        return load_users()

    def view_all_tasks(self):
        return self.task_man.load_tasks()
    
    def delete_task(self, task_id):
        tasks = self.task_man.load_tasks()
        for i, task in enumerate(tasks):
            if task.get("task_id") == task_id or task.get("id") == task_id:
                self.task_man.delete_task(i)
                return True
        return False

    def deactivate_user(self, user_id):
        users = load_users()
        for user in users:
            if user["id"] == user_id:
                user["status"] = "inactive"
                break
        save_users(users)
        return True