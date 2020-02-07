def area(radius):
    pi = 3.14159
    return pi * (radius**2)


r = int(input("Enter the radius: "))
print("Area of circle for radius {0} is {1}".format(r, area(r)))
