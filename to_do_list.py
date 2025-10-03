import os

def display_menu():
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Done")
    print("4. Delete a Task")
    print("5. Exit")


def view_todo_list():
    if not os.path.exists("todo_list.txt"):
        print("To-Do list is empty")
        return

    with open("todo_list.txt", "r") as file:
        tasks = file.readlines()
    
    if not tasks:
        print("Your To-Do List is empty!")
    else:
        print("\n" + "-" * 30)
        print("|        To-Do List       |")
        print("-" * 30)
        for idx, task in enumerate(tasks, start=1):
            print(f"| {idx}. {task.strip()}")
        print("-" * 30 + "\n")

def add_task():
    task = input("Enter the task to add: ")
    with open("todo_list.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def mark_task_done():
    view_todo_list()
    try:
        task_num = int(input("Enter the number of the task to mark as done: "))
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
        
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] = "[DONE] " + tasks[task_num - 1]
            with open("todo_list.txt", "w") as file:
                file.writelines(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    view_todo_list()
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        with open("todo_list.txt", "r") as file:
            tasks = file.readlines()
        
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            with open("todo_list.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task '{deleted_task.strip()}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            view_todo_list()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice! Please select a valid option from the menu.")

if __name__ == "__main__":
    main()
