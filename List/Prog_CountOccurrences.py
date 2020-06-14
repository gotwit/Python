def countOccurrences(lst, x):
    count = 0
    for e in lst:
        if x == e:
            count += 1
    return count


if __name__ == '__main__':
    lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
    x = int(input("Enter a number to find occurrences: "))
    occurrence = countOccurrences(lst, x)
    print(f'{lst} : {x} occurs {occurrence} times\n')
