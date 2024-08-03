N = int(input())
div_sum = int(0)
for val in range(1,N):
    if(N%val==0):
        div_sum = div_sum + val
if div_sum==N:
    print("Perfect")
else:
    print("Not Perfect")