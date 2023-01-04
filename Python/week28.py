"""
 * Challenge #28
 * Expend machine

 * Difficult : average
 *
 * Statement: Simulate the operation of a vending machine by creating an operation that receives money (coin array)
 and a number indicating product selection.
 * that receives money (array of coins) and a number indicating the product selection.
 * The program will return the name of the product and an array with the money back (with the least number of coins).
 * number of coins).
 * If the money is insufficient or the product number does not exist, this must be indicated with a message
 * and return all coins.
 * If there is no money back, the array is returned empty.
 * To make it simpler, we will work in cents with coins of 5, 10, 50, 100 and 200.
 * We must check that the coins sent are within the supported ones.
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
        change = f(*args, **kwargs)
        if change == 0:
            return []
        else:
            exchange_command = []
            for n in VALID_ENTRY:
                i = 0
                print(change)
                while change - n > 0:
                    print(f"en el while {change}")
                    change -= n
                    i += 1
                exchange_command.append((n, i))
            return exchange_command
    return wrap


@give_exchange
def get_money(value: float):
    inserted: float = 0
    while True:
        inserted = float(input("Insert: "))
        if inserted < value:
            print("Insufficient balance")
            inserted += float(input("Insert "))
        else:
            break
    if inserted != value:
        return inserted - value
    else:
        return 0


if __name__ == '__main__':
    selection = get_product(3)
    print(f"Your change: {get_money(selection[1])}")
    print(f"Take your {selection[0]}")
