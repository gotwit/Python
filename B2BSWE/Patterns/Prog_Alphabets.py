try:
    import sys, os
    sys.path.append(os.getcwd())
    from Utils import Prog_Utils as u
except Exception as e:
    print("Exception: ", e)

n = int(input("Enter no of test runs: "))

while n > 0:
    utils = u.Utils()
    rows, columns = utils.getMatrixSize()
    ucAlphaIdx = 65 # A
    lcAlphaIdx = 97 # a

    for row in range(rows):
        for col in range(columns):
            alphabet = chr(ucAlphaIdx + row)
            print(alphabet, end=" ")
        print()
    n = n - 1
