import math

N = int(input("Number of perfect numbers to generate: "))
perfect_numbers = []
n = 2
pnum_count = 0

while pnum_count < N:
    candidate_prime = 2**n - 1
    is_prime = all(candidate_prime % i != 0 for i in range(2, int(math.sqrt(candidate_prime)) + 1))

    if is_prime:
        perfect_num = candidate_prime * 2**(n-1)
        perfect_numbers.append(perfect_num)
        pnum_count += 1

    n += 1

print(f"Perfect number: {perfect_numbers[N-1]}")
print("All perfect numbers generated:", perfect_numbers)