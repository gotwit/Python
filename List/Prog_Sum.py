def sumOfList(lst):
    return sum(lst)


def sumOfList2(lst):
    s = 0

    for element in lst:
        s = s + element
    return s


def sumOfList3(lst):
    total = 0

    for e in range(0, len(lst)):
        total += lst[e]

    return total


def sumOfList4(lst):
    total, i = 0, 0

    while i < len(lst):
        total += lst[i]
        i += 1

    return total


def sumOfList5(lst, size):
    if size == 0:
        return 0
    else:
        return lst[size-1]+sumOfList5(lst, size-1)


if __name__ == '__main__':
    lst = [4, 5, 1, 9, 13]
    print('sum of {} is {}\n'.format(lst, sumOfList(lst)))


if __name__ == '__main__':
    lst = [4, 5, 1, 9, 13]
    print('sum of {} is {}\n'.format(lst, sumOfList2(lst)))


if __name__ == '__main__':
    lst = [4, 5, 1, 9, 13]
    print('sum of {} is {}\n'.format(lst, sumOfList3(lst)))


if __name__ == '__main__':
    lst = [4, 5, 1, 9, 13]
    print('sum of {} is {}\n'.format(lst, sumOfList4(lst)))


if __name__ == '__main__':
    lst = [4, 5, 1, 9, 13]
    print('sum of {} is {}\n'.format(lst, sumOfList5(lst, len(lst))))
