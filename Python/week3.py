"""
 * ¿ES UN NÚMERO PRIMO?
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 *
"""

def main():
    print("Insertar un número, se darán 100 números con el suyo como centro")
    while True:
        try: 
            num = int(input("Insertar un numero: "))
            if num is not int:
                raise TypeError
            else:
                break
        except TypeError:
            print("Eso no es un número.")
