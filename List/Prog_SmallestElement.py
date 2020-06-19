try:
    import math
    import sys
    import os

    sys.path.append(os.getcwd())
    from Utils import Prog_Utils as u
except Exception as e:
    print(e)


def smallest(lst):
    return min(lst)

def smallest2(lst):
    lst.sort()
    return lst[:1]

def smallest3(lst):
    smallest = lst[0]
    for e in lst:
        if e < smallest:
            smallest = e
    return smallest

""" if __name__ == "__main__":
    lst = u.getList()
    result = smallest3(lst[:]) # copy of list passed as a parameter
    print(f'Smallest of {lst} is {result}\n') """

""" if __name__ == "__main__":
    lst = u.getList()
    result = smallest3(lst[:]) # copy of list passed as a parameter
    print(f'Smallest of {lst} is {result}\n') """

""" if __name__ == "__main__":
    lst = u.getList()
    result = smallest3(lst[:]) # copy of list passed as a parameter
    print(f'Smallest of {lst} is {result}\n') """


