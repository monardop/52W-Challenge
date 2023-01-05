"""
 * Challenge #30
 * WORD FRAME
 * Difficulty: EASY
 *
 * Statement: Create a function that receives a text and displays each word on a line,
 forming a rectangular frame of asterisks.
 * a rectangular frame of asterisks.
"""


def draw_square(phrase: str) -> None:
    aux_phrase = phrase.split()
    print(aux_phrase)
    print("x" * 20)
    for n in range(len(aux_phrase)):
        for space in range(21):
            if space == 0:
                print('x', end="")
            elif space == 20 - len(aux_phrase[n]):
                print('x')
            elif space == (10 - len(aux_phrase[n]) // 2):
                print(aux_phrase[n], end="")
            else:
                if space < 20 - len(aux_phrase[n]):
                    print(" ", end="")
    print("x" * 20)


draw_square("hello everybody in da world")
