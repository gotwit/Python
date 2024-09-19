Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1 + 1
2
# This is the beginning
# the comments are ommitted by python interpreter
spam = 1 # this is second comment
         # this is third comment
         
# Numbers
2 + 2
4
50 - 5 * 6
20
(50 - 5*6)/4
5.0
8 / 5
1.6
5 // 2
2
5 / 2
2.5
# expressions or statements are executed Left to Right L -> R, Top to Bottom T -> B
(50 - 5*6)//4
5
(50-30)/4
5.0
50 - 5*6/4
42.5
6/4
1.5
5 * 1.5
7.5
50-7.5
42.5
5*6/4
7.5
# * < / < %
# % > / > *
# + < -
# - > +
2 + 5 - 4
3
3 + 7 - 2
8
# / returns float
# // return int
# // return int floor division removes fractional value















17/3
5.666666666666667
17//3
5
17 / 3  # classic division returns a float


17 // 3  # floor division discards the fractional part

17 % 3  # the % operator returns the remainder of the division

5 * 3 + 2  # floored quotient * divisor + remainder

SyntaxError: multiple statements found while compiling a single statement

17 % 3
2
5 * 3 + 2
17
2 + 5 * 3
17
1 * 34 / 2 % 3
2.0
1 * 34 // 2 % 3
2
2 +3 - 2
3
5 - 3 + 3
5
34 / 2
17.0
17.0 % 3
2.0
1 * 34 / 2
17.0
2 * 34 / 2
34.0
3 % 2 // 34 * 1
0
3 % 2 // 34
0
3 % 2
1
1 // 34
0
1 / 34
0.029411764705882353
2 // 34
0
2 / 34
0.058823529411764705
3 % 0
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    3 % 0
ZeroDivisionError: integer modulo by zero
2 * 2 * 2
8
2 ** 3
8
2^3
1
2 ** 4
16
2 *** 3
SyntaxError: invalid syntax
2 ** 2
4
2 ** 3
8
2 ** 4
16
print(2**2)
4
width = 20
width
20
height = 5 * 9
print(height)
45
height
45
width * height
900
x
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    x
NameError: name 'x' is not defined
4 * 3.75 - 1
14.0
# opnd1 * opnd2 - opnd3
# opnd1 op1 opnd2 op2 opnd3
# opnd - operand, op - operator
_
14.0
x = 5
y = 5
z = x + y
z
10
>>> _
10
>>> z = x + y / 2
>>> _
10
>>> z
7.5
>>> _
7.5
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
>>> _
113.06
>>> round(_, 3)
113.06
>>> 113.0625
113.0625
>>> _
113.0625
>>> round(_, 3)
113.062
>>> 113.0625
113.0625
>>> _
113.0625
>>> round(_, 4)
113.0625
>>> _
113.0625
>>> round(_)
113
>>> _ = 114
>>> _
114
