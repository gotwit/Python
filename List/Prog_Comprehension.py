import functools
""" For example :

lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1] 

here, x ** 2 is output expression, 
      range (1, 11)  is input sequence, 
      x is variable and   
      if x % 2 == 1 is predicate part. """

""" A list comprehension generally consist of these parts :

Output expression,
Input sequence,
A variable representing a member of the input sequence and
An optional predicate part. """

odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(f"Odd squares: {odd_square}\n")

odd_square = []

for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x ** 2)
print(f"Odd square: {odd_square}\n")


power_of_2 = [2 ** x for x in range(1, 5)]
print(f"Power of 2: {power_of_2}\n")


noPrimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
print(noPrimes)
primes = [i for i in range(2, 50) if i not in noPrimes]
print(primes)

lowercase = [x.lower() for x in ["A", "B", "C"]]
print(lowercase)

string = "I am you 1234."
numbers = [x for x in string if x.isdigit()]
print(numbers)

a = 5
table = [[a, b, a * b] for b in range(1, 11)]
for t in table:
    print(t)


lst = list(range(1, 11))
print(lst)

# [start index : end index]
lst_1_5 = lst[1:5]
print(lst_1_5)

lst_5_8 = lst[5:8]
print(lst_5_8)

lst_1_ = lst[1:]
print(lst_1_)

lst_5 = lst[:5]
print(lst_5)

lst_1_8_2 = lst[1:8:2]
print(lst_1_8_2)

lst_rev = lst[::-1]
print(lst_rev)

lst_9_5_2 = lst[9:4:-2]
print(lst_9_5_2)

lst_9_5_1 = lst[9:4:-1]
print(lst_9_5_1)

lst = filter(lambda x: x % 2 == 1, range(1, 20))
print(list(lst))

lst = filter(lambda x: x %
             5 == 0, [x ** 2 for x in range(2, 11) if x % 2 == 1])
print(list(lst))

# A range is from >= start and <= end (excluding)
print(list(range(-5, 5)))
lst = filter(lambda x: x < 0, range(-5, 5))
print(list(lst))


#  implementing max() function, using
print(functools.reduce(lambda a, b: a if (a > b) else b, [7, 12, 45, 100, 15]))
