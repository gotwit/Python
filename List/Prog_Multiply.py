import math
from functools import reduce

def mulList(lst):
    result = 1
    for e in lst:
        result = result * e
    return result

def mulList2(lst):
    return math.prod(lst)


def mulList3(lst):
    result = reduce((lambda x, y: x * y), lst)
    return result

if __name__ == '__main__':
    lst = [1, 2, 3]
    result = mulList(lst)
    print('Multiple of all the {} elements : {} \n'.format(lst, result))

if __name__ == '__main__':
    lst = [5, 3, 4]
    result = mulList2(lst)
    print('Multiple of all the {} elements : {} \n'.format(lst, result))

if __name__ == '__main__':
    lst = [1, 2, 3]
    result = mulList3(lst)
    print('Multiple of all the {} elements : {} \n'.format(lst, result))
