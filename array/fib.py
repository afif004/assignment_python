fib = [0, 1,]
N = int(input())
for i in range(2, N+1):
    fib.append(fib[i-1] + fib[i-2])
nth_fibonacci = fib[N]
print(nth_fibonacci)