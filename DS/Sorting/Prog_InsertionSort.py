# Worst: O(n^2) time | O(1) space
# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space


def insertionSort(array):
    n = len(array)

    for i in range(1, n):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


""" array = [8, 5, 2, 9, 5, 6, 3]
print(insertionSort(array)) """
