n = int(input("Enter no of test runs: "))

while n > 0:
    rows = int(input("Enter no of rows: "))
    columns = int(input("Enter no of columns: "))

    for row in range(1, rows+1):
        for col in range(1, columns+1):
            print(col, end=" ")
        print()
    n = n - 1