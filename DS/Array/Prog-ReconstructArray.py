def reconstruct(arr, m):
    n = len(arr)

    for i in range(1, n):
        arr[i] = (arr[i - 1] + 1) % m
    return arr


def construct(arr, m):
    n = len(arr)
    ind = 0
    for i in range(n):
        if arr[i] != -1:
            ind = i
            break

    for i in range(ind-1, -1, -1):
        if arr[i] == -1:
            arr[i] = (arr[i + 1] - 1 + m) % m

    for i in range(ind + 1, n):
        if arr[i] == -1:
            arr[i] = (arr[i - 1] + 1) % m
    return arr


arr = [5, -1, -1, 1, 2, 3]
m = 7
result = reconstruct(arr[:], m)

print("Reconstruct of {0} is {1}".format(arr, result))

print("Reconstruct of {0} is {1}".format(arr, reconstruct(arr.copy(), m)))

arr = [-1, -1, -1, 1, 2, 3]
print("Reconstruct of {0} is {1}".format(arr, construct(arr.copy(), m)))
