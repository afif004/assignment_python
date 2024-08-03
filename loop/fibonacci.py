N = int(input())
a = int(0)
b = int(1)
if N==1:
    print(a)
elif N==2:
        print(a)
        print(b)
else:
    print(a)
    print(b)
    while(N-2):
        c=a+b
        print(c)
        a=b
        b=c
        N=N-1