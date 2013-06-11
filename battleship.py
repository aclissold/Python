#!/usr/bin/python3
from random import randint

# Setup stuff

# Function to play again

def again():
    print()
    choice = input("Again? y/n: ")
    choice = choice.lower()
    if choice == "y":
        print()
        play()
    elif choice == "n":
        pass
    else:
        print("Please enter a 'y' or an 'n'.")
        again()

# Function to play

def play():

    board = []
    for x in range(5):
        board.append(["O"] * 5)

    # Print a nice boat
    print(\
    ".  o ..                  \n"\
    "o . o o.o                \n"\
    "     ...oo               \n"\
    "       __[]__            \n"\
    "    __|_o_o_o\__         \n"\
    "    \\\"\"\"\"\"\"\"\"\"\"/         \n"\
    "     \. ..  . /          \n"\
    "^^^^^^^^^^^^^^^^^^^^")

    print()
    print("Let's play Battleship!")

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)

    def print_board(board):
        for row in board:
            print(" ".join(row))

    for turn in range(10):
        hasValidGuess = False
        print()
        print("Turn", turn + 1, "of 10.")
        print_board(board)
        while not hasValidGuess:
            try:
                print()
                guess_row = eval(input("Guess Row: "))
                guess_col = eval(input("Guess Col: "))
                hasValidGuess = True
            except NameError:
                print("Please enter an index from 0 - 4.")
            except SyntaxError:
                print("Please enter an index from 0 - 4.")

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            again()
            break
        else:
            if ((guess_row < 0 or guess_row > 4)
                or (guess_col < 0 or guess_col > 4)):
                print("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            if turn == 9:
                print()
                print("GAME OVER")
                again()

if __name__ == '__main__':
    play()
