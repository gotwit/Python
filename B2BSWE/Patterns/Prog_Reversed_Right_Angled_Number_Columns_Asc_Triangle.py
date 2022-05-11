n = int(input("Enter no of test runs: "))

while n > 0:
    rows = int(input("Enter no of rows: "))
    columns = int(input("Enter no of columns: "))
    
    for row in range(rows):
        for col in range(0, columns - row):
            print(col + 1, end = " ")
        print()
    n = n - 1