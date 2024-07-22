# game.py
import random

def generate_number(low, high):
    return random.randint(low, high)

def check_guess(secret_number, guess):
    if guess < secret_number:
        return "Too low"
    elif guess > secret_number:
        return "Too high"
    else:
        return "Correct! You guessed the number."

def play_game():
    low = 1
    high = 100
    secret_number = generate_number(low, high)
    print(f"Guess a number between {low} and {high}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            result = check_guess(secret_number, guess)
            print(result)
            if result == "Correct! You guessed the number.":
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
