from collections import OrderedDict

# Solution 1


def checkOrder(str, patt):
    dict = OrderedDict.fromkeys(str)

    if len(str) < len(patt):
        return 'false'

    patlen = 0

    for key, value in dict.items():
        if key == patt[patlen]:
            patlen = patlen + 1

        if patlen == len(patt):
            return 'true'

    return 'false'

# Solution 2


def checkPattern(str, patt):
    l = len(patt)

    if len(str) < l:
        return False

    for i in range(l - 1):
        x = patt[i]
        y = patt[i + 1]
        last = str.rindex(x)
        first = str.index(y)

        if last == -1 or first == -1 or last > first:
            return False
    return True

# Solution 3


def followPattern(str, patt):
    patternSet = set()

    for i in range(len(patt)):
        patternSet.add(patt[i])

    modifiedStr = str

    for i in range(len(str) - 1, -1, -1):
        if not modifiedStr[i] in patternSet:
            modifiedStr = modifiedStr[:i] + modifiedStr[i + 1:]

    for i in range(len(modifiedStr) - 1, 0, -1):
        if modifiedStr[i] == modifiedStr[i - 1]:
            modifiedStr = modifiedStr[:i] + modifiedStr[i + 1:]

    if len(patt) != len(modifiedStr):
        return False

    for i in range(len(patt)):
        if patt[i] != modifiedStr[i]:
            return False
    return True


if __name__ == "__main__":
    str = "engineers rock"
    patt = "er"
    print("Expected: True, Actual: ", followPattern(str, patt))

    str = "engineers rocks"
    patt = "egr"
    print("Expected: False, Actual: ", followPattern(str, patt))

    str = "engineers rocks"
    patt = "gsr"
    print("Expected: False, Actual: ", followPattern(str, patt))

    str = "engineers rocks"
    patt = "eger"
    print("Expected: True, Actual: ", followPattern(str, patt))

""" 
str = "engineers rocks"
patt = "egr"
print(checkOrder(str, patt))


str = "engineers rocks"
patt = "gsr"
print(checkPattern(str, patt)) """
