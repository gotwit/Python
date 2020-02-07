"""
compound interest = p * (1 + r/100)^t
p - principal
t - time span
r - rate
"""

def calculateCompoundInterest(principal, time, rate):
    ci = principal * pow((1 + r/100), t)
    return ci

p = float(input("Enter principal: "))
t = int(input("Enter time: "))
r = float(input("Enter rate: "))

print(f"Compound interest: {calculateCompoundInterest(p, t, r)}")

