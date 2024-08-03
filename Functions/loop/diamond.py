def print_diamond_pattern(N):
    def print_line(spaces, stars):
        print(" " * spaces + "*" * stars)

    for i in range(1, N + 1):
        print_line(N - i, 2 * i - 1)
    for i in range(N - 1, 0, -1):
        print_line(N - i, 2 * i - 1)

N = int(input())
print_diamond_pattern(N)