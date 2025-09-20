print("-----------ADD  TASKS-----------")
tasks = []
print("1. Add Task")
print("2. View Tasks")
print("3. Remove Task")
print("4. Quit")
print("---------------------------------")
choice = input("Enter choice: ")

if choice == "1":
    task = input("Enter Task: ")
    tasks.append(task)
    print(f"Task '{task}' added")
    while True:
        more = input("Do you want to add another task? (yes/no): ").lower()
        if more == "yes":
            task = input("Enter Task: ")
            tasks.append(task)
            print(f"Task '{task}' added")
        elif more == "no":
            choose = input("Enter choice: ")
            if choose == "1":
                task = input("Enter Task: ")
                tasks.append(task)
                print(f"Task '{task}' added")
            elif choose == "2":
                if not tasks:
                    print("No tasks yet!")
                else:
                    print("\nYour Tasks")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
            elif choose == "3":
                if not tasks:
                    print("No tasks to remove!")
                else:
                    print("\nYour Tasks")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
                    try:
                        task_num = int(input("Enter task number to remove: "))
                        if 1 <= task_num <= len(tasks):
                            removed_task = tasks.pop(task_num - 1)
                            print(f"Task '{removed_task}' removed")
                        else:
                            print("Invalid task number")
                    except ValueError:
                        print("Please enter a valid number")
            elif choose == "4":
                print("Exiting...")
                breakpoint
                break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
elif choice == "2":
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            while True:
                more = input(
                    "Do you want to view tasks again? (yes/no): ").lower()
                if more == "yes":
                    print("\nYour Tasks")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
                elif more == "no":
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    while True:
                        more = input(
                            "Do you want to view tasks again? (yes/no): ").lower()
                    if more == "yes":
                        print("\nYour Tasks")
                        for i, task in enumerate(tasks, start=1):
                            print(f"{i}. {task}")
                    elif more == "no":
                        break
elif choice == "3":
    if not tasks:
        print("No tasks to remove!")
    else:
        print("\nYour Tasks")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid number")
            while True:
                more = input(
                    "Do you want to remove another task? (yes/no): ").lower()
                if more == "yes":
                    if not tasks:
                        print("No tasks to remove!")
                        break
                    else:
                        print("\nYour Tasks")
                        for i, task in enumerate(tasks, start=1):
                            print(f"{i}. {task}")
                        try:
                            task_num = int(
                                input("Enter task number to remove: "))
                            if 1 <= task_num <= len(tasks):
                                removed_task = tasks.pop(task_num - 1)
                                print(f"Task '{removed_task}' removed")
                            else:
                                print("Invalid task number")
                        except ValueError:
                            print("Please enter a valid number")
                elif more == "no":
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
elif choice == "4":
    print("Exiting...")
    breakpoint
else:
    print("Invalid choice. Please enter a number between 1 and 4.")
    while True:
        more = input("Do you want to try again? (yes/no): ").lower()
        if more == "yes":
            choice = input("Enter choice: ")
            if choice == "1":
                task = input("Enter Task: ")
                tasks.append(task)
                print(f"Task '{task}' added")
            elif choice == "2":
                if not tasks:
                    print("No tasks yet!")
                else:
                    print("\nYour Tasks")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
            elif choice == "3":
                if not tasks:
                    print("No tasks to remove!")
                else:
                    print("\nYour Tasks")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
                    try:
                        task_num = int(input("Enter task number to remove: "))
                        if 1 <= task_num <= len(tasks):
                            removed_task = tasks.pop(task_num - 1)
                            print(f"Task '{removed_task}' removed")
                        else:
                            print("Invalid task number")
                    except ValueError:
                        print("Please enter a valid number")
            elif choice == "4":
                print("Exiting...")
                breakpoint
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        elif more == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
