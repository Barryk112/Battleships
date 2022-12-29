from random import randint

scores = {"player": 0, "computer": 0}



class Board:
    """
    Main class for board.
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.num_ships = num_ships
        self.name = name
        self.type = type

        self.board = [["." for x in range(size)] for y in range(size)]
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))



def random_point(size):
    """
    Function that returns a random int between 0 and size 
    of the board
    """
    return randint(0, size - 1)



def validate(choice, board_size):
    """
    Validates players input choice for rows and columns
    """
    try:
        choice = int(choice)
        if choice > board_size:
            raise ValueError("Your choice must be equal or less than board size")
            return False
    except ValueError:
        print("Must be an integer")
        return False
    return True


def populate_board(board):
    """
    Populates game board with ships marked as "@"
    """
    x, y = random_point(board.size), random_point(board.size)
    while board.board[x][y] == "@":
        x, y = random_point(board.size), random_point(board.size)
    board.board[x][y] = "@"



def make_guess(board):
    """
    Takes in players guesses to place a missile on the board 
    and generates the computers guess
    """
    if board.type == "computer":
        row = int(input(f"Please enter a row between 1-{board.size}\n"))
        
        column = int(input(f"Please enter a column between 1-{board.size}\n"))
        
        board.board[row][column] = "-"
        
        return board
    else:
        row, column = random_point(board.size), random_point(board.size)
        board.board[row][column] = "-"
        return board


def play_game(player_board, computer_board):
    """
    Starts the game and displays player and computers boards
    """
    print(f"{player_board.name}'s board")
    player_board.print()

    print("+" * 20)

    print(f"{computer_board.name}'s board")
    computer_board.print()

    make_guess(computer_board)
    make_guess(player_board)

    print("-" * 40)

    play_game(player_board, computer_board)



def new_game():
    """
    Starts a new game.
    Sets the board size, number of ships and resets the scores
    """
    
    size = 5
    num_ships = 4
    scores["player"] = 0
    scores["computer"] = 0
    print("=" * 40)
    print("  Welcome to BATTLESHIPS")
    print(f"  Board size: {size}\n  Number of ships: {num_ships}")
    print("  Top left corner is row: 0, column: 0")
    print("-" * 40)
    player_name = input("What would you like to me called? \n")
    print("-" * 40)

    player_board = Board(size, num_ships, player_name, type="player")
    computer_board = Board(size, num_ships, "Computer", type="computer")

    for i in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(player_board, computer_board)


new_game()

