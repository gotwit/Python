def delDictByKey(dict, key):
    try:
        del dict[key]
    except KeyError:
        print("Key not found")
    except Exception as error:
        print(type(error))
        print(error)
        print("Exception occurred")
    else:
        print("Success")
    finally:
        print("Executing finally block")
    return dict


def delDictByPop(dict, key):
    dict.pop(key, "No key found")
    return dict


def delDictByComprehension(dict, searchKey):
    newDict = {key: value for key, value in dict.items() if key != searchKey}
    return newDict


if __name__ == '__main__':
    pass
"""     dict = {"A": 1, "B": 2, "C": 3, "D": 4}
    key = input(
        f"Enter any key from this dictionary {dict} to be deleted by key ")
    print(f"After deletion: {delDictByKey(dict, key)}")

    dict = {"A": 1, "B": 2, "C": 3, "D": 4}
    key = input(
        f"Enter any key from this dictionary {dict} to be deleted by pop ")
    print(f"After deletion: {delDictByPop(dict, key)}")

    dict = {"A": 1, "B": 2, "C": 3, "D": 4}
    key = input(
        f"Enter any key from this dictionary {dict} to be deleted by comprehension ")
    print(f"After deletion: {delDictByComprehension(dict, key)}") """


def createDict():
    dict = {1: "Sri", 2: "Ganehaya", 3: "Namaha"}
    print(dict)


# createDict()

def createMixedKeysDict():
    dict = {'Name': 'Sri', 1: ['a', 'b', 'c']}
    # Duplicate key in dictionary, but it overrides the latest value to same key
    # dict = {'Name': 'Sri', 1: ['a', 'b', 'c'], 1: 10}
    print(dict)


# createMixedKeysDict()


def createDictonaryUsingDict():
    dictionary = dict({'!': 'a', 'b': 'c', '2': '~'})
    print(dictionary)


# createDictonaryUsingDict()


def createEmptyDict():
    dictionary = {}
    print(f"Empty dictionary {dictionary}")


# createEmptyDict()

def createDictPair():
    dictionary = dict([(1, 'Om'), (2, 'Namah'), (3, 'Shivaya')])
    print(dictionary)

# createDictPair()


def createDictNameValuePair():
    dictionary = dict(One=1, Two=2, Three=3)
    print(dictionary)


# createDictNameValuePair()

def createNestedDict():
    dictionary = {'One': 1, 'Two': 2, 'Three': {
        1: "Om", 2: "Namah", 3: "Shivaya"}}
    print(dictionary)


# createNestedDict()

def addElementsToDict():
    dictionary = {}
    print(f"Empty dictionary {dictionary}")
    dictionary[0] = 'Om'
    dictionary[2] = 'Namah'
    dictionary[3] = 'Shivaya'
    print(dictionary)
    dictionary['value_set'] = 1, 2, 3, 4, 5
    print(dictionary)
    dictionary[3] = 'Narayanaya'
    dictionary[2] = 'Namo'
    print(f"Update value {dictionary}")


# addElementsToDict()

def accessDict():
    dictionary = {1: "Namasthe", 2: "Sri"}
    print(dictionary[1])
    print(dictionary.get(2))
    print(dictionary.get(3))
    # get return None for non existing keys, direct access of non existing key throw keyerror
    # print(dictionary[4])
    dictionary[3] = {"One": 'Om', 2: 'Namah', "Three": "Shivaya"}
    print(dictionary[3]["Three"])


# accessDict()


def removeDict():
    dictionary = {5: 'Welcome', 6: 'To', 7: 'Python',
                  'A': {1: 'Sample', 2: 'Dictionary'},
                  'B': {1: 'To', 2: 'Remove item'}
                  }
    print(dictionary)
    del dictionary['B'][2]
    print(dictionary)
    popElement = dictionary.pop('A')
    print(str(popElement))
    # print(str(dictionary))
    popElement = dictionary.popitem()
    print(str(popElement))
    # print(str(dictionary))
    popElement = dictionary.popitem()
    print(str(popElement))
    print(str(dictionary))
    popElement = dictionary.popitem()
    print(str(popElement))
    popElement = dictionary.popitem()
    print(str(popElement))
    popElement = dictionary.popitem()
    print(str(popElement))
    print(dictionary)


# removeDict()


def shallowCopy():
    dictionary = {1: 'Namasthe', 2: 'Sri'}
    newDict = dictionary.copy()
    newDict.clear()
    print('Original ', dictionary)
    print('New ', newDict)


# shallowCopy()

def deepCopy():
    dictionary = {1: 'Namasthe', 2: 'Sri'}
    newDict = dictionary
    newDict.clear()
    print('Original ', dictionary)
    print('New ', newDict)


# deepCopy()

def updateDict():
    dictionary = {'A': 'First', 'B': 'Second'}
    dictionary2 = {'B': 'Updated Value'}
    print('Original ', dictionary)
    dictionary.update(dictionary2)
    print('Updated ', dictionary)

    # Duplicate key in dictionary but updates the key value same as update
    dictionary = {'A': 'One', 'B': 'Two', 'C': 'Three', 'C': 3}
    print(dictionary)

    dictionary = {'A': 1}
    dictionary.update(B=2, C=3)
    print(dictionary)


# updateDict()

# setdefault returns value of key
def setDefaultDict():
    dictionary = {'A': 'One', 'B': 'Two'}
    val = dictionary.setdefault('B')

    print(dictionary)
    print(val)

    val = dictionary.setdefault('C')
    print(val)
    print(dictionary)
    val = dictionary.setdefault('D', 'Four')
    print(val)
    print(dictionary)


# setDefaultDict()

def dictKeys():
    dictionary = {1: 'One', 2: 'Two'}
    dictionary.update(six=6)
    print(dictionary.keys())
    emptyDict = {}
    print(emptyDict.keys())
    # dictionary.update(3='Three')
    dictionary.update({4: 'Four'})
    print(dictionary.keys())
    dictionary.update(B=2, C=3)
    print(dictionary.keys())


# dictKeys()

