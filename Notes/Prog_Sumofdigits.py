'''
13. Write a program which prompts the user for a 3 digit integer and checks whether the middle digit is equal to the sum of the other two digits. The program should print an appropriate response. Hint: use the // and % operations.
Middle digit is equal to sum of first and last digit
363
484
121

Middle digit is not equal to sum of first and last digit
243

Hint:

% gives units placed number
// gives non units placed number
>>> 363%10
3
>>> 363//10
36
>>> 36%10
6
>>> 36//10
3
>>> 3%10
3
>>> 3//10
0
'''


num = int(input("Enter 3 digit number: "))
if len(str(num)) > 3:
    print("Invalid entry, Please enter 3 digit number only")
else:
    sums = 0
    middle = 0
    temp = num
    i = 1
    while temp > 0:
        temp = temp % 10
        if i == 2:
            middle = temp
        else:
            sums = sums + temp
        num = num // 10
        temp = num
        i = i + 1
    if middle == sums:
      print('Middle digit is equal to sum of first and last digit')
    else:
      print("Middle digit is not equal to sum of first and last digit")