N = int(input())
for i in range(1, N+1):
    spaces = N - i
    digits = ' '.join(str(d) for d in range(i, 2*i))
    print((' ' * (spaces)) + digits)