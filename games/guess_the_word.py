import random

dictionary = {
    "planet": "A celestial body that orbits a star.",
    "banana": "A long curved fruit with yellow skin.",
    "silver": "A shiny gray precious metal.",
    "puzzle": "A game that tests your thinking skills.",
    "jungle": "A dense forest in tropical regions."
}

play_again = "yes"

while play_again == "yes":

    print("\033c", end="")   

    word = random.choice(list(dictionary.keys()))
    meaning = dictionary[word]
    length = len(word)

    attempts = 5

    while attempts > 0:

        print("\033c", end="")   

        print("Welcome to Guess The Word Game!")
        print("Meaning:", meaning)
        print("The word has", length, "letters.")
        print("Word:", "_ " * length)
        print("Attempts left:", attempts)

        guess = input("\nEnter your guess: ").lower()

        if len(guess) != length:
            print(" Please enter exactly", length, "letters.")
            input("Press Enter to continue...")
            continue

        if guess == word:
            print("\033c", end="")
            print("🎉 Congratulations! You guessed the word!")
            break

        match_count = 0

        for i in range(length):
            if guess[i] == word[i]:
                print("Letter", guess[i], "matches at position", i + 1)
                match_count += 1

        print("Total matched letters:", match_count)

        attempts -= 1
        input("Press Enter to continue...")

    if attempts == 0:
        print("\033c", end="")
        print("Game Over!")
        print("The correct word was:", word)

    play_again = input("\nDo you want to play another round? (yes/no): ").lower()

print("\nThanks for playing! 👋")