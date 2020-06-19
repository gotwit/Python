def getList():
    lst = []
    n = int(input("Enter the size of list: "))

    for i in range(0, n):
        e = int(input("Enter an element: "))
        lst.append(e)
    return lst