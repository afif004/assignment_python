def calculate_average(N):
    sum = 0.0
    for _ in range(N):
        num = float(input())
        sum += num
    return sum / N

N = int(input())
average = calculate_average(N)
print(average)