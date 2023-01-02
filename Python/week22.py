"""
 * Reto #22
 * CONJUNTOS
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
 *
"""


def get_array() -> list:
    array = input("Separate the values by commas: ")
    return array.split(',')


def intersection(array1, array2):
    values = []
    for n in array1:
        if n in array2:
            values.append()
    print(values)


def
