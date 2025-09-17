import random
print("---------------------Guessing Game---------------------")
number = random.randint(0, 100)
guess = None
tries = 0
while guess != number:
    guess = int(input("Enter your guess: "))
    tries += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(
            f"Congratulations! You've guessed the number {number} in {tries} tries.")
print("-------------------------------------------------------")
while True:
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        number = random.randint(0, 100)
        guess = None
        tries = 0
        while guess != number:
            guess = int(input("Enter your guess: "))
            tries += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(
                    f"Congratulations! You've guessed the number {number} in {tries} tries.")
                print("-------------------------------------------------------")
    elif play_again == "no":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
