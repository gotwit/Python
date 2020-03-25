# Solution 1
from collections import Counter


def findCommon(arr1, arr2, arr3):
    n1 = len(arr1)
    n2 = len(arr2)
    n3 = len(arr3)
    i, j, k = 0, 0, 0

    commonElements = []
    while i < n1 and j < n2 and k < n3:
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            commonElements.append(arr1[i])
            print(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    return commonElements


# Solution 2


def commonElement(arr1, arr2, arr3):
    # convert lists into dictionary
    arr1 = Counter(arr1)
    arr2 = Counter(arr2)
    arr3 = Counter(arr3)

    resultDict = dict(arr1.items() & arr2.items() & arr3.items())
    common = []

    for (key, val) in resultDict.items():
        for i in range(0, val):
            common.append(key)
    return common


arr1 = [1, 5, 5]
arr2 = [3, 4, 5, 5, 10]
arr3 = [5, 5, 10, 20]

# print("Common elements are ", findCommon(arr1, arr2, arr3))
print("Common elements are ", commonElement(arr1, arr2, arr3))
