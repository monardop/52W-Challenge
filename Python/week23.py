"""
 * Reto #23
 * MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
 * Dificultad: MEDIA
 *
 * Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común
 múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
 *
"""


def valid_entry() -> int:
    while True:
        try:
            number = float(input("Insert a number: "))
            if int(number) != number:
                raise ValueError
        except ValueError:
            print("Wrong input")
        else:
            return int(number)
        

def factorization(a: int) -> list:
    divisors = []
    while True:
        if a % 2 == 0:
            divisors.append(2)
            a //= 2
        elif a % 3 == 0:
            divisors.append(3)
            a //= 3
        elif a % 4 == 0:
            divisors.append(4)
            a //= 4
        elif a % 5 == 0:
            divisors.append(5)
            a //= 5
        elif a % 9 == 0:
            divisors.append(9)
            a //= 9
        else:
            return divisors



def main():
    print(factorization(60))


main()
