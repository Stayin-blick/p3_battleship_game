from random import randint

# X represents missed shot
# - represents hit shot

"""
setting up the game
board size
user board
computer board
tally of ships hit
"""

board_size = int(input("Please enter board size:"))
num_ships = int(input("Please enter number of boats:"))
user_board = [["."] * board_size for x in range(board_size)]
computer_board = [["."] * board_size for x in range(board_size)]
hidden_board = [["."] * board_size for x in range(board_size)]

def display_board(board):
    for row in board:
        print (" ".join(row))


def welcomeMessage():
    print("----------------------------------")
    print("Welcome to ULTIMATE BATTLESHIPS!!")
    print("Board Size: ",board_size,"Number of ships :",num_ships)
    print("Top left corner is row: 0, col: 0")
    print("------------------------------------")

def getName():
    name = str(input("Please enter your name: "))
    return name


def guesses(board_size):
    user_guess_row = str(input("Guess a row: "))
    user_guess_column = str(input("Guess a column: "))
    int_user_guess_row = int(user_guess_row)
    int_user_guess_column = int(user_guess_column)
    computer_guess_row = randint(0,board_size-1)
    computer_guess_column = randint(0,board_size-1)
    while int_user_guess_row > board_size-1:
        print("Invalid row input, try again")
        user_guess_row = str(input("Guess a row: "))
        int_user_guess_row = int(user_guess_row)
    while int_user_guess_column > board_size-1:
        print("Invalid column input, try again")
        user_guess_column = str(input("Guess a column: "))
        int_user_guess_column = int(user_guess_column)

    return user_guess_row, user_guess_column, computer_guess_row, computer_guess_column

def count_ships_hit(board):
    count = 0
    for row in board:
        for column in row:
            if column == "-":
                count += 1
    return (count)



