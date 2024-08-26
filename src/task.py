from dataclasses import dataclass, field
import uuid

@dataclass
class Task:
    task_id: uuid.UUID = field(default_factory=uuid.uuid4)
    desc: str = field(default="")
    completed: bool = field(default=False)

    def __post_init__(self):
        assert isinstance(self.task_id, uuid.UUID), f"Task ID must be a UUID!"
        assert isinstance(self.desc, str), f" Description must be a string!"
        assert isinstance(self.completed, bool), f"Task completion must be a bool value!"

    def to_dict(self):
        return {
            'task_id': str(self.task_id),  # Convert UUID to string
            'description': self.desc,
            'completed': self.completed
        }

    def mark_completed(self):
        self.completed = True
