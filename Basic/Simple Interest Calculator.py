''' p, r, t = map(int, input("Enter Principle Amount, Rate of intrest and Time period: ").split()) -- Mutiple input at once '''

p = float(input("Enter Principal (₹): "))
r = float(input("Enter Rate of Interest (%): "))
t = float(input("Enter Time (in years): "))

def simple_intrest(p, r, t):
    return p*r*t/100
print(simple_intrest(p, r, t))