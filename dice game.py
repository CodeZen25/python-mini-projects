import random

counter = 0

while True:
    choice = input("Roll the dice? (y/n):").lower()
    if choice == "y":
        n = int(input("How many dice you want to roll?:"))

        dice_rolls = [random.randint(1, 6) for _ in range(n)]
        print("You rolled:", dice_rolls)
        counter += 1

        print(f"You rolled the dice {counter} times.")

    elif choice == "n":
        print("Thanks for playing")
        break

    else:
        print("Invalid choice!")
