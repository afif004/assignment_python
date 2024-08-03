N = int(input())
sum = int(0)
for i in range(1, N+1, 2):
    sum = int(sum + i**2)
print(sum)