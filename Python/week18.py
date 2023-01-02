from os import system


def win_check(board: list, play: str) -> bool:
    """
    :param board: imports the updated board
    :param play: imports the actual player
    :return: True if the actual play is a winner, else false
    """
    # First check the diagonals
    win_sets = [[(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]
    for n in win_sets:
        cells_filled = 0
        for cells in n:
            row, column = cells
            if board[row][column] == play:
                cells_filled += 1
        if cells_filled == 3:
            return True

    # Now columns and rows
    for i in range(3):
        # First rows:
        row = 0
        for j in range(3):
            if board[i][j] == play:
                row += 1
        if row == 3:
            return True

        # Now the columns
        column = 0
        for j in range(3):
            if board[j][i] == play:
                column += 1
        if column == 3:
            return True

    return False


def check_status(board: list, play: str, turn: int) -> int:
    """
    Checks if the move is a winner or generates a draw.
    :return:
    1 for winner
    2 for draw
    0 if nothing happened
    """
    if win_check(board, play):
        return 1
    else:
        if turn == 7:
            return 2
    return 0


def show_game(board: list) -> None:
    """
    Cleans the console and displays the current game-board.
    """
    separator = "-"
    i = 0

    system('cls')
    for n in board:
        print(f" {n[0]} | {n[1]} | {n[2]} ")
        if i != 2:
            print(separator*11)
            i += 1


def set_game() -> list:
    """
    This function will create a clean game-board
    :return:
    game-board list.
    """
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    show_game(board)

    return board


def valid_entry(board: list) -> tuple:
    """
    Check that the entry does not go outside the bounds and that it is not occupied.
    :param board: Used to check that the selected cell is not occupied.
    :return: The verified row and column selection.
    """
    while True:
        try:
            row = int(input("Row: "))
            column = int(input("Column: "))
            for n in [row, column]:
                if n < 1 or n > 3:
                    raise ValueError
        except ValueError:
            print("Wrong entry")
        else:
            if board[row][column] != ' ':
                return row, column
            else:
                print("Cell already taken, try again")
                show_game(board)


def set_play(board: list, play: str, turn: int) -> int:
    """
    Set the player's choice
    :param board: the updated game-board
    :param play: Can be x or o.
    :param turn:
    :return: Returns a boolean that sets whether the game has ended.
    """
    row, column = valid_entry(board)
    board[row][column] = play
    show_game(board)
    return check_status(board, play, turn)


def main():
    game = set_game()
    turn = 1
    for play in ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']:
        print(f"Turn: {turn} - Player: {play}")



