"""
Quick Sort algorithm
"""


def quicksort(unsorted_list):

    if len(unsorted_list) > 2:
        v = unsorted_list[0] + unsorted_list[len(unsorted_list) - 1] + unsorted_list[len(unsorted_list) - 1 / 2] / 3
    elif len(unsorted_list) == 2:
        v = unsorted_list[0] + unsorted_list[1] / 2
    else:
        v = unsorted_list[0]

    return quicksort(filter((lambda y: y < v), unsorted_list)) \
        + [v] \
        + quicksort(filter((lambda y: y >= v), unsorted_list))


print(quicksort([9,4,2,3,1,5,6]))
