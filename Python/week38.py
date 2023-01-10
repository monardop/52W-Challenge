"""
An application that transforms binary numbers to decimals
"""


def get_number() -> str:
    while True:
        try:
            number = input("Insert a binary number: ")
            for bit in number:
                if bit not in ['1', '0']:
                    raise ValueError
        except ValueError:
            print("Wrong input, try again.")
        else:
            return number


def get_decimal(binary: str, sign_bit=False) -> int:
    bytes_used = 0
    is_negative = False
    if sign_bit:
        bytes_used = len(binary) - 2
        if binary.startswith('1'):
            is_negative = True
            binary = binary[1:]
            binary.replace("1", "", 1)
        else:
            is_negative = False
    else:
        bytes_used = len(binary) - 1

    decimal_number = 0
    for n in binary:
        decimal_number += int(n) * (2 ** bytes_used)
        bytes_used -= 1
    if is_negative:
        return decimal_number * -1
    else:
        return decimal_number


print(get_decimal("1101101"))
