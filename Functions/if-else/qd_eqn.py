import math
def calculate_roots(a, b, c):
    det = (b ** 2) - (4 * a * c)
    if det > 0:
        root1 = ((-b) + math.sqrt(det)) / (2 * a)
        root2 = ((-b) - math.sqrt(det)) / (2 * a)
        return root1, root2
    elif det == 0:
        root1 = (-b) / (2 * a)
        return root1, None
    else:
        imgn = (math.sqrt(-det)) / (2 * a)
        root = (-b) / (2 * a)
        return f"{root} + {imgn} i", f"{root} - {imgn} i"

a = float(input("Coefficient of a: "))
b = float(input("Coefficient of b: "))
c = float(input("Coefficient of c: "))
roots = calculate_roots(a, b, c)
if roots[1] is None:
    print(f"root: {roots[0]}")
else:
    print(f"roots: {roots[0]}, {roots[1]}")