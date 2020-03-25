def sumDict(dict):
    sum = 0
    """ for i in dict:
        print(i) """
    for i in dict:
        sum += dict[i]
    return sum


def sumDict2(dict):
    sum = 0
    for i in dict.values():
        sum += i
    return sum


def sumDict3(dict):
    sum = 0
    for i in dict:
        sum += i
    return sum


dict = {'a': 100, 'b': 200, 'c': 300}
print(f"Sum of dictionary {dict} is {sumDict(dict)}")
