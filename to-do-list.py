def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, (task, completed) in enumerate(todo_list, start=1):
            status = "Completed" if completed else "Not completed"
            print(f"{index}. {task} - {status}")

def add_task(todo_list):
    task = input("Enter the task's name: ")
    todo_list.append((task, False))
    print(f"Task '{task}' has been added.")

def mark_task_completed(todo_list):
    display_todo_list(todo_list)
    task_number = int(input("Enter the task number to mark as completed: "))
    if 0 < task_number <= len(todo_list):
        task, _ = todo_list[task_number - 1]
        todo_list[task_number - 1] = (task, True)
        print(f"Task '{task}' has been marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(todo_list):
    display_todo_list(todo_list)
    task_number = int(input("Enter the task number to remove: "))
    if 0 < task_number <= len(todo_list):
        task, _ = todo_list.pop(task_number - 1)
        print(f"Task '{task}' has been removed.")
    else:
        print("Invalid task number.")

def main():
    todo_list = []
    while True:
        print("\n1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            mark_task_completed(todo_list)
        elif choice == '4':
            remove_task(todo_list)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
