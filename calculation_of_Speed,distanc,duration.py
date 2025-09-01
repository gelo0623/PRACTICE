while True:
    print("--------------------------------------------")
    print("Press 'a' to calculate speed")
    print("Press 'b' to calculate duration")
    print("Press 'c' to calculate distance")
    print("---------------------------------------------")

    choice = input("Enter your choice: ")

    if choice == 'a':
        distance = float(input("Enter distance: "))
        duration = float(input("Enter the duration: "))

        if duration == 0:
            print("Undefined")
        else:
            speed = distance / duration
            print(f"The speed is: {speed} km/h")

    elif choice == 'b':
        distance = float(input("Enter distance: "))
        speed = float(input("Enter speed: "))

        if speed == 0:
            print("Undefined")
        else:
            duration = distance / speed
            print(f"The duration is: {duration}")

    elif choice == 'c':
        speed = float(input("Enter distance: "))
        duration = float(input("Enter duration: "))

        distance = speed * duration
        print(f"The distance is: {distance}")

    elif choice == 'n':
        print("Exiting program")
        break
    else:
        print("Invalid choice")

    again = input("Do you wish to calculate again? (y/n)")
    if again != 'y':
        break
