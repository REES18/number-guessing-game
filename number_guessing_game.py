
# Number Guessing Game
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10")

# Pick a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize the guess
guess = 0

# Loop until the guess is correct
while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
