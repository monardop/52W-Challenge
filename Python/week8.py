"""
/*
 * Reto #8
 * DECIMAL A BINARIO
 * Dificultad: FÁCIL

 * Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias
   del lenguaje que lo hagan directamente.
"""


def decimal_binary(number: int) -> list:
    decimal = []
    while True:
        decimal.append(number % 2)
        number //= 2
        if number // 2 == 0:
            decimal.append(1)
            break
    return decimal


def get_number() -> int:
    while True:
        try:
            number = int(input("Insert a integer number: "))
        except ValueError:
            print("Wrong input.")
        else:
            return number


def main():
    number: int = get_number()
    binary: list = decimal_binary(number)
    while len(binary) != 0:
        print(binary.pop(), end="")


if __name__ == '__main__':
    main()
