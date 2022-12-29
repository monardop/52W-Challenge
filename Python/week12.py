"""
 * Reto #12
 * ¿ES UN PALÍNDROMO?
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
"""


def palindrome_check(phrase: str) -> bool:
    phrase = phrase.replace(" ", "").lower()
    aux_phrase = phrase[::-1]
    return phrase == aux_phrase


print(palindrome_check(input("Inserte una frase: ")))
