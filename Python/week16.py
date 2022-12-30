"""
 * Reto #16
 * EN MAYÚSCULA
 * Dificultad: FÁCIL

 * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""


def capitalize_letters(phrase: str):
    words = phrase.split()
    new_phrase = ""
    for word in words:
        word = word.replace(word[0], word[0].capitalize(), 1)
        new_phrase += word + " "
    print(new_phrase.strip())


capitalize_letters(input("Insert a phrase: "))
