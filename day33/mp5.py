import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Get user input
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# Computer makes a random choice
computer_choice = random.choice(choices)

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print("🎉 You win!")
elif user_choice in choices:
    print("😞 Computer wins!")
else:
    print("Invalid input! Please choose rock, paper, or scissors.")
