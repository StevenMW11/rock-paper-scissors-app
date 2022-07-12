#import necessary packages, including random, choice, and os
from secrets import choice
import random
import os

#allow player to input their own name through environment variable
player_name = os.getenv("PLAYER_NAME", default="Player One")

#create function to run player and computer choices through to determine winner
def rock_paper_scissors_outcome(player, computer):
    player_choice = player
    computer_choice = computer
    
    if player_choice == computer_choice:
        print(f"Both Player and Computer chose {player_choice}. It's a tie game.")
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print(f"Rock beats Scissors. {player_name} Wins!")
        else:
            print("Paper beats Rock. The Computer Wins...")
    elif player_choice == "paper":
        if computer_choice == "rock":
            print(f"Paper beats Rock. {player_name} Wins!")
        else:
            print("Scissors beats Paper. The Computer Wins...")
    else:
        if computer_choice == "paper":
            print(f"Scissors beats Paper. {player_name} Wins!")
        else:
            print("Rock beats Scissors. The Computer Wins...")

if __name__ == "__main__":

    #welcome message
    print("--------------------------------------------------")
    print(f"Welcome {player_name} to Rock, Paper, Scissors, Shoot! Time to play against the Computer.")

    #define list of valid options
    valid_choices = ["rock", "paper", "scissors"]

    #obtain user input, case sensitize the variable with casefold function (makes all uppercase letters lowercase)
    player_choice = input("Choose: Rock, Paper, or Scissors: ").casefold()
    print("--------------------------------------------------")
    #play the game and present the outcome, unless the user inputs an invalid choice
    if (player_choice in valid_choices):
        computer_choice = random.choice(valid_choices)

        print(f"{player_name}'s Choice: ", player_choice)
        print("Computer's Choice: ", computer_choice)
        print("")

        rock_paper_scissors_outcome(player_choice,computer_choice)
        print("")

        print("Thank you for playing. Please play again!")
        print("--------------------------------------------------") 
    else:
        print("Your choice was not a valid input, please re-run the program with a valid input of Rock, Paper, or Scissors.")
        print("--------------------------------------------------")
        exit()