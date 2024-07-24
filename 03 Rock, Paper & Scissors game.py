# TASK 03  **** ROCK PAPER SCISSOR **** CODSOFT ****

import random

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "You Win!"
    else:
        return "Computer Wins!"

def main():
    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        print("Choose one: rock, paper, scissors")
        print("Type 'exit' to leave the game")

        options = ['rock', 'paper', 'scissors']
        user_choice = input("Your choice: ").lower()

        if user_choice == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        if user_choice in options:
            comp_choice = random.choice(options)
            print(f"Computer chose: {comp_choice}")
            outcome = get_winner(user_choice, comp_choice)
            print(outcome)
        else:
            print("Invalid input. Please select rock, paper, or scissors, or type 'exit'.")

if __name__ == "__main__":
    main()
