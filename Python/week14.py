"""
* Reto #14
 * ¿ES UN NÚMERO DE ARMSTRONG?
 * Dificultad: FÁCIL
 *
 * Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
"""


def is_narcissistic(number: int) -> bool:
    power = len(str(number))
    value = 0
    for digit in str(number):
        value += int(digit)**power
    return value == number


print(is_narcissistic(int(input("Insert a number: "))))
