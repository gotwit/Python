Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'Hello' + 'World'
'HelloWorld'
print('Hello' + 'world')
Helloworld
print("Hello" + "world")
Helloworld
print("Hello" + "world" + "welcome")
Helloworldwelcome
"welcome" + "Hello" + "world" * 3
'welcomeHelloworldworldworld'
("welcome" + "Hello" + "world") * 3
'welcomeHelloworldwelcomeHelloworldwelcomeHelloworld'
("welcome" + "Hello" + "world" + "\n") * 3
'welcomeHelloworld\nwelcomeHelloworld\nwelcomeHelloworld\n'
print(("welcome" + "Hello" + "world" + "\n") * 3)
welcomeHelloworld
welcomeHelloworld
welcomeHelloworld

print('welcomeHelloworld\nwelcomeHelloworld\nwelcomeHelloworld\n')
welcomeHelloworld
welcomeHelloworld
welcomeHelloworld

'Hello' 'World!'
'HelloWorld!'
"Welcome" "Hello" "World"
'WelcomeHelloWorld'
hello world
SyntaxError: invalid syntax
hello, world
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    hello, world
NameError: name 'hello' is not defined. Did you mean: 'help'?
"Hello""world"
'Helloworld'
text = ('This is my first')
text = ('This is my first'
        'python tutorial')
text
'This is my firstpython tutorial'
text = ('This is my first'
        'python tutorial')
text
'This is my firstpython tutorial'
print(text)
This is my firstpython tutorial
text = ('This is my first'\
        'python tutorial')
text
'This is my firstpython tutorial'
print(text)
This is my firstpython tutorial
text = ('This is my first'
        ' python tutorial')
text
'This is my first python tutorial'
print(text)
This is my first python tutorial

word = 'python'
word[0]
'p'
word[5]
'n'
word[0:5]
'pytho'
word[0:2]
'py'
word[2:5]
'tho'
word[0:0]
''
word[0:1]
'p'
word[5:1]
''
word[4:1]
''
word[4:]
'on'
word[5:]
'n'
word[2:]
'thon'
word[4:5]
'o'
word[5:6]
'n'
word[5:7]
'n'
word[6:]
''
word[6:7]
''
word = "python"
word[:2]
'py'
word[:1]
'p'
word[:0]
''
word[:6]
'python'
word[:7]
'python'
word[:]
'python'
word
'python'
print(word)
python
print(r"python")
python
print(rword)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(rword)
NameError: name 'rword' is not defined. Did you mean: 'word'?
word[:2] + word[2:]
'python'
word[:2] word[2:]
SyntaxError: invalid syntax
print(word[:2], word[2:])
py thon
print(word[:2],word[2:])
py thon

"""
word[start:end:step]
step +ve Left to Right
step -ve Right to Left
"""

