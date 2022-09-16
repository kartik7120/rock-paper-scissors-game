import random


def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock,paper,scissors)")
    if player_choice not in options:
        raise ValueError(f"choice should be one of ({','.join(options)})!")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player} Computer chose {computer}")
    if player == computer:
        return "It's a tie"
    if player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers Rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers Rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."


def main():
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])

    print(result)


if __name__ == "__main__":
    main()
