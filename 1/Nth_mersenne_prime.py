def f(n,i=1,j=0):
    while j!=n:
        i+=1;m=2**i-1;j+=all(m%k for k in range(2,m))
    print(m)
f(7)