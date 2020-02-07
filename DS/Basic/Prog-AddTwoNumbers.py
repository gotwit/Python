num1 = 10
num2 = 20
result = num1 + num2
print("Sum of {0} and {1} is {2}".format(num1, num2, result))

def add(num1, num2):
    return num1 + num2

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum of {0} and {1} is {2}".format(num1, num2, add(num1, num2)))
