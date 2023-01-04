"""
* Reto #26
 * CUADRADO Y TRIÁNGULO 2D
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
"""


def draw_square(length: int) -> None:
    icon = '*'
    for n in range(0, length+1):
        if n in [0, length]:
            print(icon*length)
        else:
            print(f"{icon}{' '*(length-2)}{icon}")


def draw_triangle(length: int):
    icon = '*'
    for n in range(1, length+1):
        print(icon*n)


draw_square(int(input("Insert length: ")))
draw_triangle(int(input("Insert length: ")))
