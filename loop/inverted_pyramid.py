N = int(input())

for i in range(1, N + 1):
    spaces = ' ' * (i -1)
    stars = '*' * ((2 * (N-i+1)) - 1)
    print(spaces + stars)