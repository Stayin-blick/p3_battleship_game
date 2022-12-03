from random import randint
scores = {"computer":0, "player":0}

class board:
    """
    battleship board, player set board size, player set number of ships,
    the player name and board type (player board or computer)
    has methods for adding ships and guessses and prints the board
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]        
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.gueses = []
        self.ships = []
    
    def print(self):
        for row in self.board:
            print("_".join(row))
    
    def guess (self, x, y):
        self.gueses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error you cannot add any more ships")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board [x] [y] = "@"
    

def random_point (size):
    """
    helper function to return integer between 0 and size
    """
    return randint(0, size - 1)

"""
def valid_coordinates(x, y, board): 
    makes sure guesses are in the scope and not repeated
    try:

"""

def populate_board(board):
    print(_) * {size}

"""

def play_game(computer_board, player board):
    computer random row random column (random_point())
    player input column input row
    computer_board 
"""

def new_game():
    """
    starts a new game. sets the board size and number of ship, resets the
    scores and initailises the boards.
    """

    try:
        size = int(input("choose your board size: "))
    except ValueError():
        print("input must be a number")
    try:
        num_ships = int(input("how many ships would you like to play with: "))
    except ValueError():
        print("input must be a number")
    scores ["computer"] = 0 
    scores ["player"] = 0
    print ("-" * 35)
    print ("welcome to ultimate battleships")
    print (f"board size:{size}. number of ships:{num_ships}")
    print ("top left corner is row 0, column 0")
    print ("-" * 35)
    player_name = input("please enter your name: \n")
    print ("-" * 35)

    computer_board = board(size, num_ships, "computer", type = "computer")
    player_board = board(size, num_ships, player_name, type = "player")

    for _ in range(num_ships):
        populate_board (player_board)
        populate_board (computer_board)
    
    play_game (computer_board, player_board)


new_game()