import time

n = int(input("Enter no of test runs: "))

start = time.perf_counter()

while n > 0:
    rows = int(input("Enter no of rows: "))
    columns = int(input("Enter no of columns: "))

    # Solution 1
    # for row in range(rows):
    #     for col in range(columns):
    #         if (row + col) >= (columns - 1):
    #             print("*", end=" ")
    #         else:
    #             print(" ", end=" ")
    #     print()

    # Solution 2
    # for row in range(rows):
    #     spaceLength = columns - (row + 1)
    #     for s in range(spaceLength):
    #         print(" ", end=" ")
    #     for col in range(spaceLength, columns):
    #         print("*", end=" ")
    #     print()

    # Solution 3
    for row in range(rows):
        for s in range(columns - 1, row, -1): # space loop
            print(" ", end=" ")
        for col in range(0, row + 1):
            print("*", end=" ")
        print()
    n = n - 1

stop = time.perf_counter()
print("Elapse time: ", stop, start)
elapsedTime = stop - start
print(f"Elapsed time during the whole program in seconds: {elapsedTime}")