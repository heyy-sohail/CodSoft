#Rock-Paper-Scissors in Python
import random

# Options
choices = ['rock', 'paper', 'scissors']

# Scores
user_score = 0
computer_score = 0

print("🎮 Welcome to Rock-Paper-Scissors Game!")
print("Instructions: Type rock, paper, or scissors to play.\n")

while True:
    # user input
    user = input("Your choice (rock/paper/scissors): ").lower()
    if user not in choices:
        print("Invalid choice. Try again.\n")
        continue

    # computer choice
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    # Determine winner
    if user == computer:
        result = "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        result = "You win! 🎉"
        user_score += 1
    else:
        result = "You lose! 😢"
        computer_score += 1

    # Show result
    print(result)
    print(f"Score: You {user_score} - {computer_score} Computer\n")

    # Play again?
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("\nThanks for playing!")
        break
