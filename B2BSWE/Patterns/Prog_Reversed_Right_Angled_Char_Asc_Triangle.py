import sys, os, time
sys.path.append(os.getcwd())
from Utils import Prog_Utils as u

n = int(input("Enter no of test runs: "))

start = time.perf_counter()
print("Start time: ", start)

while n > 0:
    rows = int(input("Enter no of rows: "))
    columns = int(input("Enter no of columns: "))



    for row in range(rows):
        for col in range(0, columns - row):
            char = chr(col + u.uppercaseIndex)
            print(char, end=" ")
        print()
    n = n - 1

stop = time.perf_counter()
print(f"Stop time: {stop}")
time = stop - start
print(f"Time: {time}")