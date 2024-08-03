def reverse_number(N):
    rev = 0
    while N > 0:
        rev = rev * 10 + N % 10
        N = N // 10 
    return rev

N = int(input())
print(reverse_number(N))