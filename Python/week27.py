"""
 * Reto #27
 * VECTORES ORTOGONALES
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
 *
"""


def dot_product(vector1: list, vector2: list) -> int:
    scalar = 0
    for i, j in zip(vector1, vector2):
        scalar += i*j
    return scalar


def set_vector(dimension: int) -> list:
    vector = []
    for n in range(dimension):
        while True:
            try:
                value = int(input(f"Insert position {n+1}: "))
            except ValueError:
                print("Insert a number")
            else:
                vector.append(value)
                break
    return vector


if __name__ == '__main__':
    while True:
        try:
            dim = int(input("Insert the dimension/range: "))
        except ValueError:
            print("Wrong input")
        else:
            break
    if dot_product(set_vector(dim), set_vector(dim)) == 0:
        print("They are orthogonal")
    else:
        print("Not orthogonal")
