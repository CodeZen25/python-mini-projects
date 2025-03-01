import random


start = int(input("Enter start of range:"))
end = int(input("Enter end of range:"))

secret_number = random.randint(start, end)
attempts = 3

count_attempt = 0


for _ in range(attempts):
    while True:
        try:
            guess = int(input(f"Guess the number between {start} and {end}: "))

            if guess > secret_number:
                print("Too high!")
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Congratulations! You guessed the number!")
                count_attempt += 1
                print(f"You guessed at {count_attempt} attempt")
                break
            break

        except ValueError:
            print("Please enter a valid number.")
