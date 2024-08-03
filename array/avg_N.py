Num = []
N = int(input())
sum = float(0)
for i in range(1,N+1):
    Num.append(float(input()))
    sum = sum+Num[i-1]
print(sum/N)