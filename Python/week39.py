"""
Quick Sort algorithm
"""
from random import randint
from time import time


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    new_partition = partition(array, start, end)
    quick_sort(array, start, new_partition - 1)
    quick_sort(array, new_partition + 1, end)


lista = []
start_time = time()
for n in range(1000):
    lista.append(randint(0, 1000))
quick_sort(lista, 0, len(lista) - 1)
print(lista)
elapsed_time = time() - start_time
print(f"Elapsed time: {elapsed_time}")



