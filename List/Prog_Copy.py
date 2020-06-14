# Cloning or copying

# slicing


def cloneList(lst):
    newList = lst[:]
    return newList

# extend


def cloneList2(lst):
    newList = []
    # appends each element from iteratable object to end of new list
    newList.extend(lst)
    return newList

# list method


def cloneList3(lst):
    li_copy = list(lst)
    return li_copy


# comprehension

def cloneList4(lst):
    li_copy = [i for i in lst]
    return li_copy


# append

def cloneList5(lst):
    li_copy = []
    for e in lst:
        li_copy.append(e)
    return li_copy

# copy


def cloneList6(lst):
    li_copy = lst.copy()
    return li_copy


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f'By slicing List: {lst} Clone: {cloneList(lst)}')

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f'By extend List: {lst} Clone: {cloneList2(lst)}')

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f'By list method List: {lst} Clone: {cloneList3(lst)}')

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f'By comprehension List: {lst} Clone: {cloneList4(lst)}')


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f'By append List: {lst} Clone: {cloneList5(lst)}')


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f'By copy List: {lst} Clone: {cloneList5(lst)}')
