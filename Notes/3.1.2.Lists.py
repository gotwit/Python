Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'hello' * 3
'hellohellohello'
prefix = 'pyth'
prefix * 3
'pythpythpyth'
prefix 'on'
SyntaxError: invalid syntax
('hello' * 3)
'hellohellohello'
('hello' * 3) 'good'
SyntaxError: invalid syntax
prefix + 'on'
'python'
('hello' * 3) + 'sri'
'hellohellohellosri'
word = 'python'
word[0]
'p'
word[5]
'n'
word[6]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    word[6]
IndexError: string index out of range
word[-1]
'n'
word[-6]
'p'
word[-7]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    word[-7]
IndexError: string index out of range
arr = [10, 20, 30, 40, 50]
len(arr)
5
arr = [10, 20, 30, 40, 50, 60]
len(arr)
6
arr[0
    ]
10
arr[5]
60
arr[6]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    arr[6]
IndexError: list index out of range
arr[-1]
60
arr[-7]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    arr[-7]
IndexError: list index out of range
word
'python'
len(word)
6
# slicing
word[0:2]
'py'
# word[start : end : increment]
word[0:2:1]
'py'
word[0:2:2]
'p'
word[2:5]
'tho'
word[2:6]
'thon'
word[2:7]
'thon'
word[2:8]
'thon'
word[2:7:6]
't'
word[-1:-6]
''
word[-6:-1]
'pytho'
word[-6:]
'python'
word[-1:-6:-1]
'nohty'
word[0:-6:-1]
''
word[-1:-7:-1]
'nohtyp'
'nohtyp'
'nohtyp'






























word[-1:-7]
''
word[-1:-7:-1]
'nohtyp'
word[0:-7:-1]
'p'
word[:2]
'py'
word[4:]
'on'
word[-2:]
'on'
word[-4:]
'thon'
word[-6:]
'python'
word[:]
'python'
word
'python'
word[::]
'python'
word[:2] + word[2:]
'python'
word[:2]
'py'
word[2:]
'thon'
word[0:9]
'python'
word[4:12]
'on'
word[45:]
''
word[43]
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    word[43]
IndexError: string index out of range
word[50:]
''
word
'python'
word[3]
'h'
word[3]='i'
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    word[3]='i'
TypeError: 'str' object does not support item assignment
word[3]="j"
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    word[3]="j"
TypeError: 'str' object does not support item assignment
word[0:2]='pqr'
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    word[0:2]='pqr'
TypeError: 'str' object does not support item assignment
s = 'supercalifragilisticexpialidocious'
len(s)
34
lst = [1, 2, 3, 4, 5, 6]
type(lst)
<class 'list'>
lst2 = [10, "hi", 3.5, True, 'i']
>>> lst2
[10, 'hi', 3.5, True, 'i']
>>> type(lst2)
<class 'list'>
>>> lst2[3]
True
>>> lst2[2:4]
[3.5, True]
>>> squares[i**2 for i in range(1:4)]
SyntaxError: invalid syntax
>>> squares=[i**2 for i in range(1:4)]
SyntaxError: invalid syntax
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> squares
[1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares = squares + [36, 49, 64, 81, 100]
>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> # strings are immutable means you can't change / modify / update value using
>>> # indexing or slicing
>>> # list are mutable means you can modify items / elements / values
>>> i**2 for i in range(5)
SyntaxError: invalid syntax
>>> [i**2 for i in range(5)]
[0, 1, 4, 9, 16]
>>> cubes = [i**3 for i in range(1, 11)]
>>> cubes
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
>>> squares = [i**2 for i in range(1, 10)]
>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> squares = [i**2 for i in range(1, 11)]
>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
