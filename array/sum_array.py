a = [i for i in range(100)]
b = [i*2 for i in range(100)]
c = [0] * 100
for i in range(100):
    c[i] = a[i] + b[i]
print(c)