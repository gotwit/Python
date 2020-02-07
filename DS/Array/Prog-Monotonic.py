def isMonotonic(arr):
    n = len(arr)
    increasingMonotonic = False
    decreasingMonotonic = False

    for i in range(n - 2):
        if arr[i] <= arr[i + 1]:
            increasingMonotonic = True
        else:
            increasingMonotonic = False
            break

    for i in range(n - 2):
        if arr[i] >= arr[i + 1]:
            decreasingMonotonic = True
        else:
            decreasingMonotonic = False
            break

    return increasingMonotonic or decreasingMonotonic


def checkMonotonic(arr):
    n = len(arr)
    # https://docs.python.org/3/library/functions.html#all
    return all(True if arr[i] <= arr[i+1] else False for i in range(n-2)) or all(True if arr[i] >= arr[i+1] else False for i in range(n-2))


arr1 = [6, 8, 4, 4]
# arr1 = [6, 5, 4, 4]
# arr1 = [1, 2, 3, 4]
# arr1 = [1, 4, 3, 2]
result1 = "is " if isMonotonic(arr1[:]) else "isn't"
print(f"{arr1} array {result1} monotonic")

# arr2 = [6, 8, 4, 4]
# arr2 = [6, 5, 4, 4]
# arr2 = [1, 2, 3, 4]
arr2 = [1, 4, 3, 2]
result2 = "is " if checkMonotonic(arr2[:]) else "isn't"
print(f"{arr2} array {result2} monotonic")


# Python program to demonstrate ternary operator
a, b = 10, 20

# Use tuple for selecting an item
print((b, a)[a < b])

# Use Dictionary for selecting an item
print({True: a, False: b}[a < b])

# lamda is more efficient than above two methods
# because in lambda  we are assure that
# only one expression will be evaluated unlike in
# tuple and Dictionary
print((lambda: b, lambda: a)[a < b]())
