def hollow(n):
    for i in range(1, N + 1):
        spaces =' ' * (2 * (N - i))
        stars = '* ' * (2*i -1)
        print(spaces + stars)

N = int(input())
hollow(N)