N = int(input())

for i in range(1, N+1):
    for j in range(1, N+2):
        if j == i or j == (N + 1 - i):
            print("*", end='')
        else:
            print(" ", end='')
    print()