def find_gcd(x, y):
    while(y):
        x, y = y, x % y    
    return x
     
N = int(input())
Nums = []
Nums.append(int(input()))
Nums.append(int(input()))
gcd = find_gcd(Nums[0], Nums[1])
for i in range(2, N):
    Nums.append(int(input()))
    gcd = find_gcd(gcd, Nums[i])
    
print(gcd)