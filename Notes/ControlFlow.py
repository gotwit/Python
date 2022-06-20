for i in range(10):
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

