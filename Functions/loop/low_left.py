def low_left(N):
    for i in range(1, N + 1):
        stars = '*' * i
        print(stars)
N = int(input())
low_left(N)