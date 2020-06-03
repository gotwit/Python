def swapByPositions(array, pos1, pos2):
    array[pos1], array[pos2] = array[pos2], array[pos1]
    return array


array = [23, 65, 19, 90]
# print(f'Array {array} swapped by position to {swapByPositions(array, 0, 2)}')


def swapByPositions2(array, pos1, pos2):
    item1 = array.pop(pos1)
    item2 = array.pop(pos2-1)
    array.insert(pos1, item2)
    array.insert(pos2, item1)
    return array


# print(f'Array {array} swapped by position to {swapByPositions2(array, 0, 2)}')
