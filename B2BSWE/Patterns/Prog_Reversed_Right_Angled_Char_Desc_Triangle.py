import sys, os
sys.path.append(os.getcwd())
from Utils import Prog_Utils as u
import time


n = int(input("Enter no of test runs: "))

while n > 0:
    rows = int(input("Enter no of rows: "))
    columns = int(input("Enter no of columns: "))

    start = time.perf_counter()
    print("Start time: ", start)

    for row in range(rows):
        for col in range(columns - 1, row - 1, -1):
            char = chr(col + u.uppercaseIndex)
            print(char, end=" ")
        print()
    n = n - 1

    stop = time.perf_counter()
    print(f"Stop time: {stop}")
    time = stop - start
    print(f"Time: {time}")