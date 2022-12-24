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
        num = input("Insertar un numero: ")
        try: 
            num = int(num)
        except ValueError:
            print("Eso no es un número.")
        else:
            break

if __name__ == "__main__":
    main()