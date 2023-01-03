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
            if number == 0:
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


def gcd(a: list, b: list) -> int:
    common_division = []
    divisors = set(a+b)
    result = 1

    for number in divisors:
        if number in b and number:
            if a.count(number) < b.count(number):
                common_division.append([number, a.count(number)])
            else:
                common_division.append([number, b.count(number)])

    for n in common_division:
        result *= pow(n[0], n[1])

    return int(result)


def lcm(a: int, b: int):
    return int(a*b/(gcd(factorization(a), factorization(b))))


def main():
    a = valid_entry()
    b = valid_entry()
    print(f"gcd: {gcd(factorization(a), factorization(b))}")
    print(f"LCM: {lcm(a, b)}")


main()
