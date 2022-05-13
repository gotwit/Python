import sys, os
sys.path.append(os.getcwd())
from Utils import Prog_Utils as u
import time

n = int(input("Enter no of test runs: "))

start = time.perf_counter()
# print("Start time: ", start)

while n > 0:
    rows = int(input("Enter no of rows: "))
    columns = int(input("Enter no of columns: "))


    for row in range(rows, 0, -1):
        # for col in range(row):
        for col in range(columns, rows - row, -1):
            char = chr(row - 1 + u.uppercaseIndex)
            print(char, end=" ")
        print()
    n = n - 1

stop = time.perf_counter()
# print(f"Stop time: {stop}")
print("Elapsed time: ", stop, start)
elapsedTime = stop - start
print(f"Elapsed time during the whole program in seconds: {elapsedTime}")