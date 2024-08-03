def invert_pyramid(N):
    for i in range(1, N + 1):
        spaces = ' ' * (i -1)
        stars = '*' * ((2 * (N-i+1)) - 1)
        print(spaces + stars)

N = int(input())
print(invert_pyramid(N))