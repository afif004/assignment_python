def right_diamond(N):
    for i in range(1, N + 1):
        print("*" * i)

    for i in range(1, N):
        print("*" * (N - i))

N = int(input())
right_diamond(N)