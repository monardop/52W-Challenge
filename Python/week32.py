"""
 * Challenge #32
 * THE SECOND
 * Difficulty: EASY
 *
 * Statement: Given a list of numbers, find the largest SECOND.
 *
"""


def get_max(*args) -> int:
    numbers = args
    max_list = [0, 0]
    cambio = True
    while cambio:
        cambio = False
        for n in numbers:
            if n > max_list[0]:
                max_list[0] = n
                cambio = True
            elif (n > max_list[1] and
                  max_list[0] > n):
                max_list[1] = n
                cambio = True
    return max_list[1]


print(get_max(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(get_max(123, 34234, 3212, 656, 313, 77, 123))
