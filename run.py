from random import randint


class Board:
    """
    Main class for  the game board.
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
    of the board.
    """
    return randint(0, size - 1)


def count_hit_ships(board):
    """
    Counts amount of hit ships on a board.
    """
    count = 0
    for row in board.board:
        for column in row:
            if column == "X":
                count += 1
    return count


def validate(placement, board_size):
    """
    Validates players input choice for rows and columns.
    """
    while True:
        try:
            choice = int(input(f"Please enter a {placement}\n"))
            if choice <= board_size-1:
                print(f"You choose {choice}")
                return choice
            else:
                print(f"Please enter a number between 0-{board_size-1}")
        except ValueError:
            print(f"Please enter a number between 0-{board_size-1}")


def populate_board(board):
    """
    Populates game board with ships marked as "@".
    """
    x, y = random_point(board.size), random_point(board.size)
    while board.board[x][y] == "@":
        x, y = random_point(board.size), random_point(board.size)
    board.board[x][y] = "@"


def make_guess(board, display_board):
    """
    Takes in players guesses to place a missile on the board,
    generates the computers guess and updates the display board.
    """

    if board.type == "computer":
        row = "row"
        row = validate(row, board.size)

        column = "column"
        column = validate(column, board.size)

        if board.board[row][column] == ".":
            print("You missed! Try again")
            board.board[row][column] = "-"
            display_board.board[row][column] = "-"
        elif board.board[row][column] == "-":
            print("You missed! You tried there already. Pay attention")
        elif board.board[row][column] == "@":
            print("HIT! well done")
            board.board[row][column] = "X"
            display_board.board[row][column] = "X"
        return board, display_board

    else:
        row, column = random_point(board.size), random_point(board.size)
        if board.board[row][column] == "@":
            print("You have lost a ship!")
            board.board[row][column] = "X"
        else:
            board.board[row][column] = "-"
        return board, display_board


def play_game(player_board, computer_board, display_board, guesses):
    """
    Starts the game and displays player and computers boards.
    Keeps count of guesses and ends game when guesses goes to 0
    or when all ships are destroyed.
    """
    while guesses > 0:
        print(f"{player_board.name}'s board")
        player_board.print()

        print("+" * 20)

        print(f"{computer_board.name}'s board")
        display_board.print()

        make_guess(computer_board, display_board)
        make_guess(player_board, display_board)

        guesses -= 1

        print(f"You have {guesses} guesses left")

        player_hits = count_hit_ships(computer_board)
        computer_hits = count_hit_ships(player_board)

        if guesses == 0:
            print("You have run out of guesses")
            print("GAME OVER")
            exit()
        elif player_hits == computer_board.num_ships:
            print("***You beat the computer!***")
            print("GAME OVER")
            exit()
        elif computer_hits == player_board.num_ships:
            print("***You lost!***")
            print("GAME OVER")
            exit()

        play_game(player_board, computer_board, display_board, guesses)


def new_game():
    """
    Starts a new game.
    Sets the board size, number of ships and guesses.
    """

    num_ships = 4
    guesses = 10
    print("=" * 40)
    print("  *** Welcome to BATTLESHIPS ***")
    print("=" * 40)
    while True:
        try:
            print("Recommended board size: 5")
            size = int(input("Please enter the board size\n"))
            break
        except ValueError:
            print("Invalid input. Please try again")
    print(f"  Board size: {size}\n  Number of ships: {num_ships}")
    print(f"  Number of guesses: {guesses}")
    print("  Top left corner is row: 0, column: 0")
    print("-" * 40)
    print("@ = ship")
    print("X = sunk ship")
    print("- = missed guess")
    print("-" * 40)
    player_name = input("What would you like to me called? \n")
    print("-" * 40)

    player_board = Board(size, num_ships, player_name, type="player")
    computer_board = Board(size, num_ships, "Computer", type="computer")
    display_board = Board(size, num_ships, "display", type="display")

    for i in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(player_board, computer_board, display_board, guesses)


new_game()
