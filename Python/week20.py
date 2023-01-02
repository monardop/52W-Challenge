"""
 * Reto #20
 * PARANDO EL TIEMPO
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir,
    sin detener la ejecución del programa principal. Se podría ejecutar varias veces al mismo tiempo.
 *
"""
from time import sleep
from os import system

while True:
    try:
        a = int(input("Insert first value: "))
        b = int(input("Insert second value: "))
    except ValueError:
        print("Wrong input")
    else:
        break
print(f"Now, you'll see how much it is {a}+{b}")
sleep(2)
system('cls')
print("Almost there")
sleep(3)
system('cls')
print("A little bit difficult jeje...")
sleep(4)
system('cls')
print("Yeah...I know how to do it, just let me...")
sleep(2)
system('cls')
print(f"I KNOW, IT IS {int(a + b * 1.8)}")
sleep(3)
system('cls')
print(f"Just joking, it is {a+b}")