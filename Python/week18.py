from os import system


def check_status(game_board: list) -> int:
    """
    Checks if the move is a winner or generates a draw.
    :return:
    1 for winner
    2 for draw
    0 if nothing happened
    """
    


def show_game(game_board: list) -> None:
    """
    Cleans the console and displays the current game-board.
    """
    separator = "-"
    i = 0

    system('cls')
    for n in game_board:
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
    game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    show_game(game_board)

    return game_board


def valid_entry(game_board: list) -> tuple:
    """
    Check that the entry does not go outside the bounds and that it is not occupied.
    :param game_board: Used to check that the selected cell is not occupied.
    :return: The verified row and column selection.
    """
    while True:
        try:
            row = int(input("Row: "))
            column = int(input("Column: "))

        except ValueError:
            print("Wrong entry")
        else:
            if game_board[row][column] != ' ':
                return row, column
            else:
                print("Cell already taken, try again")
                show_game(game_board)


def set_play(game_board: list, play: str) -> int:
    """
    Set the player's choice
    :param game_board: the updated game-board
    :param play: Can be x or o.
    :return: Returns a boolean that sets whether the game has ended.
    """
    row, column = valid_entry(game_board)
    game_board[row][column] = play
    show_game(game_board)
    return check_status(game_board)
