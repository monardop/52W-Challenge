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


def load_player(game: str) -> tuple:
    player_name = input("Insert player's name: ")
    play = ""
    for section in game:
        option = ""
        while True:
            try:
                option = input("Did s/he jump or run? ").lower().strip()
                if option != "jump" and option != "run":
                    raise ValueError
            except ValueError:
                print("Wrong entry")
            else:
                break
        if option == "jump":
            if section == "_":
                play += "x"
            else:
                play += "o"
        if option == "run":
            if section == "|":
                play += "/"
            else:
                play += "o"
    return player_name, play


def point_count(player: tuple) -> int:
    name, result = player
    errors = 0
    for n in result:
        if n != "o":
            errors += 1
    print(f"The player {name} made {errors}/{len(result)} mistakes")
    return errors


def continue_menu() -> bool:
    while True:
        try:
            ans = int(input("To continue adding players, insert 1, else insert 0: "))
            if ans == 1:
                return True
            elif ans == 0:
                return False
            else:
                raise ValueError
        except ValueError:
            print("Wrong entry")


def score(participants: list) -> None:
    participants = participants.sort(key=participants[1])
    print(participants)


def main():
    print("First, let's set the game")
    game = game_set()
    add = True
    participants = []

    while add:
        player = load_player(game)
        errors = point_count(player)
        participants.append([player[0], errors]) # player[0] = player's name
        add = continue_menu()

    if len(participants) > 1:
        score(participants)

    return 0


if __name__ == '__main__':
    main()

# TODO: correct the scoreboard
