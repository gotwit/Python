try:
    import sys, os

    sys.path.append(os.getcwd())
    from Utils import Prog_Utils as u
except Exception as e:
    print('Exception: ', e)


def largest(lst, n):
    size = len(lst)

    if n > size:
        return 0
        
    lst.sort()
    return lst[-1*n]

# N largest elements
def largest2(lst, n):
    lst.sort()
    return lst[-n:]


def largest3(lst, n):
    newList = []

    for i in range(0, n):
        max = 0
        for j in range(len(lst)):
            if lst[j] > max:
                max = lst[j]
        lst.remove(max);
        newList.append(max);
    return newList

""" if __name__ == '__main__':
    lst = u.getList()
    n = int(input('Enter the ith largest no: '))
    result = largest(lst[:], n)
    print(f'{n} largest of {lst} is {result}') """


""" if __name__ == '__main__':
    lst = u.getList()
    n = int(input('Enter the ith largest no: '))
    result = largest2(lst[:], n)
    print(f'{n} largest of {lst} is {result}') """


if __name__ == '__main__':
    lst = u.getList()
    n = int(input('Enter the ith largest no: '))
    result = largest3(lst[:], n)
    print(f'{n} largest of {lst} is {result}')