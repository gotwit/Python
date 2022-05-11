n = int(input("Enter no of test runs: "))

while n > 0:
    rows = int(input("Enter no of rows: "))
    columns = int(input("Enter no of columns: "))

    for row in range(rows):
        for col in range(columns, row, -1):
            print(row + 1, end=" ")
        print()
    n = n - 1