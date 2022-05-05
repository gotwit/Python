n = int(input("Enter no of test runs: "))

if n <= 0:
    print("Please enter valid no of test runs")

while n > 0:
    rows = int(input("Enter no of rows: "))
    columns = int(input("Enter no of columns: "))

    for row in range(1, rows+1):
        for col in range(1, columns+1):
            print(row, end=" ")
        print()

    n = n - 1