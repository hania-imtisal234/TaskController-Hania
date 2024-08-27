from dataclasses import dataclass, field
import uuid

@dataclass
class Task:
    task_id: uuid.UUID = field(default_factory=uuid.uuid4)
    desc: str = field(default="")
    completed: bool = field(default=False)

    def __post_init__(self):
        if not isinstance(self.task_id, uuid.UUID):
            raise TypeError("Task ID must be a UUID!")
        if not isinstance(self.desc, str):
            raise TypeError("Description must be a string!")
        if not isinstance(self.completed, bool):
            raise TypeError("Task completion must be a bool value!")

    def to_dict(self):
        return {
            'task_id': str(self.task_id),  # Convert UUID to string
            'description': self.desc,
            'completed': self.completed
        }

    def mark_completed(self):
        self.completed = True
