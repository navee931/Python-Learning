# Let user add/remove tasks via input and maintain a list.

Todo = []

def view():
     if Todo:
            print("Your To-Do List:")
            for i, t in enumerate(Todo, start=1):
                print(f"{i}. {t}")
     else:
         print("Your To-Do list is empty.")

while True:

    print("\nChoose an operation")
    print("1. Add")
    print("2. Remove")
    print("3. View")
    print("4. Exit")
    
    choice = input("\nEnter your Choice: ")
    
    if choice == "1":
        task = input("Enter your Task: ")
        Todo.append(task)
        print("Task added\n")
        view()

    elif choice == "2":
       task = input("Enter your Task number: ")
       if task.isdigit() and 1 <= int(task) <= len(Todo):
            Todo.pop(int(task) - 1)
            print("Task Removed\n")
            view()
       else:
            print("Task not found\n")
            view()

    elif choice == "3":
        print()
        view()

    elif choice == "4":
        print("\nThank You")
        break

    else:
        print("\nInvalid Choice, Try again") 
