"""
 * Reto #24
 * ITERATION MASTER
 * Dificultad: FÁCIL
 *
 * Enunciado: Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno). ¿De cuántas maneras eres
 capaz de hacerlo? Crea el código para cada una de ellas.
"""
i = 1
while i != 101:
    print(i, end=" ")
    i += 1
print("")
for n in range(1, 101):
    print(n, end=" ")
print("")
numbers = [n for n in range(1, 101)]
print(numbers)