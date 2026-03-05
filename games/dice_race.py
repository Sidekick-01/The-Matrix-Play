import random
print("\033[38;2;150;255;50m")
# print("\033[38;2;50;200;50m")
print("===================================")
print("            Dice-Race              ")
print("===================================")

human_score = 0
computer_score = 0

while human_score < 26 and computer_score < 26:


    input("\nPress Enter to roll the dice...")

    human_dice = random.randint(1, 6)
    print("You rolled:", human_dice)

    human_score = human_score + human_dice
    print("Your total score:", human_score)

    if human_score >= 26:
        break


    print("\nComputer is rolling...")
    computer_dice = random.randint(1, 6)
    print("Computer rolled:", computer_dice)

    computer_score = computer_score + computer_dice
    print("Computer total score:", computer_score)

    print("\n-----------------------------")


print("\nFinal Scores:")
print("Your score:", human_score)
print("Computer score:", computer_score)

if human_score >= 26:
    print("\n🎉 You Win!")
else:
    print("\n💻 Computer Wins!")