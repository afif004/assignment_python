def sum_of_sqrs(N):
    m = (N + 1) // 2
    total = m * (2 * m - 1) * (2 * m + 1) // 3
    return total

N = int(input())
print(sum_of_sqrs(N))