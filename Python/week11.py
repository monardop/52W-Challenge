"""
 * Reto #11
 * ELIMINANDO CARACTERES
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima
    otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
"""


def get_str():
    str1 = input("Input 1: ")
    str2 = input("Input 2: ")
    return str1, str2


def out(phrase1: str, phrase2: str) -> set:
    char_set = set()
    for n in phrase1:
        if n not in phrase2:
            char_set.add(n)
    return char_set


def main():
    phrase1, phrase2 = get_str()
    print(f"The difference between str1 and str2 is: {out(phrase1, phrase2)}")
    print(f"The difference between str2 and str1 is: {out(phrase2, phrase1)}")
    return 0


if __name__ == '__main__':
    main()
