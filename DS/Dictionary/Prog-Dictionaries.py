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
    value = dict.pop(key, "No key found")
    return dict


def delDictByComprehension(dict, searchKey):
    newDict = {key: value for key, value in dict.items() if key != searchKey}
    return newDict


""" 

dict = {"A": 1, "B": 2, "C": 3, "D": 4}
key = input(f"Enter any key from this dictionary {dict} to be deleted by key ")
print(f"After deletion: {delDictByKey(dict, key)}")


dict = {"A": 1, "B": 2, "C": 3, "D": 4}
key = input(f"Enter any key from this dictionary {dict} to be deleted by pop ")
print(f"After deletion: {delDictByPop(dict, key)}") """


dict = {"A": 1, "B": 2, "C": 3, "D": 4}
key = input(
    f"Enter any key from this dictionary {dict} to be deleted by comprehension ")
print(f"After deletion: {delDictByComprehension(dict, key)}")
