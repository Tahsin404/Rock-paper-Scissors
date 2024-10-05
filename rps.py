import random


# create a function to fetch user info along with computer data and store them in a dict

while True:

    def data():
        options = ["Rock", "Paper", "Scissors"]

        player_input = input("Choose: rock, paper or scissors?".title()).capitalize()
        computer_input = random.choice(options).capitalize()

        choices = {
            "player": player_input,
            "computer": computer_input,
        }

        return choices

    def compute(player, computer):
        # Declare player and computer choice
        print(f"You Chose {player} and computer chose {computer}")

        if player == computer:
            return "It is a tie".title()
        elif player == "Rock":
            if computer == "Scissors":
                return "Rock beats scissors, You win!".title()
            else:
                return "Paper beats rock, You lose!".title()
        elif player == "Paper":
            if computer == "Rock":
                return "Paper beats rock, you win!".title()
            else:
                return "Scissors beats paper, you lose!".title()
        elif player == "Scissors":
            if computer == "Paper":
                return "Scissors beats paper, you win!".title()
            else:
                return "Rock beats scissors, you lose!".title()
        else:
            return "Please choose one of the following: Rock paper or scissors".title()

        # fetch the choices dict from the function and set it as the new params of compute function.

    info = data()

    initiate = compute(info.get("player"), info.get("computer"))
    print(initiate)
    reinitialize = input("Would You like to play again?(Y/n)").capitalize()
    print(reinitialize)
    while reinitialize not in ["Y", "N"]:
        print(f"Please Type Y or N, {reinitialize}")
        reinitialize = input("Would you like to play again?(Y/N)")
    if reinitialize == "Y":
        continue
    elif reinitialize == "N":
        print("Thank you For playing")
        break
    else:
        continue
