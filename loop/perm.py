n = int(input("n: "))
r = int(input("r: "))
if r > n:
    result = 0
elif r == 0:
    result = 1
else:
    result = 1
    for i in range(n - r + 1, n + 1):
        result *= i
print("nPr:", result)