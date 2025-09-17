print("-------------------Tasks-------------------")
print("This is a collection of simple Python tasks.")
print("Choose a task to perform:")
print("1. Guessing Game")
print("2. Average Calculator")
print("3. Calculator")
print("4. Exit")
print("-------------------------------------------")
while True:
    task_choice = input(
        "Enter the number of the task you want to perform (1-4): ")
    if task_choice == '1':
        import guessing_game
    elif task_choice == '2':
        import averagecalc
    elif task_choice == '3':
        import Calculator
    elif task_choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 4.")
