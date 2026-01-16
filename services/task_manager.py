import json
import os
from models.task import Task

task_file = "tasks.json"

class taskManager():
    def __init__(self):
       if os.path.exists(task_file) is False:
           with open(task_file, "w") as f:
               json.dump([], f)
    
    def load_tasks(self):
        with open(task_file, "r") as f:
            return json.load(f)

    def edit_task(self, task_index, updated_data):
        tasks = self.load_tasks()
        if 0 <= task_index < len(tasks):
            tasks[task_index].update(updated_data)
            self.save_tasks(tasks)

    def save_tasks(self, tasks):
        with open(task_file, "w") as f:
            json.dump(tasks, f, indent=4)

    def add_task(self, task):
        tasks = self.load_tasks()
        tasks.append(task.task_to_dict())
        self.save_tasks(tasks)

    def get_user_tasks(self, owner_id):
        tasks = self.load_tasks()
        return [(i, t) for i, t in enumerate(tasks) if t["owner_id"]==owner_id]
    
    def delete_task(self, task_index):
        tasks = self.load_tasks()
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            self.save_tasks(tasks)