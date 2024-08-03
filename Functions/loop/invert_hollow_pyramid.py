def invert_hollow(N):
    for i in range(1, N + 1):
        spaces = ' ' * (2*i -1)
        stars = '* ' * ((2 * (N-i+1)) - 1)
        print(spaces + stars)
N = int(input())
invert_hollow(N)