def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def gcd_of_list(arr):
    gcd = find_gcd(arr[0], arr[1])
    for num in arr[2:]:
        gcd = find_gcd(gcd, num)
    return gcd

N = int(input("Number of elements: "))
arr = [int(input()) for i in range(N)]
result = gcd_of_list(arr)
print(f"GCD of the given numbers: {result}")