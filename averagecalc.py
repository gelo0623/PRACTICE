print("-------------------Average Calculator-------------------")
print("This program calculates the average of numbers you enter.")
print("Type 'done' when you are finished entering numbers.")
print("--------------------------------------------------------")
total = 0
count = 0
while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done'.")
if count > 0:
    average = total / count
    print(f"The average of the entered numbers is: {average}")
else:
    print("No numbers were entered.")
print("--------------------------------------------------------")
while True:
    restart = input(
        "Do you want to calculate another average? (yes/no): ").lower()
    if restart == "yes":
        total = 0
        count = 0
        while True:
            user_input = input("Enter a number (or 'done' to finish): ")
            if user_input.lower() == 'done':
                break
            try:
                number = float(user_input)
                total += number
                count += 1
            except ValueError:
                print("Invalid input. Please enter a valid number or 'done'.")
        if count > 0:
            average = total / count
            print(f"The average of the entered numbers is: {average}")
        else:
            print("No numbers were entered.")
        print("--------------------------------------------------------")
    elif restart == "no":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
