def print_num(n):
    if n>0:
        print_num(n-1)
        print(n)
N = int(input())
print_num(N)