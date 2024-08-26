from taskcontroller import TaskController

def menu():
    print("----------------Task Manager------------------")
    print('Press 1.Add Task')
    print('Press 2.Delete Task')
    print('Press 3.Mark Task as completed')
    print('Press 4.List Task')
    print('Press 5.Exit')
    return int(input('Choose an option: '))

def cli():
    manager = TaskController('Tasks.json')

    while True:
        chosen_option = menu()

        match chosen_option:
            case 1:
                description = input("Enter the task description: ")
                manager.add_task(description)
                print('Task Added!')
            case 2:
                task_id = input("Enter the task ID to delete it: ")
                manager.delete_task(task_id)

            case 3:
                task_id = input("Enter the task ID to mark as completed: ")
                manager.mark_as_completed(task_id)
            case 4:
                manager.list_tasks()
                print('Task Listed!')

            case 5:
                print('Program Exited Successfully!')
                break
