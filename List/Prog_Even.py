try:
    import sys, os

    sys.path.append(os.getcwd())
    from Utils import Prog_Utils as u
except Exception as e:
    print('Exception: ', e)

def even(lst):
    evens = []

    for ele in lst:
        if ele % 2 == 0:
            evens.append(ele)
    return evens

def even2(lst):
    n = len(lst)
    i = 0
    evens = []
    
    while i < n:
        if lst[i] % 2 == 0:
            evens.append(lst[i])
        i = i + 1
    return evens


def even3(lst):
    evens = [e for e in lst if e % 2 == 0]
    return evens


def even4(lst):
    evens = list(filter(lambda x: (x % 2 == 0), lst))
    return evens

if __name__ == '__main__':
    lst = u.getList()
    result = even(lst)
    print(f'{lst} has even nos {result}')


if __name__ == '__main__':
    lst = u.getList()
    result = even2(lst)
    print(f'{lst} has even nos {result}')


if __name__ == '__main__':
    lst = u.getList()
    result = even3(lst)
    print(f'{lst} has even nos {result}')


if __name__ == '__main__':
    lst = u.getList()
    result = even4(lst)
    print(f'{lst} has even nos {result}')