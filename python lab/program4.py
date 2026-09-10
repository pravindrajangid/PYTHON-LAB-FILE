from queue import Queue 
tasks = Queue()

while True:
    print("\n--- Task Scheduler ---")
    print("1. Add Task ")
    print("2. Run Task ")
    print("3. Check Tasks")
    print("4. Exit")

    choice = input("Enter  your choice:")

    if choice  == "1":
        task = input("Enter task name:")
        conditions = input("Should the task run? (yes/no): ")
        tasks.put((task , conditions))
        print("Task added successfully.")


    elif choice == "2":
        if tasks.empty():
            print ("No tasks available.")
        else:
            task, condition = tasks.get()
            if condition == "yes" and task != "":
                print("Running task:", task)
            elif condition == "no" or task == "":
                print("Skipping task:", task)
            else:
                print("Invalid condition.")

    elif choice == "3":
        if not tasks.empty():
            print("Tasks are available.")
        else:
            print("No tasks available.")

    elif choice == "4":
        print("Exiting Task Scheduler...")
        break
    else:
        print("Invalid  choice. Please try again.")
