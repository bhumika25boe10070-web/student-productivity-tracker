tasks = []

def add_task():
    task_name = input("Enter task: ")
    tasks.append({"task": task_name, "done": False})
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    
    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(f"{i+1}. {task['task']} - {status}")
    print()

def mark_complete():
    view_tasks()
    if not tasks:
        return
    
    try:
        task_no = int(input("Enter task number to mark as complete: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["done"] = True
            print("Task marked as complete!\n")
        else:
            print("Invalid task number.\n")
    except:
        print("Please enter a valid number.\n")

def show_progress():
    if not tasks:
        print("No tasks to track.\n")
        return
    
    completed = sum(1 for task in tasks if task["done"])
    total = len(tasks)
    percent = (completed / total) * 100
    
    print(f"\nProgress: {completed}/{total} tasks completed ({percent:.2f}%)\n")

def menu():
    while True:
        print("===== Student Productivity Tracker =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Show Progress")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            show_progress()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()