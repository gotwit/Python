def largest(arr, n):
    _max = arr[0]

    for i in range(1, n):
        if arr[i] > _max:
            _max = arr[i]
    return _max


arr = [10, 324, 45, 90, 9809]
n = len(arr)
ans = largest(arr, n)
print('Largest element in array %s' % ans)
