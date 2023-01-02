"""
 * Reto #21
 * CALCULADORA .TXT
 * Dificultad: MEDIA

 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
 * - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
 *
 * Informar
"""
from sys import argv

try:
    open(argv[1], "r")
except FileNotFoundError:
    print("file not found")
    exit(1)
with open(argv[1], "r") as f:
    operations = f.readlines()
for n in operations:
    n.strip()
for equation in operations:
    num = []
    for n in equation:
        if n != '+' or n != '-' or n != '*' or n != '/':
            num.append(n)
        else:
            operator = n
    a = int("".join(num[0]))
    b = int("".join(num[1]))
    if operator == '+':
        print(a+b)
    elif operator == '-':
        print(a-b)
    elif operator == '*':
        print(a*b)
    elif operator == '/':
        print(a/b)
    del num
