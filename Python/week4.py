"""
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 *
"""
def valid_number(msg:str)-> int:
    while True:
        try:
            number = int(input(msg))
            if number < 0: 
                raise ValueError
        except ValueError:
            print("Entrada incorrecta")
        else:
            return number
def triangle():
    base = valid_number("Set a base: ")
    height = valid_number("Set the height: ")
    print((base*height)/2)
def square():
    base = valid_number("Set one of its sides: ")
    print(base**2)
def rectangle():
    base = valid_number("Set a base: ")
    height = valid_number("Set the height: ")
    print(base*height)

def main():
    while True:
        try:
            op = int(input("Select:\n1 - Triangle \n2- Square\n3- Rectangle\nNum: "))
            if op == 1:
                triangle()
            elif op ==2:
                square()
            elif op ==3:
                rectangle()
            else: 
                raise ValueError
        except ValueError:
            print("Error, try again.")
        else:
            exit(1)
if __name__ == '__main__':
    main()