n = int(input("Enter no of test runs: "))

while n > 0:
    rows = int(input("Enter no of rows: "))
    columns = int(input("Enter no of columns: "))

    for row in range(rows, 0, -1):
        # for col in range(columns, columns - row, -1):
        # for col in range(columns - row, columns):
        for col in range(row):
            print(row, end=" ")
        print()
    n = n - 1