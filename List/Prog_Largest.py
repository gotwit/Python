try:
    import math
    import sys
    import os

    sys.path.append(os.getcwd())
    from Utils import Prog_Utils as u
except Exception as e:
    print('Exception: ', e)

def largest(lst):
    lst.sort()
    return lst[-1]

def largest2(lst):
    return max(lst)

def largest3(lst):
    largest = lst[0]
    
    for e in lst:
        if e > largest:
            largest = e
    return largest

""" if __name__ == '__main__':
    lst = u.getList()
    result = largest(lst[:])
    print('Largest of {} is {}\n'.format(lst, result))
 """

""" f __name__ == '__main__':
    lst = u.getList()
    result = largest2(lst[:])
    print('Largest of {} is {}\n'.format(lst, result)) """


""" if __name__ == '__main__':
    lst = u.getList()
    result = largest3(lst[:])
    print('Largest of {} is {}\n'.format(lst, result)) """