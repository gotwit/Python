def sumofarray(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum


arr = [1, 2, 4]
print(f"Sum of array: {arr} is {sumofarray(arr)}")
