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

new_game()