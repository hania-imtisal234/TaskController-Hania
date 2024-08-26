# Task Manager CLI

A simple command-line interface (CLI) application for managing tasks. The application allows users to add, delete, mark tasks as completed, and list all tasks. Tasks are stored in a JSON file and managed using Python's built-in libraries.

## Project Structure

- `task.py`: Contains the `Task` class, representing individual tasks.
- `taskcontroller.py`: Contains the `TaskController` class, handling task management operations.
- `util.py`: Contains utility functions and the CLI menu for user interaction.
- `main.py`: The entry point of the application, which runs the CLI.

## Features

- Add a new task
- Delete an existing task
- Mark a task as completed
- List all tasks

## Requirements

- Python 3.6 or higher

## Installation
1.**Install any required packages (if applicable):**
    This project does not require any external packages beyond the standard Python library.

## Usage

1. **Run the CLI application:**
    ```bash
    python main.py
    ```
2. **Interact with the application using the menu options:**

    - **1**: Add Task
      - Enter the task description when prompted.
    - **2**: Delete Task
      - Enter the task ID to delete the specific task.
    - **3**: Mark Task as Completed
      - Enter the task ID to mark the specific task as completed.
    - **4**: List Tasks
      - Displays all tasks with their IDs, descriptions, and statuses.
    - **5**: Exit
      - Exits the application.

## Code Overview

### `task.py`

Defines the `Task` class using Python's `dataclass` decorator:

- **Attributes:**
  - `task_id`: UUID of the task (auto-generated if not provided).
  - `desc`: Description of the task.
  - `completed`: Status of the task (True if completed, False otherwise).
- **Methods:**
  - `to_dict()`: Converts the task object to a dictionary.
  - `mark_completed()`: Marks the task as completed.

### `taskcontroller.py`

Manages tasks using the `TaskController` class:

- **Attributes:**
  - `tasks`: A dictionary storing tasks with their UUIDs as keys.
  - `filename`: Name of the JSON file used for storing tasks.
- **Methods:**
  - `add_task(description)`: Adds a new task with the given description.
  - `delete_task(task_id)`: Deletes a task by its ID.
  - `mark_as_completed(task_id)`: Marks a task as completed.
  - `list_tasks()`: Lists all tasks.
- **Private Methods:**
  - `__save_tasks()`: Saves the current tasks to the JSON file.
  - `__load_tasks()`: Loads tasks from the JSON file.

### `util.py`

Contains utility functions for the CLI:

- **`menu()`**: Displays the main menu and returns the user's choice.
- **`cli()`**: Manages the main CLI loop, calling appropriate methods based on user input.

### `main.py`

Entry point for the application. Runs the CLI interface.