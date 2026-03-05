import random
import time
# This is a simple rock paper adn scissor game okay 
# cli version u can see the ascii art on terminal for graphics
def r_p_s(choice):
    # each and individual ascii art is here 
    # i have used teh every line of teh ascii art in a list coz when i try to print it on terminal 
    # in a whole using triple quoutes there was glithcing means a single character extra or ,
    # The width of teh screen changes tehn the whole art get disturbed liek teh common problem was 
    # bottom part of the ascii art was not comming 
    if choice == "rock":
        return [
            "    _______      ",
            "---'   ____)     ",
            "      (_____)    ",
            "      (_____)    ",
            "      (____)     ",
            "---.__(___)      "
        ]

    elif choice == "paper":
        return [
            "     _______     ",
            "---'   ____)____ ",
            "          ______)",
            "          _______)",
            "         _______)",
            "---.__________)  "
        ]

    elif choice == "scissors":
        return [
            "    _______      ",
            "---'   ____)____ ",
            "          ______)",
            "       __________)",
            "      (____)     ",
            "---.__(___)      "
        ]


def player_name():
    name = input("What is your name? ")
    if name == "":
        name = "Player"
    return name


def player_choice(name):
    while True:
        print("1 = rock   2 = paper   3 = scissors")
        num = input(f"{name}'s choice (1/2/3): ")

        if num == "1":
            return "rock"
        elif num == "2":
            return "paper"
        elif num == "3":
            return "scissors"
        else:
            print("Please choose 1, 2 or 3!\n")


def computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def who_wins(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"


def main():
    print("\033c", end="")

    name = player_name()
    scores = {"player": 0, "computer": 0, "ties": 0}

    print(f"\nHello {name}! Let's play Rock Paper Scisors!\n")

    while True:

        player = player_choice(name)
        computer = computer_choice()

        player_art = r_p_s(player)
        computer_art = r_p_s(computer)

        print("\n" + name.upper() + "        COMPUTER")
        print("-" * 40)


        for i in range(len(player_art)):
            print(player_art[i] + "   " + computer_art[i])

        print("-" * 40)

        result = who_wins(player, computer)

        if result == "player":
            print(f"{name.upper()} WINS! 🎉")
            scores["player"] += 1
        elif result == "computer":
            print("COMPUTER WINS 😔")
            scores["computer"] += 1
        else:
            print("TIE 🤝")
            scores["ties"] += 1

        print(f"\nScore: {name} {scores['player']} - Computer {scores['computer']} - Ties {scores['ties']}\n")

        again = input("Wanna Play Again (y/n): ").lower()
        if again != "y":
            print("\nThanks for playing!")
            break

        print("\033c", end="")


main()