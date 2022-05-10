n = int(input("Enter no of test runs: "))

while n > 0:
    rows = int(input("Enter no of rows: "))
    columns = int(input("Enter no of columns: "))
    ucAlphaIdx = 65 # A
    lcAlphaIdx = 97 # a

    for row in range(rows):
        for col in range(row + 1):
            alphabet = chr(ucAlphaIdx + col)
            print(alphabet, end=" ")
        print()
    n = n - 1
