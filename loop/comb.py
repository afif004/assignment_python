n = int(input("n: "))
r = int(input("r: "))

if r > n:
    nCr = 0
else:
    r = min(r, n - r)
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= (n - i)
        denominator *= (i + 1)
    nCr = numerator // denominator

print("nCr: ", nCr)