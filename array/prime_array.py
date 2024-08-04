def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def generate_primes(limit):
    primes = []
    num = 2
    while len(primes) < limit:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

N = int(input("Number of primes: "))
primes = generate_primes(N)
print(f"Prime array: {primes}")
print(primes[N-1])