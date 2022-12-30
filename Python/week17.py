"""
 * Reto #17
 * LA CARRERA DE OBSTÁCULOS
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
 *        variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 *
"""


def game_set() -> str:
    print("The game is set with two values: _ floor, | jump")
    while True:
        try:
            game = input("Set the game: ")
            for n in game:
                if n != "_" or n != "|":
                    break
            else:
                raise ValueError
        except ValueError:
            print("Wrong entry")
        else:
            return game


def load_player(game: str):
    player_name = input("Insert player's name: ")
    play = ""
    for section in game:
        option = ""
        while True:
            try:
                option = input("Did s/he jump or run? ").lower()
                if option != "jump" and option != "run":
                    raise ValueError
            except ValueError:
                print("Wrong entry")
            else:
                break
        

