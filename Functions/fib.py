memo={}
def nth_fib(n):
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 0
        return 0
    elif n == 1:
        memo[n] = 1
        return 1
    else:
        memo[n] = nth_fib(n-1) + nth_fib(n-2)
        return memo[n]
    
def fib_series(n):
    if n >= 0:
        fib_series(n-1)
        print(nth_fib(n), end=' ')
        
N = int(input())
print("Fibonacci series:")
fib_series(N)
print()
print(f"{N}th Fibonacci number: {nth_fib(N)}")