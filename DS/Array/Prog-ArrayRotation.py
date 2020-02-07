def rotatebyone(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp

# O(d * n) time | O(1) space


def rotate(arr, d):
    for i in range(d):
        rotatebyone(arr)
    return arr


def gcd(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return gcd(b, a % b)

# Juggling algorithm
# O(n) time | O(1) space

def leftRotate(arr, d):
    n = len(arr)
    for i in range(gcd(d, n)):
        temp = arr[i]
        j = i
        while 1:
            k = j + d  # d = 2
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
            arr[j] = temp


# Optimized rotation by reverse algorithm
# O(n) time | O(1) space

def reverseArr(arr, start, end):
    watch = 0
    while start < end:
        watch += 1
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    print(f"watch: {watch}")


def rotateleft(arr, d):
    n = len(arr)
    reverseArr(arr, 0, d - 1)
    reverseArr(arr, d, n - 1)
    reverseArr(arr, 0, n - 1)
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(f"Rotation of {arr} is {rotateleft(arr, 2)}")