print(word[:2], word[2:])
py thon
print(word[:2],word[2:])
SyntaxError: multiple statements found while compiling a single statement
word = "python"
print(word[:2],word[2:])
py thon
word[:2],word[2:]
('py', 'thon')
word[:2]word[2:]
SyntaxError: invalid syntax
word[:2] word[2:]
SyntaxError: invalid syntax
word[:2]+word[2:]
'python'
print(word[:2]+word[2:])
python
word[0:2:-1]
''
word[0:6:-1]
''
word[6:0:-1]
'nohty'
word[6::-1]
'nohtyp'
word[6:-1:-1]
''
word[7:0:-1]
'nohty'
word[6:
word='python'
word[6::-1]
'nohtyp'
word[5:0]
''
word[::-1]
'nohtyp'
word[6:-1:-1]
''
word[6:1:-1]
'noht'
word[6:0:-1]
'nohty'
word[-1:-6:-1]
'nohty'
word[-1:-6:1]
''
word[0:-6:-1]
''
word[-5::-1]
'yp'
word[-6::-1]
'p'
word[-6:-1:-1]
''
word[-6:-1:1]
'pytho'
word[-6:0:1]
''
word[-6:0:-1]
''
word = 'python'
word[6::-1]
'nohtyp'
word[-6::1]
'python'
word[6:-1:1]
''
word[6:0:-1]
'nohty'
word[6:1:-1]
'noht'
word[7:1:-1]
'noht'
word[6:-1:-1]
''
word[-1:-6:-1]
'nohty'
word[-1:-7:-1]
'nohtyp'

word = 'python'
word[3]= 'i'
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    word[3]= 'i'
TypeError: 'str' object does not support item assignment
word[3:]='ee'
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    word[3:]='ee'
TypeError: 'str' object does not support item assignment
word[1] + 'i
SyntaxError: unterminated string literal (detected at line 1)
word[1]+'a'
'ya'
word[3:]+ 'bla'
'honbla'
s = 'abcdefghij'
len(s)
10
string='abc'
len(string)
3
type(string)
<class 'str'>
x = 10
type(x)
<class 'int'>


x = 10
word =
SyntaxError: invalid syntax
word = 'python'

word + ' is ' + x + ' times faster'
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    word + ' is ' + x + ' times faster'
TypeError: can only concatenate str (not "int") to str
word + ' is ' + str(x) + ' times faster'
'python is 10 times faster'
print(f'{word} is {x} times faster')
python is 10 times faster
print('word is x times faster')
word is x times faster
word ' is ' str(x) ' times faster'
SyntaxError: invalid syntax
'python' ' is ' str(x) ' times faster'
SyntaxError: invalid syntax
'python' ' is ' '10' ' times faster'
'python is 10 times faster'

print('%(language)s has %(number)03d times faster' % {'python', 5})
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print('%(language)s has %(number)03d times faster' % {'python', 5})
TypeError: format requires a mapping
print('%(language)s has %(number)03d times faster' % {'language': 'python', 5, 'number': 5})
SyntaxError: ':' expected after dictionary key
print('%(language)s has %(number)03d times faster' % {'language': 'python','number': 5})
python has 005 times faster
print('%(language)s has %(number)d times faster' % {'language': 'python','number': 5})
python has 5 times faster
print('%(language)s is %(number)d times faster' % {'language': 'python','number': 5})


print('%(language)s is %(number)d times faster' % {'abc': 'python','number': 5})
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print('%(language)s is %(number)d times faster' % {'abc': 'python','number': 5})
KeyError: 'language'
print('%(language)s is %(number)d times faster' % {'language': 'python','number': 5})
python is 5 times faster
print('%(language)s is %(number)000d times faster' % {'language': 'python','number': 5})
python is 5 times faster
print('%(language)s is %(number)03d times faster' % {'language': 'python','number': 5})
python is 005 times faster
print('%(language)s is %(number)3d times faster' % {'language': 'python','number': 5})
python is   5 times faster
print('%(language)s is %(number)04d times faster' % {'language': 'python','number': 5})
python is 0005 times faster

2 ** 2
4
squares = [1, 4, 9, 16, 25]
squares
[1, 4, 9, 16, 25]
squares[3]
16
squares[-1]
25
squares[-1:]
[25]
squares[-6:]
[1, 4, 9, 16, 25]
squares[-6::1]
[1, 4, 9, 16, 25]
squares[-3:]
[9, 16, 25]
squares[:]
[1, 4, 9, 16, 25]
squares = [1, 4, 9, 16, 25]
squares[5] = 36
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    squares[5] = 36
IndexError: list assignment index out of range
squares[4] = 36
squares
[1, 4, 9, 16, 36]

squares = [1, 4, 9, 16, 25]
squares[2]= 26
squares
[1, 4, 26, 16, 25]
squares[2]=36
squares
[1, 4, 36, 16, 25]
squares[:]
[1, 4, 36, 16, 25]
squares=[1, 4, 9, 16, 25]
squares
[1, 4, 9, 16, 25]
sqcopy = squares
squares
[1, 4, 9, 16, 25]
squares[2]=36
squares
[1, 4, 36, 16, 25]
sqcopy
[1, 4, 36, 16, 25]
sqcopy[2] = 49
squares
[1, 4, 49, 16, 25]
sqcopy
[1, 4, 49, 16, 25]

List operations
append
clear
copy
count
extend
index
insert
pop
remove
reverse
sort

Fibonacci series
0 1 1 2 3 5 8 13

a = 0
b = 1

c = a + b
0 1 1

a = 1
b = 1
c = a + b

print a, b
print a=b, b = c

a = 0, b = 1
-> a => 0
a = 1, b = 1
-> a => 1
a = 1, b = 2
-> a => 1
a = 2, b = 3
-> a => 2




while a < 10:

while False:
--
--
--

while "":

while []:

len("abc") => 3

isValid = True
while isValid:


if() {

}

3 * 3

a, b = 0, 1
a, b, c = 0, 1, 2
a = b, b = c


a, b = 0, 1
while a < 10:
    c = a + b
    print(a)
    print(b)
    a = b
    b = c

Expected: 0 1 1 2 3
Output:   0 1 2 4 8

a, b = 0, 1
a = 0, b = 1

Iteration 1: 0 < 10
a = 0, b = 1
0
a = 1
b = 1 + 1 = 2

Iteration 2: 1 < 10
a = 1, b = 2
1
a = 2
b = 2 + 2 = 4

Iteration 3: 2 < 10
a = 2, b = 4
2
a = 4
b = 4 + 4 = 8

Iteration 4: 4 < 10
a = 4, b = 8
4
a = 8
b = 8 + 8 = 16

Iteration 5: 8 < 10
a = 8, b = 16
8
a = 16
b = 16 + 16 = 32

Iteration 6: 16 < 10 => False


Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
3 * 3

9
3**3
27
3**2
9
-3**2
-9
(-3)**2
9
a, b = 0, 1
while a < 10:
    c = a + b
    print(a)
    print(b)
    a = b, b = c

    
0
1
Traceback (most recent call last):
  File "<pyshell#12>", line 5, in <module>
    a = b, b = c
TypeError: cannot unpack non-iterable int object
a, b = 0, 1
while a < 10:
    c = a + b
    print(a)
    print(b)
    a = b b = c
    
SyntaxError: multiple statements found while compiling a single statement
a, b = 0, 1
while a < 10:
    c = a + b
    print(a)
    print(b)
    a = b
    
SyntaxError: multiple statements found while compiling a single statement
a, b = 0, 1
while a < 10:
    c = a + b
    print(a)
    print(b)
    a = b
    
SyntaxError: multiple statements found while compiling a single statement



Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a, b = 0, 1
while a < 10:
    c = a + b
    print(a)
    print(b)
    a = b
    b = c
    
SyntaxError: multiple statements found while compiling a single statement
a, b = 0, 1
while a < 10:
    c = a + b
    print(a)
    print(b)
    a = b
    b = c

    
0
1
1
1
1
2
2
3
3
5
5
8
8
13
a, b = 0, 1
while a < 10:
    c = a + b
    print(a)
    a = b
    b = c
    
SyntaxError: multiple statements found while compiling a single statement
a, b = 0, 1
whiel a < 10:
    
SyntaxError: invalid syntax
a, b = 0, 1
while a < 10:
    c = a + b
    print(a)
    a = b
    b = c

    
0
1
1
2
3
5
8
a, b = 0, 1
while a < 20:
    c = a + b
    print(a, end = ' ')
    a = b
    b = c

    
0 1 1 2 3 5 8 13 
a, b = 0, 1
while a < 20:
    print(a, end='\n')
    a = b
    b = a + b

    
0
1
2
4
8
16




Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a, b = 0, 1
while a < 20:
    print(a, end = '\n')
    a = b
    b = a + b

    
0
1
2
4
8
16
a, b = 0, 1
while a < 20:
    print(a, end = '\n')
    a, b = b, a+b

    
0
1
1
2
3
5
8
13
a, b = 0, 1
while a < 10:
    print(a, end = ' ')
    a = b
    b = a+b

    
0 1 2 4 8 


