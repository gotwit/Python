from bisect import bisect_left


def checkElementExists(lst, n):
    for i in lst:
        if i == n:
            return True
    return False


def checkElementExistsBySet(lst, n):
    newList = set(lst)

    if n in newList:
        return True
    return False


def checkElementExistByBisect(lst, n):
    if bisect_left(lst, n):
        return True
    return False


if __name__ == '__main__':
    lst = [10, 20, 30, 40, 50]
    n = int(input("Please enter search element\n"))
    foundElement = checkElementExists(lst, n)

    if foundElement:
        print('Found %(searchElement)s element\n' % {"searchElement": n})
    else:
        print('Element %(searchElement)s not found\n' % {"searchElement": n})

    list_set = [1, 6, 3, 5, 3, 4]
    foundElement = checkElementExistsBySet(list_set, n)

    if foundElement:
        print('Found %(searchElement)s element\n' % {"searchElement": n})
    else:
        print('Element %(searchElement)s not found\n' % {"searchElement": n})

    list_bisect = [1, 6, 3, 5, 3, 4]
    foundElement = checkElementExistByBisect(list_bisect, n)

    if foundElement:
        print('Found %(searchElement)s element\n' % {"searchElement": n})
    else:
        print('Element %(searchElement)s not found\n' % {"searchElement": n})
