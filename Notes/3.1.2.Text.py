Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'spam eggs'
'spam eggs'
"Paris rabbit got your back :)! Yay!"
'Paris rabbit got your back :)! Yay!'
'1857'
'1857'
print('1857')
1857
print("Paris rabbit")
Paris rabbit
print('spam')
spam
'doesn\'t'
"doesn't"
"doesn't"
"doesn't"
'"Yes", they said."
SyntaxError: unterminated string literal (detected at line 1)
'"Yes", they said.'
'"Yes", they said.'
"\"Yes\", they said."
'"Yes", they said.'
'"Isn\'t, they said.'
'"Isn\'t, they said.'
s = 'First line.\nSecond line.'
s
'First line.\nSecond line.'
print(s)
First line.
Second line.
print('C:\workspace\python')
C:\workspace\python
print('C:\backup\node')
C:ackup
ode
print(r'C:\backup\node')
C:\backup\node
print("""\
Usage: thing
    -h              Display the usage message
    -H hostname     Hostname to connect to
""")
Usage: thing
    -h              Display the usage message
    -H hostname     Hostname to connect to

print('''\
Usage: thing
    -h              Display the usage message
    -H hostname     Hostname to connect to
''')
Usage: thing
    -h              Display the usage message
    -H hostname     Hostname to connect to

print('''
Usage: thing
    -h              Display the usage message
    -H hostname     Hostname to connect to
''')

Usage: thing
    -h              Display the usage message
    -H hostname     Hostname to connect to

print('''
some random string
''')

some random string

print('''\
I'm learning python
''')
I'm learning python

3 * 'a'
'aaa'
'b' * 5
'bbbbb'
"Rama\n" * 10
'Rama\nRama\nRama\nRama\nRama\nRama\nRama\nRama\nRama\nRama\n'
print("Jai Sri Ram" * 10)
Jai Sri RamJai Sri RamJai Sri RamJai Sri RamJai Sri RamJai Sri RamJai Sri RamJai Sri RamJai Sri RamJai Sri Ram
print("Jai Sri Ram\n" * 10)
Jai Sri Ram
Jai Sri Ram
Jai Sri Ram
Jai Sri Ram
Jai Sri Ram
Jai Sri Ram
Jai Sri Ram
Jai Sri Ram
Jai Sri Ram
Jai Sri Ram

'How' + "are" + 'u'
'Howareu'
'How ' + "are " + 'u'
'How are u'
'py' 'thon'
'python'
print('hello' 'world')
helloworld
text = ('Put several strings within parnetheses ')
text = ('Put several strings within parnetheses '
        'to have them joined together.')
text
'Put several strings within parnetheses to have them joined together.'
prefix = 'py'
prefix 'thon'
SyntaxError: invalid syntax
print(prefix 'thon')
SyntaxError: invalid syntax
prefix + 'thon'
'python'
word = 'python'
word
'python'
len(word)
6
>>> start_index = word.index(0)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    start_index = word.index(0)
TypeError: must be str, not int
>>> start_index = word.index[0]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    start_index = word.index[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> word.index('p')
0
>>> word.index('n')
5
>>> start_index = word.index('p')
>>> end_index = word.index('n')
>>> start_index
0
>>> end_index
5
>>> word2 = 'pythonpython'
>>> word2.index('p')
0
>>> word2.index('n')
5
>>> word2.index('p', -1)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    word2.index('p', -1)
ValueError: substring not found
>>> word2.index('p', 6, len(word2))
6
>>> word2.index('n', 6, len(word2))
11
>>> len(word2)
12
>>> word2.index('p', word2.index('n')+1)
6
>>> word2.index('n', word2.index('n')+1)
11
