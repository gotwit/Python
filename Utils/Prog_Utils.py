def getList():
    lst = []
    n = int(input("Enter the size of list: "))

    for i in range(0, n):
        element = None
        try:
            element = input("Enter an element: ")
        except Exception as e:
            print(f"Exception: {e}")
        lst.append(element)
    return lst

def getIntList():
    lst = []
    n = int(input("Enter the size of list: "))

    for i in range(0, n):
        element = None
        try:
            element = int(input("Enter an element: "))
        except Exception as e:
            print(f"Exception: {e}")
        lst.append(element)
    return lst

def funcType(name, x):
    switch = {
        int: lambda x: int(x),
        float: lambda x: float(x),
        str: lambda x: str(x)
    }
    default = None
    return switch.get(name, default)

def getListV2():
    lst = []
    n = int(input("Enter the size of list: "))

    for i in range(0, n):
        element = None
        try:
            element = input("Enter an element: ")

            element = funcType(element.__class__.__name__, element)
        except Exception as e:
            print(f"Exception: {e}")
        lst.append(element)
    return lst

class Utils:
    # def __init__(self):
    #     pass

    def getMatrixSize(self):
        rows = int(input("Enter no of rows: "))
        columns = int(input("Enter no of columns: "))

        return (rows, columns)