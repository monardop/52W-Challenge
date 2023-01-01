"""
 * TRES EN RAYA
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
 *
"""
from os import system


def check_status() -> int:
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
    game_board = [['', '', ''], ['', '', ''], ['', '', '']]
    show_game(game_board)
    return game_board


def valid_entry(game_board: list) -> tuple:
    """
    Check that the entry does not go outside the bounds and that it is not occupied.
    :param game_board:
    :return:
    """


def set_play(game_board: list, play: str) -> bool:
    """
    Set the player's choice
    :param game_board: the updated game-board
    :param play: Can be x or o.
    :return: Returns a boolean that sets whether the game has ended.

    """
    row, column = valid_entry(game_board)
    game_board[row][column] = play
    show_game(game_board)


