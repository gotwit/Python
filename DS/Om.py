from urllib.parse import urlencode
from base64 import b64encode
import gzip
from math import pi
from collections import deque
print("Om")


def showList(arr):
    for i in arr:
        print(i, end=' ')
    print()


def showListTuple(arr):  # def showTuple(**arr):
    for key, value in arr:
        print('key: %s value: %s' % (key, value))
        # print('Value:%s' % v)
    print('\n')


def showTuple(arr):  # def showTuple(**arr):
    for k, v in arr.copy().items():
        print('Key:%s' % k)
        print('Value:%s' % v)
    print()


""" print("list")
a = []
a[len(a):] = [1]
a[len(a):] = [2]
a.append(3)
newList = [4, 5]
a.extend(newList)
a.insert(len(a), 6)
a.append(3)
a.remove(3)
a.pop()
a.append(4)
a.append(3)
a.append(7)
a.append(3)
a.append(8)
a.append(0)

showList(a)

print('\n')

# print(len(a))
a.pop(len(a) - 1)

print(a.index(2, 0, 3))

print(a.count(2))

showList(a)

print()

x = 3
print("%s occur \
%s times" % (x, a.count(x)))
# print("count {}".format(a.count()))

a.sort()

showList(a)

a.reverse()

showList(a) """

""" print("stack")

stack = [1, 2, 3]
stack.append(4)
stack[len(stack):] = [5]

showList(stack)

stack.pop()

showList(stack)

print(stack) """

""" print("queue")

queue = deque(["Orange", "Apple", "Mango", "Pineapple", "Pears"])
print(queue)
showList(queue)
queue.append("Bananna")
queue.extend(["Pomegrenate"])
showList(queue)
queue.pop()
showList(queue)
queue.popleft()
showList(queue) """

""" print("List compreshension")

squares = []
# for x in range(0, 10):
for x in range(11):
    squares.append(x ** 2)

showList(squares)

squares2 = list(map(lambda x: x**2, range(10)))
showList(squares2)

squares3 = [x ** 2 for x in range(10)]
showList(squares3)

# showTuple(**{'jack': 4098, 'guido': 4127, 'irv': 4127})
showTuple({'jack': 4098, 'guido': 4127, 'irv': 4127})

tupl = [(x, y) for x in [1, 2, 4] for y in [3, 1, 4] if x != y]
print(tupl)
showListTuple(tupl)

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])

print([abs(x) for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([fruit.strip() for fruit in freshfruit])

print([(x, x ** 2) for x in range(10)])

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

print([round(pi, i) for i in range(1, 6)]) """

""" print("Nested List Compreshensions")

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

for i in range(4):
    for row in matrix:
        print(row[i], end=' ')
    print()

transposed = []
for i in range(4):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
        # print(row[i], end=' ')
    transposed.append(transpose_row)
    print()
print(transposed)

print([[row[i] for row in matrix] for i in range(4)])

for row in matrix:
    for i in range(4):
        print(row[i], end=' ')
    print()

# unpack arguments from list
print(*matrix)

# zip is built-in function for transpose
print(list(zip(*matrix))) """

""" a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:2]  # no element is removed
print(a)

del a[2:3]
print(a)

del a[:]  # del a
print(a)

t = 10, 'a', 'abc'
print(t)
print(t[2])
# t[1] = 'b' immutable
u = t, (1, 2, 3)
print(u)

v = ([1, 2, 3], [4, 5, 6])
print(v)
# v[0] = [7, 8]

# Sequence unpacking
x, y, z = t
# too many value to unpack
# x, y = t
 """

""" print("Sets")

fruits = {"Orange", "Apple", "Mango", "Pineapple", "Pears"}
print(fruits)

print("Mango" in fruits)

a = set('abracadabra')
b = set('alacazam')

# unique letters in a
print(a)

# difference letters in a  but not in b
print(a - b)

# union letters in a or b or both
print(a | b)

# intersection letters in both a and b
print(a & b)

# symmetric difference letters in a or b but not both
print(a ^ b)

# list comprehension for set
x = {i for i in 'abracadabra' if i not in 'abc'}
print(x) """

""" str = "srikanth"  # "malayalam"
print(str[-1])
print(str[-2])
print(str[-3])
print(str[-4])
print(str[-5])
print(str[-6])
print(str[-7])
print(str[-8])
print(str[:-1])
print(str[:-3])
print(str[:4])
print(str[::-1])

print(tuple([1, 2, 3]))
x = 1,
print(x) """


""" 
1  5  7  3  2  4  6
0  1  2  3  4  5  6
-7 -6 -5 -4 -3 -2  -1 
"""

""" lst = [1, 5, 7, 3, 2, 4, 6]
print(lst)
print(lst[:])
print(lst[::2])  # list[start:end:step]
print(lst[::-1]) """


""" def get_kusto_link(cluster: str, database: str, query: str) -> str:
    byte_query = query.encode()
    gzipped_query = gzip.compress(byte_query)
    b64encoded_query = b64encode(gzipped_query)
    urlencoded_query = urlencode({
        'web': 0,
        'query': b64encoded_query
    })
    return f'https://{cluster}/{database}?{urlencoded_query}' """


""" 
url = get_kusto_link('cdbsupport.kusto.windows.net:443',
                     'Support', 'CosmosDBRegionalFederationsCapacity("West US")')
print('%(function) %(url)' %
      {'function': 'CosmosDBRegionalFederationsCapacity("West US")', "url": url}) """

""" print('function: %(function) surl: %(surl)' %
      {"function": "abc", "surl": "https://"}) """
#   {'function': 'CosmosDBRegionalFederationsCapacity("West US")', 'url': get_kusto_link('cdbsupport.kusto.windows.net:443', 'Support', 'CosmosDBRegionalFederationsCapacity("West US")')})


""" print(get_kusto_link('cdbsupport.kusto.windows.net:443',
                     'Support', "RegionalCapacityAllNew() | extend Status = case((Region contains 'Germany North'), 'Restricted - EA Only', (Region contains 'Germany West Central'), 'Restricted - EA Only', (Region contains 'Central India'), 'Restricted - Existing Only', (Region contains 'South India'), 'Restricted - EA Only', (Region contains 'West India'), 'Restricted - EA Only', (Region contains 'North Europe'), 'Restricted - EA Only', (Region contains 'West Europe'), 'Restricted - Existing Only', (Region contains 'Australia East'), 'Restricted - EA Only', (Region contains 'UK West'), 'Restricted - EA Only', (Region contains 'UK South'), 'Restricted - Existing Only', (Region contains 'Southeast Asia'), 'Restricted - EA Only', (Region contains 'Canada East'), 'Restricted - Existing Only', (Region contains 'Norway East'), 'Restricted - Existing Only', (Region contains 'USGov Arizona'), 'Restricted - Existing Only', '')"))
 """
