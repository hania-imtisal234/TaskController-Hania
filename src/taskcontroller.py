import json
from task import Task
import uuid

class TaskController:
    def __init__(self, filename):
        self.tasks = {}
        self.filename = filename
        self.__load_tasks()

    def add_task(self, description) -> None:
        try:
            task = Task(desc=description)
            self.tasks[task.task_id] = task
            self.__save_tasks()
        except Exception as e:
            print(f"Error adding task: {e}")

    def delete_task(self, task_id) -> None:
        try:
            task_uuid = uuid.UUID(task_id)
            if task_uuid in self.tasks:
                del self.tasks[task_uuid]
                self.__save_tasks()
            else:
                print(f"Task ID {task_id} not found.")
        except ValueError:
            print(f"Invalid UUID format: {task_id}")
        except Exception as e:
            print(f"Error deleting task: {e}")

    def mark_as_completed(self, task_id):
        try:
            task_uuid = uuid.UUID(task_id)
            if task_uuid in self.tasks:
                self.tasks[task_uuid].mark_completed()
                self.__save_tasks()
            else:
                print(f"Task ID {task_id} not found.")
        except ValueError:
            print(f"Invalid UUID format: {task_id}")
        except Exception as e:
            print(f"Error marking task as completed: {e}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks.values():
            status = "Completed" if task.completed else "Pending"
            print(f'Task ID: {task.task_id}, Description: "{task.desc}", Status: {status}')

    def __save_tasks(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump({
                    'tasks': [task.to_dict() for task in self.tasks.values()]
                }, file, indent=4)
        except IOError as e:
            print(f"Error saving tasks to {self.filename}: {e}")
        except Exception as e:
            print(f"Unexpected error during save: {e}")

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
            print(f"{self.filename} not found. Starting with an empty task list.")
            self.tasks = {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON in {self.filename}. Starting with an empty task list.")
            self.tasks = {}
        except Exception as e:
            print(f"Unexpected error loading tasks: {e}")
            self.tasks = {}
