def interchange(array):
    size = len(array)
    temp = array[0]
    array[0] = array[size - 1]
    array[size - 1] = temp
    return array


array = [12, 35, 9, 56, 24]
# print(f'Array {array} interchanged to {interchange(array)}')


def interchange2(array):
    array[0], array[-1] = array[-1], array[0]
    return array


# print(f'Array {array} interchanged to {interchange2(array)}')

# Interchange elements using tuple variable
def interchange3(array):
    tupl = array[-1], array[0]
    array[0], array[-1] = tupl
    return array


# print(f'Array {array} interchanged to {interchange3(array)}')

""" a, *b, c, d = array
print(a)
print(b)
print(c)
print(d)
 """

# Interchange elements using starred expression and mandatory expression


def interchange4(array):
    first, *middle, last = array
    array = [last, *middle, first]
    return array


# print(f'Array {array} interchanged to {interchange4(array)}')


def interchange5(array):
    first = array.pop(0)
    last = array.pop(-1)
    array.insert(0, last)
    array.append(first)
    return array


# print(f'Array {array} interchanged to {interchange5(array)}')
