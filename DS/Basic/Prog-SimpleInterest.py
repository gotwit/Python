# formula
"""
SimpleInterest = (p * t * r)/100
p - principal amount
t - time
r - rate
"""

def calculateSimpleInterest(principal, time, rate):
    si = (principal * time * rate)//100
    return si

p = float(input("Enter principal amount: "))
t = int(input("Enter a time: "))
r = float(input("Enter a interest rate: "))

print(f"Simple interest: {calculateSimpleInterest(p, t, r)}")

