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

if __name__ == '__main__':
    lst = u.getList()
    n = int(input('Enter the ith largest no: '))
    result = largest(lst[:], n)
    print(f'{n} largest of {lst} is {result}')