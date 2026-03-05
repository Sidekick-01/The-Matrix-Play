import random
# it will clear the terminal after every event ,
# you can say it liek refresh rate of this game.
def clear():
    print("\033c", end="")
# this is teh grid of the game 
def game_grid(pos):
    print()
    print(pos[0], "|", pos[1], "|", pos[2])
    print("--+---+--")
    print(pos[3], "|", pos[4], "|", pos[5])
    print("--+---+--")
    print(pos[6], "|", pos[7], "|", pos[8])
    print()

def check_winner(pos, s):
    # these are the winning positions on the grid
    if pos[0] == s and pos[1] == s and pos[2] == s:
        return True
    if pos[3] == s and pos[4] == s and pos[5] == s:
        return True
    if pos[6] == s and pos[7] == s and pos[8] == s:
        return True
    # the logic for the computer can check whose lien get completed first
    if pos[0] == s and pos[3] == s and pos[6] == s:
        return True
    if pos[1] == s and pos[4] == s and pos[7] == s:
        return True
    if pos[2] == s and pos[5] == s and pos[8] == s:
        return True


    if pos[0] == s and pos[4] == s and pos[8] == s:
        return True
    if pos[2] == s and pos[4] == s and pos[6] == s:
        return True

    return False


def get_player_move(pos, player_name):
    while True:
        move = input(f"{player_name}, choose position (1-9): ")

        if move in pos:
            return int(move) - 1
        else:
            print("Invalid move! Try again.")



def oppo_move(pos):
    # for now i am using oppoenent as computer (random) 
    # later i will add or connect it to multiplayer when i add it to my website.
    while True:
        r = random.randint(0, 8)

        if pos[r] != "X" and pos[r] != "O":
            return r


def play_game(player_name, scores):

    pos = ["1","2","3","4","5","6","7","8","9"]

    while True:
        clear()
        print("TIC TAC TOE\n")
        game_grid(pos)

        move_index = get_player_move(pos, player_name)
        pos[move_index] = "X"

        if check_winner(pos, "X"):
            clear()
            game_grid(pos)
            print(f"🎉 {player_name} wins!")
            scores["player"] += 1
            break

        full = True
        for cell in pos:
            if cell != "X" and cell != "O":
                full = False

        if full:
            clear()
            game_grid(pos)
            print("It's a draw!")
            scores["draw"] += 1
            break


        opponent_index = oppo_move(pos)
        pos[opponent_index] = "O"

        if check_winner(pos, "O"):
            clear()
            game_grid(pos)
            print("Computer wins!")
            scores["computer"] += 1
            break

        full = True
        for cell in pos:
            if cell != "X" and cell != "O":
                full = False

        if full:
            clear()
            game_grid(pos)
            print("It's a draw!")
            scores["draw"] += 1
            break


def main():

    clear()
    print("Welcome to Tic Tac Toe Game\n")

    player_name = input("Enter your name: ")
    if player_name == "":
        player_name = "Player"

    scores = {
        "player": 0,
        "computer": 0,
        "draw": 0
    }

    while True:
        play_game(player_name, scores)

        print("\nScoreboard:")
        print(f"{player_name}: {scores['player']}")
        print(f"Computer: {scores['computer']}")
        print(f"Draws: {scores['draw']}")

        again = input("\nPlay again? (y/n): ").lower()

        if again != "y":
            print("\nThanks for playing!")
            break

# Don't forget to play these cli based games on my webiste .
# https://sidekick-01.github.io/The-Matrix-Play/
main()