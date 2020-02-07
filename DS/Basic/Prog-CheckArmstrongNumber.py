"""
A positive integer of n digits is called an Armstrong number of order n
(order is number of digits) if
abcd... = pow(a, n) + pow(b, n) + pow(c, n) + pow(d, n)+...
"""

# Function to calculate order of the number
""" """


def order(n):
    count = 0
    while n != 0:
        count = count + 1
        n = n//10
    return count


# Solution 1 - Brute force technique
''' '''


def isArmstrong(x):
    n = order(x)
    temp = x
    _sum = 0

    while (temp != 0):
        r = temp % 10
        _sum = _sum + pow(r, n)
        temp = temp // 10
    return _sum == x


# list comprehension
""" """


def isArmstrong2(val: int) -> bool:
    noOfDigits = order(val)
    digits = [int(_) for _ in str(val)]
    # print(digits)

    _sum = 0
    for d in digits:
        _sum = _sum + d ** noOfDigits
    return _sum == val


""" x = int(input("Enter an armstrong number: "))

print(order(x))
print(isArmstrong2(x)) """

print([_ for _ in range(1000) if isArmstrong2(_)])


import math
import sys

def NthArmstrong(n): 
  
    count = 0 
      
    # upper limit from integer  
    # for i in range(1, sys.maxsize): 
    for i in range(1, 1000):
  
        rem = 0 
        digit = 0 
        sum = 0 
          
        # Copy the value for num in num  
        num = i 
          
        # Find total digits in num  
        digit = int(math.log10(num) + 1) 
          
        # Calculate sum of power of digits  
        while(num > 0): 
            rem = num % 10 
            sum = sum + pow(rem, digit) 
            num = num // 10 
          
        # Check for Armstrong number  
        if i == sum:
            count += 1 
        if count == n:
            return i

n = 12
print(NthArmstrong(n))