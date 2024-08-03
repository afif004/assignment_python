def find_divisors(N):
    divisors = []
    for val in range(1, N + 1):
        if N % val == 0:
            divisors.append(val)
    return divisors
N = int(input())
divisors = find_divisors(N)
for divisor in divisors:
        print(divisor)