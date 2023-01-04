"""
/*
 * Reto #25
 * PIEDRA, PAPEL, TIJERA
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
 *
"""


def win_check(player1: str, player2: str) -> str:
    if player1 == player2:
        return "Tie"
    winners = [('R', 'S'), ('S', 'P'), ('P', 'R')]
    if (player1, player2) in winners:
        return "Player 1 wins"
    else:
        return "Player 2 wins"


def valid_play() -> str:
    while True:
        try:
            a = input("Rock, Scissors or Paper: ").upper()
            if a not in ['R', 'S', 'P']:
                raise ValueError
            else:
                return a
        except (AttributeError, ValueError):
            print("R, S or P")


if __name__ == '__main__':
    print(win_check(valid_play(), valid_play()))

