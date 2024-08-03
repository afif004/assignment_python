def left_triangle(N):
    for i in range(1, N + 1):
        print(" " * (i - 1) + "*" * (N - i + 1))
    
N = int(input())
left_triangle(N)