try:
    import sys, os
    sys.path.append(os.getcwd())
    from Utils import Prog_Utils as u
except Exception as e:
    print("Exception: ", e)

utils = u.Utils()
n = utils.getNoOfRuns()

while n > 0:
    rows, columns = utils.getMatrixSize()

    for row in range(rows):
        for col in range(row + 1):
            print(col + 1, end=" ")
        print()
    n = n - 1