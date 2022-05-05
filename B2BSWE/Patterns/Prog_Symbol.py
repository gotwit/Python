n = int(input("Enter no of test runs: "))

if n <= 0:
    print("Please enter valid no of test runs")

while n > 0:
    rows = int(input("Enter no of rows: "))
    columns = int(input("Enter no of columns: "))
    symbol = input("Enter a symbol to print in matrix: ")

    for row in range(rows):
        for col in range(columns):
            print(symbol, end=" ")
        else:
            if columns <= 0:
                print("%d %s" %(columns, " is invalid column count"))
                break
        print() # print empty/ New line
    else:
        if rows <= 0:
            print("%d %s" %(rows, " is invalid row count"))
    n = n - 1