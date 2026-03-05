import random

print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
print("You have 10 chances to guess it")
print("")

secret_number = random.randint(1, 100)
chances_left = 10
chance_number = 1

while chances_left > 0:

    print("Chance", chance_number)
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 You guessed it! You win!")
        print("The number was:", secret_number)
        break
    else:
        if guess > secret_number:
            print("Too high!")
        else:
            print("Too low!")

        chances_left = chances_left - 1
        chance_number = chance_number + 1

        print("Chances left:", chances_left)
        print("")

if chances_left == 0:
    print("Game Over! You used all chances.")
    print("The secret number was:", secret_number)