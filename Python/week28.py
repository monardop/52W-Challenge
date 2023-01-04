"""
 * Reto #28
 * MÁQUINA EXPENDEDORA

 * Dificultad: MEDIA
 *
 * Enunciado: Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección del producto.
 * - El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor
 *   número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un mensaje
 *   y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
 *
"""


products = {
    1: ('Mints', 2.75),
    2: ('Candy', 1.30),
    3: ('Gum', 0.5),
    4: ('Water', 5.5),
    5: ('Juice', 6.10),
    7: ('Coke', 8.9),
    8: ('Sprite', 8.9),
    9: ('Bar', 3.3)
}
VALID_ENTRY = (2, 1, .5, .1, .05)


def get_product(number: int) -> tuple:
    print(f"Selected: {products[number][0]}")
    print(f"Insert {products[number][1]}")
    return products[number]


def give_exchange(f):
    def wrap(*args, **kwargs):
        change = f()
        if change == 0:
            return ()
        else:
            exchange_command = []
            for n in VALID_ENTRY:
                i = 0
                while change - n > 0:
                    change -= n
                    i += 1
                exchange_command.append((n, i))
            return tuple(exchange_command)


@give_exchange
def get_money(value: float):
    inserted: float = 0
    while True:
        inserted = float(input())
        if inserted % 0.05 != 0:
            print(f"We only accept: {VALID_ENTRY}")
        elif inserted < value:
            print("Insufficient balance")
        else:
            break
    if inserted != value:
        return value - inserted
    else:
        return 0


if __name__ == '__main__':
    selection = get_product(3)
