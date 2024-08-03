def compute_nCr(n, r):
    if r > n:
        return 0
    r = min(r, n - r)
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= (n - i)
        print(numerator)
        denominator *= (i + 1)
        print(denominator)
    return numerator // denominator

n = int(input("n: "))
r = int(input("r: "))
nCr = compute_nCr(n, r)
print("nCr: ", nCr)