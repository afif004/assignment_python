import math
N = float(input())
n = math.floor(math.sqrt(N))
f = 0
for val in range(2,n+1):
    if N%val==0:
        f = 1
        break
if f == 0:
    print(1)
else:
    print(0)