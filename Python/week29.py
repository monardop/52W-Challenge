"""
 * Challenge #29
 * ORDER THE LIST
 * Difficulty: EASY
 *
 * Statement: Create a function that sorts and returns an array of numbers.
 * - The function will receive a list (for example [2, 4, 6, 8, 9]) and an additional parameter.
 * "Asc" or "Desc" to indicate whether to sort from smallest to largest or from largest to smallest.
 * You cannot use the language's own functions to solve it automatically.
"""


class OwnList:
    def __init__(self, length: int):
        self.array = []
        for n in range(length):
            while True:
                try:
                    value = float(input("insert a number: "))
                except ValueError:
                    print("Not a valid number")
                else:
                    self.array.append(value)
                    break

    def bubble_order(self, asc=True):
        benchmark = len(self.array) - 1
        disordered = 1
        while disordered != 0:
            disordered = 0
            if asc:
                for i in range(benchmark):
                    if self.array[i] > self.array[i+1]:
                        aux = self.array[i]
                        self.array[i] = self.array[i+1]
                        self.array[i+1] = aux
                        disordered = i
                benchmark = disordered
            else:
                for i in range(benchmark):
                    if self.array[i] < self.array[i + 1]:
                        aux = self.array[i]
                        self.array[i] = self.array[i + 1]
                        self.array[i + 1] = aux
                        disordered = i
                benchmark = disordered
        return self.array


lista = OwnList(5)
print(lista.bubble_order(asc=False))
