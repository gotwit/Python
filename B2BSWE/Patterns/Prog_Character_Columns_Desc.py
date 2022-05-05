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
    ucAlphaIdx = 65 # A
    lcAlphaIdx = 97 # a

    for row in range(rows + ucAlphaIdx - 1, ucAlphaIdx - 1, -1):
        for col in range(columns + ucAlphaIdx - 1, ucAlphaIdx - 1, -1):
            alphabet = chr(col)
            print(alphabet, end=" ")
        print()
    n = n - 1