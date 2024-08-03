Num = []
N = int(input())
min = float('inf')
max = float('-inf')
for i in range(1,N+1):
    Num.append(float(input()))
    if (min>Num[i-1]):
        min=Num[i-1]
    elif (max<Num[i-1]):
        max=Num[i-1]
print(min,max) 