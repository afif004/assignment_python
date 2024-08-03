def num_cone(N):
    for i in range(1, N+1):
        spaces = N - i
        digits = ' '.join(str(d) for d in range(i, 2*i))
        print((' ' * (spaces)) + digits)

N = int(input())
num_cone(N)