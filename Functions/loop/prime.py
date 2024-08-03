import math
def is_prime(N):
    n = math.floor(math.sqrt(N))
    for val in range(2,n+1):
        if N%val==0:
            return 1
    return 0
N = float(input())
print(is_prime(N))