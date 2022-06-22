""" for i in range(10):
    print(i, end=' ')

    
0 1 2 3 4 5 6 7 8 9 
for i in range(5, 10, 1):
    print(i, end=' ')

    
5 6 7 8 9 
for i in range(5, 10, 2):
    print(i, end=' ')

    
5 7 9 
for i in range(10,,-1):
    
SyntaxError: expected ':'
for i in range(10, 0, -1):
    print(i, end=' ')

    
10 9 8 7 6 5 4 3 2 1 

for i in range(9, -1, -1):
    print(i, end=' ')

    
9 8 7 6 5 4 3 2 1 0 
for i in range(5, -1, -1):
    print(i, sep=' ')

    
5
4
3
2
1
0
for i in range(5, -1, -1):
    print(i, end=',', sep=' ')

    
5,4,3,2,1,0,
for i in range(5, -6, -1):
    print(i, end=' ')

    
5 4 3 2 1 0 -1 -2 -3 -4 -5 

list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for(int i = 0; i < n; i++)

 """
""" 
2: (2,2) =>  
3: (2,3) =>  2 
4: (2,4) =>  2 3 
5: (2,5) =>  2 3 4 
6: (2,6) =>  2 3 4 5 
7: (2,7) =>  2 3 4 5 6 
8: (2,8) =>  2 3 4 5 6 7 
9: (2,9) =>  2 3 4 5 6 7 8 
 """
""" 
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x, ' & is not a prime number')
            break
    else:
        print(n, 'is a prime number')
 """
""" 
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print("Found an odd number %(n)d" % {'n': num})
 """
 