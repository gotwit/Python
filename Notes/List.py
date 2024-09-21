Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
float("-inf")
-inf
print(-inf)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(-inf)
NameError: name 'inf' is not defined. Did you mean: 'int'?
print("-inf")
-inf
while True:
    pass
KeyboardInterrupt
lst = []
len(lst)
0
print(lst)
[]
print(len(lst))
0
lst.append(10)
>>> lst
[10]
>>> size = len(lst)
>>> size
1
>>> lst.append(20)
>>> lst
[10, 20]
>>> iterable = [30, 40, 50]
>>> iterable
[30, 40, 50]
>>> lst.extend(iterable)
>>> lst
[10, 20, 30, 40, 50]
>>> iterable2 = 60
>>> lst.extend(iterable2)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    lst.extend(iterable2)
TypeError: 'int' object is not iterable
>>> iterable3 = [70]
>>> iterable3
[70]
>>> lst.extend(iterable3)
>>> lst
[10, 20, 30, 40, 50, 70]
>>> iterable4 = [80, 90]
>>> iterable4
[80, 90]
>>> lst.append(iterable4)
>>> lst
[10, 20, 30, 40, 50, 70, [80, 90]]
>>> lst.pop()
[80, 90]
>>> lst
[10, 20, 30, 40, 50, 70]
>>> len(lst)
6
>>> lst.insert(5, 60)
>>> lst
[10, 20, 30, 40, 50, 60, 70]
lst.append(60)
lst
[10, 20, 30, 40, 50, 60, 70, 60]
lst.remove(60)
lst
[10, 20, 30, 40, 50, 70, 60]
lst.remove(60)
lst
[10, 20, 30, 40, 50, 70]
lst.remove(60)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    lst.remove(60)
ValueError: list.remove(x): x not in list
lst.pop()
70
lst
[10, 20, 30, 40, 50]
len(lst)
5
lst.insert(len(lst), 60)
lst
[10, 20, 30, 40, 50, 60]
len(lst)
6
lst.insert(8, 70)
lst
[10, 20, 30, 40, 50, 60, 70]
lst.insert(-1, 80)
lst
[10, 20, 30, 40, 50, 60, 80, 70]
lst.clear()
lst
[]
lst.insert(-1, 10)
lst
[10]
lst.insert(-3, 20)
lst
[20, 10]
lst.count()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    lst.count()
TypeError: list.count() takes exactly one argument (0 given)
lst.count(10)
1
[10, 20, 30, 40, 50, 60, 70, 60].count(60)
2
