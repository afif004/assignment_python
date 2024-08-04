import math

N = int(input("Number of primes: "))

primes = []
num = 2

while len(primes) < N:
    if num > 1:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    num += 1

print(f"Prime array: {primes}")
print(primes[N-1])
