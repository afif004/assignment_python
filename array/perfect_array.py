import math

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def perfect_number(n):
    if prime(2**n - 1):
        perfect = (2**n - 1) * 2**(n-1)
        return perfect
    return None

N = int(input())
perfect = []
n = 2
pnum_count = 0

while pnum_count < N:
    perfect_num = perfect_number(n)
    if perfect_num:
        perfect.append(perfect_num)
        pnum_count += 1
    n += 1

print(perfect[N-1])
print(perfect)