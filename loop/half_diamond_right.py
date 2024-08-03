N = int(input())

# First pattern
for i in range(1, N + 1):
    print("*" * i)

# Second pattern
for i in range(1, N):
    print("*" * (N - i))
