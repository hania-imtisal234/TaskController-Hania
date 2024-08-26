import json
from task import Task
import uuid

class TaskController:
    def __init__(self, filename):
        self.tasks = {}
        self.filename = filename
        self.__load_tasks()

    def add_task(self, description) -> None:
        task = Task(desc=description)
        self.tasks[task.task_id] = task
        self.__save_tasks()


    def delete_task(self, task_id):
        try:
            task_uuid = uuid.UUID(task_id)
            if task_uuid in self.tasks:
                del self.tasks[task_uuid]
                self.__save_tasks()
        except ValueError:
            print(f"Invalid UUID: {task_id}")

    def mark_as_completed(self, task_id):
        try:
            task_uuid = uuid.UUID(task_id)
            if task_uuid in self.tasks:
                self.tasks[task_uuid].mark_completed()
                self.__save_tasks()
        except ValueError:
            print(f"Invalid UUID: {task_id}")

    def list_tasks(self):
        for task in self.tasks.values():
            print(f'Task ID: {task.task_id}, Description: "{task.desc}", Status: {"Completed" if task.completed else "Pending"}')

    # private methods
    def __save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump({
                 'tasks': [task.to_dict() for task in self.tasks.values()]
            }, file, indent=4)

    #private method
    def __load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                data = file.read().strip()
                data = json.loads(data)
                self.tasks = {
                    uuid.UUID(task_data['task_id']): Task(
                        task_id=uuid.UUID(task_data['task_id']),
                        desc=task_data['description'],
                        completed=task_data['completed']
                    )
                    for task_data in data.get('tasks', [])
                }
        except FileNotFoundError:
            self.tasks = {}
        except ValueError as e:
            print(f"Error loading tasks: {e}")
