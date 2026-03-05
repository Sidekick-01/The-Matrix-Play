import random
import time


def opponent_dice():
    return random.randint(1, 6)


def dice_race(player_name):

    print("\n************************************")
    print("           DICE RACE GAME           ")
    print("************************************")

    player_score = 0
    computer_score = 0

    while player_score < 26 and computer_score < 26:

        input("\nPress Enter to roll dice...")

        player_roll = random.randint(1, 6)
        print(player_name, "rolled:", player_roll)
        player_score += player_roll
        print(player_name, "total:", player_score)

        if player_score >= 26:
            print(player_name, "WINS DICE RACE!")
            return "player"

        print("\nComputer rolling...")
        comp_roll = opponent_dice()
        print("Computer rolled:", comp_roll)
        computer_score += comp_roll
        print("Computer total:", computer_score)

        if computer_score >= 26:
            print("Computer WINS DICE RACE!")
            return "computer"


def bomb_defusal(player_name):

    print("\n************************************")
    print("          BOMB DEFUSAL GAME         ")
    print("************************************")

    wires = ["red", "blue", "green"]
    safe_wire = random.choice(wires)

    print("Wires available: red, blue, green")
    choice = input("Choose a wire to cut: ")
    if choice in wires:
        if choice != safe_wire:
            print(" BOOM! Wrong wire!")
            print("Computer wins Bomb Defusal!")
            return "computer"
        else:
            print("🎉 Bomb Defused Successfully!")
            print(player_name, "wins Bomb Defusal!")
            return "player"
    else:
        print("You Failed to cut teh wire!")



def math_game(player_name):

    print("\n************************************")
    print("         MATH CHALLENGE GAME        ")
    print("************************************")

    player_points = 0
    computer_points = 0

    for i in range(3):

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct = num1 + num2

        print("\nQuestion:", num1, "+", num2)
        answer = int(input("Your answer: "))

        if answer == correct:
            player_points += 1

        comp_answer = random.randint(1, 20)
        if comp_answer == correct:
            computer_points += 1

    print(player_name, "score:", player_points)
    print("Computer score:", computer_points)

    if player_points > computer_points:
        print(player_name, "wins Math Challenge!")
        return "player"
    else:
        print("Computer wins Math Challenge!")
        return "computer"



def word_scramble(player_name):

    print("\n************************************")
    print("          WORD SCRAMBLE GAME        ")
    print("************************************")

    words = ["planet", "silver", "banana", "jungle"]
    word = random.choice(words)

    scrambled = list(word)
    random.shuffle(scrambled)
    scrambled_word = ""

    for letter in scrambled:
        scrambled_word += letter

    print("Scrambled word:", scrambled_word)
    guess = input("Your guess: ")

    if guess == word:
        print(player_name, "wins Word Scramble!")
        return "player"
    else:
        print("Wrong! Word was:", word)
        print("Computer wins Word Scramble!")
        return "computer"



def memory_game(player_name):

    print("\n************************************")
    print("            MEMORY GAME             ")
    print("************************************")

    numbers = []

    for i in range(5):
        numbers.append(random.randint(1, 9))

    print("Remember these numbers:")
    print(numbers)

    time.sleep(5)
    print("\033c", end="")

    guess = input("Enter 5 numbers separated by space: ")
    user_numbers = guess.split()

    if len(user_numbers) != 5:
        print(" You did not enter 5 numbers!")
        print("Computer wins Memory Game!")
        return "computer"

    score = 0

    for i in range(5):
        if user_numbers[i].isdigit():
            if int(user_numbers[i]) == numbers[i]:
                score += 1
        else:
            print("Invalid input detected!")
            return "computer"

    if score >= 3:
        print(player_name, "wins Memory Game!")
        return "player"
    else:
        print("Computer wins Memory Game!")
        return "computer"


print("****************************************")
print("        ULTIMATE GAME TOURNAMENT        ")
print("****************************************")

player_name = input("Enter your name: ")

player_total = 0
computer_total = 0


games = [dice_race, bomb_defusal, math_game, word_scramble, memory_game]

for game in games:
    result = game(player_name)

    if result == "player":
        player_total += 1
    else:
        computer_total += 1

    print("\nCurrent Score:")
    print(player_name, ":", player_total)
    print("Computer :", computer_total)
    input("Press Enter to continue to next game...")



print("\n****************************************")
print("          TOURNAMENT RESULTS            ")
print("****************************************")

print(player_name, "won", player_total, "games")
print("Computer won", computer_total, "games")

if player_total > computer_total:
    print("\n🏆", player_name, "IS THE TOURNAMENT WINNER!")
else:
    print("\n🏆 COMPUTER IS THE TOURNAMENT WINNER!")