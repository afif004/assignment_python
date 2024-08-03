import math
a = float(input("Coefficient of a: "))
b = float(input("Coefficient of b: "))
c = float(input("Coefficient of c: "))
root1 = ((-b) + math.sqrt((b**2)-(4*a*c)))/(2*a)
root2 = ((-b) - math.sqrt((b**2)-(4*a*c)))/(2*a)
print(f"roots: {root1}, {root2}")