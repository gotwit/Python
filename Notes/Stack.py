Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lst = []
len(lst)
0
lst.append('a')
lst
['a']
lst
['a']
lst[len(lst)] = 'b'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    lst[len(lst)] = 'b'
IndexError: list assignment index out of range
lst[len(lst):] = 'b'
lst
['a', 'b']
lst[len(lst):] = 'c'
lst
['a', 'b', 'c']
iterable = [1, 2, 3]
lst.extend(iterable)
lst
['a', 'b', 'c', 1, 2, 3]
iterable2 = ['d', 'e', 'f']
lst[len(lst):] = iterable2
lst
['a', 'b', 'c', 1, 2, 3, 'd', 'e', 'f']
lst[len(lst):] = [4, 5, 6]
lst
['a', 'b', 'c', 1, 2, 3, 'd', 'e', 'f', 4, 5, 6]
lst.insert(3, 7)
lst
['a', 'b', 'c', 7, 1, 2, 3, 'd', 'e', 'f', 4, 5, 6]
lst.insert(6, ['C', "D", 'E'])
lst
['a', 'b', 'c', 7, 1, 2, ['C', 'D', 'E'], 3, 'd', 'e', 'f', 4, 5, 6]
lst.insert(len(lst), 8)
lst
['a', 'b', 'c', 7, 1, 2, ['C', 'D', 'E'], 3, 'd', 'e', 'f', 4, 5, 6, 8]
list.remove(['C', 'D', 'E'])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list.remove(['C', 'D', 'E'])
TypeError: list.remove() takes exactly one argument (0 given)
lst.remove(['C','D','E'])
lst
['a', 'b', 'c', 7, 1, 2, 3, 'd', 'e', 'f', 4, 5, 6, 8]
lst.remove(7)
lst.remove(1)
lst.remove(2)
lst.remove(3)
lst
['a', 'b', 'c', 'd', 'e', 'f', 4, 5, 6, 8]
lst.remove(4)
lst.remove(5)
lst.remove(6)
lst.remove(8)
lst
['a', 'b', 'c', 'd', 'e', 'f']
len(lst)
6
lst.remove(9)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    lst.remove(9)
ValueError: list.remove(x): x not in list
lst.pop()
'f'
lst
['a', 'b', 'c', 'd', 'e']
lst.pop(3)
'd'
lst
['a', 'b', 'c', 'e']
lst.pop()
'e'
lst.pop()
'c'
lst.pop()
'b'
lst.pop()
'a'
lst.pop()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    lst.pop()
IndexError: pop from empty list
lst.clear()
lst
[]
lst[len(lst)] = 1
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    lst[len(lst)] = 1
IndexError: list assignment index out of range
lst[len(lst):] = 1
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    lst[len(lst):] = 1
TypeError: can only assign an iterable
lst[len(lst)] = 'a'
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    lst[len(lst)] = 'a'
IndexError: list assignment index out of range
len(lst)
0
lst[len(lst):] = 'a'
lst
['a']
len(lst)
1
lst
['a']
lst.clear()
lst
[]
lst[len(lst):] = 'a'
lst
['a']
del lst[:]
lst
[]
lst = ['a', 'b', 'c', 7, 1, 2, ['C', 'D', 'E'], 3, 'd', 'e', 'f', 4, 5, 6, 8]
lst
['a', 'b', 'c', 7, 1, 2, ['C', 'D', 'E'], 3, 'd', 'e', 'f', 4, 5, 6, 8]
len(lst)
15
lst.index('C')
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    lst.index('C')
ValueError: 'C' is not in list
lst.index(2)
5
lst.index(2, 5, len(lst))
5
lst.index(2, 6, 15)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    lst.index(2, 6, 15)
ValueError: 2 is not in list
lst.count(2)
1
lst.sort(*, key=None, reverse=False)
SyntaxError: invalid syntax
lst.sort()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    lst.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
lst.reverse()
lst
[8, 6, 5, 4, 'f', 'e', 'd', 3, ['C', 'D', 'E'], 2, 1, 7, 'c', 'b', 'a']
lst.reverse()
lst
['a', 'b', 'c', 7, 1, 2, ['C', 'D', 'E'], 3, 'd', 'e', 'f', 4, 5, 6, 8]
lst.pop(-1)
8
>>> lst
['a', 'b', 'c', 7, 1, 2, ['C', 'D', 'E'], 3, 'd', 'e', 'f', 4, 5, 6]
>>> lst.pop(6)
['C', 'D', 'E']
>>> lst
['a', 'b', 'c', 7, 1, 2, 3, 'd', 'e', 'f', 4, 5, 6]
>>> lst.sort(*, key=None, reverse=False)
SyntaxError: invalid syntax
>>> lst.sort()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    lst.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> lst = ['d', 'e', 'f', 'a', 'b', 'c']
>>> lst
['d', 'e', 'f', 'a', 'b', 'c']
>>> lst.sort()
>>> lst
['a', 'b', 'c', 'd', 'e', 'f']
>>> lst.reverse()
>>> lst
['f', 'e', 'd', 'c', 'b', 'a']
>>> lst.sort()
>>> lst
['a', 'b', 'c', 'd', 'e', 'f']
>>> lst
['a', 'b', 'c', 'd', 'e', 'f']
>>> lst.reverse()
>>> lst
['f', 'e', 'd', 'c', 'b', 'a']
>>> lst.sort(*, key=None, reverse=False)
SyntaxError: invalid syntax
>>> lst
['f', 'e', 'd', 'c', 'b', 'a']
>>> lst.sort()
>>> lst
['a', 'b', 'c', 'd', 'e', 'f']
>>> lst2 = lst.copy()
>>> lst2
['a', 'b', 'c', 'd', 'e', 'f']
