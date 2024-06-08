# Task 4: Rock-Paper-Scissors Game
import random


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"


def main():
    while True:
        user_choice = input(
            "Enter your choice (rock/paper/scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Try again.")
            continue
        computer_choice = get_computer_choice()
        print("Computer chose:", computer_choice)
        print(get_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
