"""
 * Challenge #30
 * WORD FRAME

 * Difficulty: EASY
 *
 * Statement: Create a function that receives a text and displays each word on a line,
 forming a rectangular frame of asterisks.
 * a rectangular frame of asterisks.
"""


def get_length(elements: list) -> int:
    max_len = 0
    for element in elements:
        if len(element) > max_len:
            max_len = len(element)
    return max_len


def draw_square(phrase: str) -> None:
    icon = '*'
    aux_phrase = phrase.split()
    length = get_length(aux_phrase)

    for n, word in zip(range(length), aux_phrase):
        if n in [0, len(aux_phrase)]:
            print(icon*length)
        else:
            print(f"{icon}{' '*(length-2)}{icon}")

