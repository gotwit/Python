def reverseList(lst):
    return [ele for ele in reversed(lst)]


def reverseList2(lst):
    lst.reverse()

    return lst


def reverseList3(lst):
    newLst = lst[::-1]
    return newLst


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6]
    print(f'Reverse of {lst} is {reverseList(lst)}\n')

if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6]
    print(f'Reverse of {lst} is {reverseList2(lst)}\n')


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6]
