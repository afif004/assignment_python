N = int(input())
sum = int(0)
while(int(N)>int(0)):
    sum = int(sum + N%10)
    N = int(N/10)
print(sum)