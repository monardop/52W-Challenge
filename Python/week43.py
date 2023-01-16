"""
 * Enunciado: Crea una función que retorne el número total de bumeranes de
 * un array de números enteros e imprima cada uno de ellos.
"""
from random import randint

list_of_numbers = []
for n in range(100):
    list_of_numbers.append(randint(1, 9))
print(list_of_numbers)
print("Boomerangs found")
for n in range(97):
    if list_of_numbers[n] == list_of_numbers[n+2] != list_of_numbers[n+1]:
        print(f"[{list_of_numbers[n]}, {list_of_numbers[n+1]}, {list_of_numbers[n+2]}]")
