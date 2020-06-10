def clearList(lst):
    newList = lst[:]  # copy original list
    print('List: ' + str(lst))
    lst.clear()
    print('Clear list using "clear" method: ' + str(lst))

    lst = newList
    print('List: ' + str(lst))
    lst = []
    print('Clear list assigning empty "[]": ' + str(lst))

    # To avoid clearing references, use copy() or [:]
    lst = newList.copy()
    print('List: ' + str(lst))
    lst *= 0
    print('Clear list by assinging "*=0": ' + str(lst))

    # clear's references as well
    lst = newList
    print('List: ' + str(lst))
    del lst[:]
    print('Clear list by "del": ' + str(lst))


if __name__ == '__main__':
    lst = [6, 9, 1, 0, 4]

    clearList(lst)
