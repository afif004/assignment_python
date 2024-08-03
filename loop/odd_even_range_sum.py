min_value = int(input("Minimum: "))
max_value = int(input("Maximum: "))
odd_count = 0
even_count = 0
odd_sum = 0
even_sum = 0

for val in range(min_value, max_value + 1):
    if val % 2 == 0:
        even_count += 1
        even_sum += val
    else:
        odd_count += 1
        odd_sum += val

print(f"Number of Odd: {odd_count}\nNumber of Even: {even_count}\nSum of Odd: {odd_sum}\nSum of Even: {even_sum}")
