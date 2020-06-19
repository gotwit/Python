try:
    import sys, os
    sys.path.append(os.getcwd())

    from Utils import Prog_Utils as u
except Exception as e:
    print("Exception: ", e)

# Returns second largest list element
def largest(lst):
    lst.sort()
    newList = set(lst)
    newList.remove(max(newList))
    return max(newList)


def largest2(lst):
    lst.sort()
    return lst[-2]


def largest3(lst):
    highest = max(lst[0], lst[1])
    lowest = min(lst[0], lst[1])
    n = len(lst)

    for i in range(2, n):
        if lst[i] > highest:
            lowest = highest
            highest = lst[i]
        elif lst[i] > lowest and highest != lst[i]:
            lowest = lst[i]
        else:
            if highest == lowest:
                lowest = lst[i]

    return lowest


def largest4(lst):
    return sorted(lst)[-2]


if __name__ == '__main__':
    lst = u.getList()
    result = largest(lst[:])
    print(f'Second largest of {lst} is {result}\n')

    result = largest2(lst[:])
    print(f'Second largest of {lst} is {result}\n')

    result = largest3(lst[:])
    print(f'Second largest of {lst} is {result}\n')

    result = largest4(lst[:])
    print(f'Second largest of {lst} is {result}\n')
