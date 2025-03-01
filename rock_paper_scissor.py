import random

# emojis
r = "🪨"
p = "📄"
s = "✂️"


# computer choice

options = [r, p, s]
computer_choice = random.choice(options)

# input rps?
your_choice = input("Rock, paper, or scrissors? (r/p/s):")

# print you chose
print(f"You chose {your_choice}")

# print computer chose
print(f"Computer chose {computer_choice}")

while True:

    if your_choice is r and computer_choice is s:
        print("You win!")

    elif your_choice is p and computer_choice is r:
        print("You win!")

    elif your_choice is s and computer_choice is p:
        print("You win!")

    elif your_choice is r and computer_choice is p:
        print("You lose!")

    elif your_choice is p and computer_choice is s:
        print("You lose!")

    elif your_choice is s and computer_choice is r:
        print("You lose!")

    elif your_choice == computer_choice:
        print("Tie")
        break

    else:
        print("Invalid choice")

    # input continue y/n?

    wanna_continue = input("Continue? (y/n):")

    if wanna_continue == "y":
        your_choice = input("Rock, paper, or scrissors? :")
    elif wanna_continue == "n":
        break
