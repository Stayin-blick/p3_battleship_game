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

board_size = int(input("Please enter board size:\n"))
num_ships = int(input("Please enter number of boats:\n"))
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
    name = str(input("Please enter your name: \n"))
    return name


def guesses(board_size):
    user_guess_row = str(input("Guess a row: \n"))
    user_guess_column = str(input("Guess a column: \n"))
    int_user_guess_row = int(user_guess_row)
    int_user_guess_column = int(user_guess_column)
    computer_guess_row = randint(0,board_size-1)
    computer_guess_column = randint(0,board_size-1)
    while int_user_guess_row > board_size-1:
        print("Invalid row input, try again")
        user_guess_row = str(input("Guess a row: \n"))
        int_user_guess_row = int(user_guess_row)
    while int_user_guess_column > board_size-1:
        print("Invalid column input, try again")
        user_guess_column = str(input("Guess a column: \n"))
        int_user_guess_column = int(user_guess_column)

    return user_guess_row, user_guess_column, computer_guess_row, computer_guess_column

def count_ships_hit(board):
    count = 0
    for row in board:
        for column in row:
            if column == "-":
                count += 1
    return (count)


def main(board_for_user, board_for_computer, hidden_board):
    """
    Placement of ships on the board
    user
    computer
    confirmation of hits
    """
    welcomeMessage()
    name = getName()
    print(name + "'s Board:")


    for i in range(num_ships):
        random_row, random_column = randint(0,num_ships), randint(0,num_ships)
        while board_for_user[random_row][random_column] == "@":
            random_row, random_column = randint(0,num_ships), randint(0,num_ships)
        board_for_user[random_row][random_column] = "@"

    for i in range(num_ships):
        random_row, random_column = randint(0,num_ships), randint(0,num_ships)
        while hidden_board[random_row][random_column] == "@":
            random_row, random_column = randint(0,num_ships), randint(0,num_ships)
        hidden_board[random_row][random_column] = "@"

    display_board(board_for_user)

    print("Computer's Board: ")
    display_board(board_for_computer)

    player_score = 0
    computer_score = 0

    while count_ships_hit(user_board) < num_ships:
        """
        loop to determine winner
        """
        
        user_guess_row, user_guess_column, computer_guess_row, computer_guess_column = guesses(board_size)
        
        int_user_guess_row = int(user_guess_row)
        int_user_guess_column = int(user_guess_column)
        int_computer_guess_row = int(computer_guess_row)
        int_computer_guess_column = int(computer_guess_column)
        if board_for_computer[int_user_guess_row][int_user_guess_column] == "X":
            print("You guessed that one already")
            print("-----------------------------")
        else:
            if hidden_board[int_user_guess_row][int_user_guess_column] != "@":
                board_for_computer[int_user_guess_row][int_user_guess_column] = "X"
                print("Player missed this time")
            else:
                board_for_computer[int_user_guess_row][int_user_guess_column] = "-"
                print("You scored a point")
                player_score = player_score + 1
                print(name,"overall score is", player_score)

        if board_for_user[int_user_guess_row][int_user_guess_column] == "X":
            print("Computer guessed that one already")
            print("-----------------------------")
        else:
            if board_for_user[int_computer_guess_row][int_computer_guess_column] != "@":
                print("Computer missed this time")
                board_for_user[int_computer_guess_row][int_computer_guess_column] = "X"
            else:
                board_for_user[int_computer_guess_row][int_computer_guess_column] = "-"
                print("Computer scored a point")
                computer_score = computer_score + 1
                print("Computer overall score is", computer_score)

        print(name,"'s board'")
        display_board(user_board)
        print("---------------------------------------")
        print("Computer_board")
        display_board(computer_board)
        print("---------------------------------------")
        if count_ships_hit(computer_board) == num_ships:
            print(name,"wins")
            break
        if count_ships_hit(user_board) == num_ships:
            print("Computer wins")
            break

main(user_board,computer_board,hidden_board)
