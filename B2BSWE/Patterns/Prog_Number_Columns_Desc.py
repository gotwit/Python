try:
    import sys, os
    sys.path.append(os.getcwd())
    # from Utils.Prog_Utils import Utils
    from Utils import Prog_Utils as u
except Exception as e:
    print("Exception: ", e)

n = int(input("Enter no of test runs: "))

while(n > 0):
    utils = u.Utils() #Utils()
    rows, columns = utils.getMatrixSize()

    for row in range(rows, 0, -1):
        for col in range(columns, 0, -1):
            print(col, end=" ")
        print()
    n = n - 1