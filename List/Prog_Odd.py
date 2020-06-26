try:
    import sys, os

    sys.path.append(os.getcwd())
    from Utils import Prog_Utils as u
except Exception as e:
    print('Exception: ', e)


def odd(lst):
    odds = []

    for e in lst:
        if e % 2 != 0:
            odds.append(e)
    return odds


def odd2(lst):
    odds = []
    n = len(lst)
    i = 0

    while i < n:
        if lst[i] % 2 != 0:
            odds.append(lst[i])
        i = i + 1
    return odds


def odd3(lst):
    odds = [e for e in lst if e % 2 != 0]
    return odds

def odd4(lst):
    odds = list(filter(lambda x: x % 2 != 0, lst))
    return odds


""" if __name__ == '__main__':
    lst = u.getList()
    result = odd(lst)
    print(f'{lst} has odd nos {result}') """


""" if __name__ == '__main__':
    lst = u.getList()
    result = odd2(lst)
    print(f'{lst} has odd nos {result}') """


""" if __name__ == '__main__':
    lst = u.getList()
    result = odd3(lst)
    print(f'{lst} has odd nos {result}') """


""" if __name__ == '__main__':
    lst = u.getList()
    result = odd4(lst)
    print(f'{lst} has odd nos {result}') """