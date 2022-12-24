"""
 * ¿ES UN NÚMERO PRIMO?
 * Dificultad: MEDIA
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 *
"""
def prime_number(number: int) -> bool:
    for n in range(2,number):
        if number%n == 0 and number != 2:
            return False
    return True 

def create_list(num: int)-> None:
    if num < 102:
        for n in range(2,100):
            if prime_number(n):
                print(n, end="  ")
    else: 
        for n in range(num-100, num+1):
            if prime_number(n):
                print(n, end="  ")

def main():
    while True:
        num = input("Insertar un numero: ")
        try: 
            num = int(num)
        except ValueError:
            print("Eso no es un número.")
        else:
            break
    if prime_number(num):
        print("Es primo")
        create_list(num)
    else:
        print("No es primo")

if __name__ == "__main__":
    main()