"""
 * Reto #7
 * CONTANDO PALABRAS
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre
    el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""


def clean_phrase(phrase: str) -> str:
    for n in phrase:
        if n == "," or n == "." or n == "-" or n == ":":
            phrase = phrase.replace(n, " ")
    new_phrase = phrase.lower()
    return new_phrase


def count_words(phrase):
    word_list = set(phrase.split())
    for n in word_list:
        print(f"The word {n} appears {phrase.count(n)} times")


def main():
    phrase = input("Insert a phrase: ")
    new_phrase = clean_phrase(phrase)
    count_words(new_phrase)


if __name__ == "__main__":
    main()


