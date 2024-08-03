N = int(input())
bin = 0
place_value = 1
while N > 0:
    remainder = N % 2
    bin += remainder * place_value
    place_value *= 10
    N //= 2
print(bin)