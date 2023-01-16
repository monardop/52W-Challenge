"""
 Enunciado: Dado un array de números enteros positivos, donde cada uno
 * representa unidades de bloques apilados, debemos calcular cuantas unidades
 * de agua quedarán atrapadas entre ellos.
"""
from random import randint

blocks = []
for n in range(20):
    blocks.append(randint(0, 20))
print(blocks)
max_height = max(blocks)
water = 0
for n in blocks:
    water += max_height - n
print(f"{water}lts of water")

for n in range(max_height + 1, 0):
    for stage in blocks:
        if stage >= n:
            print("T")
        else:
            print(':')
