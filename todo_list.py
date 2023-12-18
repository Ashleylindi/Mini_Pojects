class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        if self.tasks:
            print("Tasks in the to-do list:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks in the to-do list.")

# Creating an instance of the TodoList
my_todo_list = TodoList()

# Sample usage
while True:
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        my_todo_list.add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        my_todo_list.remove_task(task)
    elif choice == '3':
        my_todo_list.view_tasks()
    elif choice == '4':
        print("Exiting the to-do list app. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
