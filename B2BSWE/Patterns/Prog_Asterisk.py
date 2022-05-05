print("Enter no of rows and columns to print asterisk")
rows = int(input("Enter no of rows: "))
columns = int(input("Enter no of columns: "))

for row in range(rows):
    for col in range(columns):
        print("*", end="")
    print(end="\n")
