def low_right(N):
    for i in range(1, N + 1):
        spaces = ' ' * (N-i)
        stars = '*' * i
        print(spaces + stars)
    
N = int(input())
low_right(N)