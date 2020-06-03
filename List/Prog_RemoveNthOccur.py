def removeOccurrence(lst, word, occurrances):
    newList = []
    count = 0

    for item in lst:
        if item == word:
            count = count + 1
            if count != occurrances:
                newList.append(item)
        else:
            newList.append(item)
    # return False if count == 0 else True
    return newList


def removeOccurrence2(lst, word, n):
    count = 0

    for i in range(0, len(lst)):
        if lst[i] == word:
            count += 1
            if count == n:
                del(lst[i])
                return True
    return False


def removeOccurrence3(lst, word, n):
    count = 0
    index = 0
    for i in range(len(lst)):
        index += 1
        if lst[i] == word:
            count += 1
            if count == n:
                lst.pop(index - 1)
                return True
    return False


if __name__ == '__main__':
    lst = ["I", "am", "you", "I", "am", "the", "rowdy", "you", "I", "am",
           "you", "I", "am", "the", "row", "row", "rowdy", "you", "Rowdy"]
    word = "I"
    n = 1
    # print("Update list : ", removeOccurrence(lst, word, n))
    flag = removeOccurrence3(lst, word, n)

    if flag:
        print("Update list : ", lst)
    else:
        print("Item not found")
