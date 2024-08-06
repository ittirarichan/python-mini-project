# main.py
import game

def main():
    print("Welcome to the Guessing Game!")
    while True:
        game.play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()