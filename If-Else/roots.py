import math
import math
a = float(input("Coefficient of a: "))
b = float(input("Coefficient of b: "))
c = float(input("Coefficient of c: "))
det = (b**2) - (4*a*c)
if det>0:
    root1 = ((-b) + math.sqrt((b**2)-(4*a*c)))/(2*a)
    root2 = ((-b) - math.sqrt((b**2)-(4*a*c)))/(2*a)
    print(f"roots: {root1}, {root2}")
elif det==0:
    root1 = (-b)/(2*a)
    print(f"root: {root1}")
else:
    imgn = (math.sqrt(-(det))) / (2*a)
    root = (-b)/(2*a)
    print(f"roots: {root} + {imgn} i, {root}-{imgn} i")