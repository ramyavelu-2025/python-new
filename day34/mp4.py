import random

# Generate a random secret number between 1 and 20
secret_number = random.randint(1, 20)
attempts = 5  # Total attempts allowed

print("🎯 Welcome to the Number Guessing Game!")
print("You have 5 chances to guess the number between 1 and 20.\n")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed the correct number!")
        break  # Exit the loop when guessed correctly
    elif guess > secret_number:
        print("📉 Too high! Try again.")
    else:
        print("📈 Too low! Try again.")

    attempts -= 1

    if attempts == 0:
        print(f"\n❌ Out of attempts! The correct number was {secret_number}.")
    else:
        print(f"Attempts remaining: {attempts}\n")
