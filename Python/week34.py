"""
 * Challenge #34
 * THE MISSING NUMBERS
 * Difficulty: EASY
 *
 * Statement: Given a sorted array of integers with no repeats, create a function that computes
 * and returns all the missing ones between the largest and the smallest.
 * - Throws an error if the input array is not correct.

"""


def set_array(*args):
    try:
        if valid_array(args):
            return args
        else:
            raise ValueError
    except ValueError:
        exit(1)


def valid_array(numbers: list) -> bool:
    if len(numbers) != len(set(numbers)):
        print("There are repeated values")
        return False
    for n in numbers:
        if n is str:
            print(f"{n} is not a number")
            return False
    return True


def decorator(function):

    def wrapper():
        lowest, highest = function()
        i = 0
        between_numbers = [n for n in range(lowest, highest + 1)]
        for n in between_numbers:
            if n not in array:
                print(n, end="\t")
            else:
                i += 1
        if i == len(between_numbers):
            print("All if them are on your array")

    return wrapper


@decorator
def get_min_max() -> tuple:
    lowest: int = array[0]
    highest: int = array[0]
    for n in array:
        if lowest > n:
            lowest = n
        if highest < n:
            highest = n
    return lowest, highest


if __name__ == '__main__':
    array = set_array(1, 2, 7, 43, 3, 55)
    get_min_max()
