def sum_of_digits(N):
    total = 0
    while N > 0:
        total += N % 10
        N //= 10
    return total
N = int(input())
result = sum_of_digits(N)
print(result)