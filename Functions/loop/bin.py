def decimal_to_binary(N):
    binary = 0
    place_value = 1
    while N > 0:
        remainder = N % 2
        binary += remainder * place_value
        place_value *= 10
        N //= 2
    return binary

N = int(input())
binary = decimal_to_binary(N)
print(binary)