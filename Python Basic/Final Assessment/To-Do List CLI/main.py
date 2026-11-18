tasks=[]

while True:
    print("\n=====To-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task As Complete")
    print("4. Delete Task")
    print("5. Exit")
    
    
    choice=input("Enter Your Choice: ")
    
    if choice=="1":
        task=input("enter A new Task:")
        tasks.append({"title":task,"completed":False})
        print("Task added successfully")
        
    elif choice=="2":
        if len(tasks)==0:
            print("no Tasks found")
        else:
            for i, task in enumerate(tasks, start=1):
                status="completed" if task ["completed"]else"pending"
                print(f"{i}.{task['title']}-{status}")
    
    elif choice =="3":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']}")

        if len(tasks) > 0:
            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to complete.")

    elif choice == "4":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']}")

        if len(tasks) > 0:
            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print("Deleted task:", removed["title"])
            else:
                print("Invalid task number.")
        else:
            print("No tasks to delete.")

    elif choice == "5":
        print("Thank you for using To-Do List")
        break

    else:
        print("Invalid choice. Please try again")