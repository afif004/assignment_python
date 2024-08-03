import math
def is_perfect_number(N):
    div_sum = 1
    sqrt_N = int(math.sqrt(N))
    for val in range(2, sqrt_N + 1):
        if N % val == 0:
            div_sum += val
            if val != N // val:
                div_sum += N // val
    return div_sum == N

N = int(input())
if is_perfect_number(N):
    print("Perfect")
else:
    print("Not Perfect")
