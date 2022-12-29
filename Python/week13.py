"""
 * Reto #13
 * FACTORIAL RECURSIVO
 * Dificultad: FÁCIL
 *
 * Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
"""


def factorial(number: int, fact=1):
    if number - 1 == 0:
        return fact
    return factorial(number - 1, fact * number)


def valid_number() -> int:
    while True:
        try:
            number = int(input("Insert a number: "))
            if number < 0:
                raise ValueError
        except ValueError:
            print("That's not a valid number")
        else:
            return number


def main():
    number = valid_number()
    if number == 0:
        print("1")
    else:
        print(factorial(number))
    return 0


if __name__ == '__main__':
    main()
