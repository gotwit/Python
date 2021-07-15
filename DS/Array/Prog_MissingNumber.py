# Time O(N) | Space O(1)
def missingNumber(arr, n):
    distinct = 1
    i = 0
    size = n-1

    while(i < size):
        if arr[i] != distinct:
            return distinct
        distinct = distinct + 1
        i = i + 1

arr = [1, 2, 3, 5]
n = 5

missingNum = missingNumber(arr, n)
print(missingNum)