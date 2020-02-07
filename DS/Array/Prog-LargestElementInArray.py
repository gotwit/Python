
def findlargest(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max


def findLargest(arr):
    n = len(arr)
    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [10, 20, 4]
print(f"Largest element of {arr} is {findLargest(arr)}")
