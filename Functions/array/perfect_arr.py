import math

def prime(n):
    return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

def perfect_number(n):
    if prime(2**n - 1):
        perfect = (2**n - 1) * 2**(n-1)
        return perfect
    return None

N = int(input("Number of perfect numbers to generate: "))
perfect_numbers = []
n = 2
pnum_count = 0

while pnum_count < N:
    perfect_num = perfect_number(n)
    if perfect_num:
        perfect_numbers.append(perfect_num)
        pnum_count += 1
    n += 1

print(f"Perfect number: {perfect_numbers[N-1]}")
print("All perfect numbers generated:", perfect_numbers)