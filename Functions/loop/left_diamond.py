def left_diamond(N):
    for i in range(1, N + 1):
        print(' ' * (N - i) + '*' * i)

    for i in range(1, N + 1):
        print(' ' * i + '*' * (N - i))

N = int(input())
left_diamond(N)