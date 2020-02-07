def findRemainder(arr, n):
    # n = len(arr)
    mul = 1

    for i in arr:
        mul = (mul * (i % n)) % n
    return mul % n


arr = [100, 10, 5, 25, 35, 14]
n = 11
print(f"Remainder of array multiplication of {arr} is {findRemainder(arr, n)}")
