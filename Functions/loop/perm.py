def factorial_range(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

def calculate_nPr(n, r):
    if r > n:
        return 0
    if r == 0:
        return 1
    return factorial_range(n - r + 1, n)

n = int(input("n: "))
r = int(input("r: "))
nPr = calculate_nPr(n, r)
print("nPr:", nPr)