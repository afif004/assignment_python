def num_pyramid(N):
    for i in range(1, N + 1):
        print("  " * (N - i), end='')
        for j in range(1, ((2*i))):
            print(f"{i + j - 1} ", end='')
        print()
N = int(input())
num_pyramid(N)