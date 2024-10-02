import random

def player_input():
    print("Welcome To the Game of Rock Paper Scissors!")
    options = ["rock", "paper", "scissors"]
    player_choice = input("Please Choose one of the following : Rock, Paper, Scissors!").capitalize()
    computer_choice = random.choice(options).capitalize()
    choices = {
        "player": player_choice, "computer": computer_choice
    }

    return choices

def check_game(player, computer):
    print(f"You Chose {player} and computer chose {computer}")
    if player == computer:
        return "It is a Tie"
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock Beats Scissors, You Win!"
        else:
            return "Paper Beats Rock, You Lose!"
    elif player == "Paper":
        if computer == "Rock":
            return "Paper Beats Rock, You Win!"
        else:
            return "Scissors Beats Paper, You Lose!"
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissors Beats Paper, You Win!"
        else: 
            return "Rock beats Scissors, You Lose!"
    else:
        return "Please Choose One of The Correct Option: Rock, Paper and Scissors"

fetch_input = player_input()

initiate_game = check_game(fetch_input.get("player"), fetch_input.get("computer"))

print(initiate_game)

print(input("Click Enter to Dismiss"))

