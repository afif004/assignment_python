def sum_freq_odd_even(mn, mx):
    odd_count = 0
    even_count = 0
    odd_sum = 0
    even_sum = 0

    for val in range(mn, mx + 1):
        if val % 2 == 0:
            even_count += 1
            even_sum += val
        else:
            odd_count += 1
            odd_sum += val

    return (f"Number of Odd: {odd_count}\nNumber of Even: {even_count}\nSum of Odd: {odd_sum}\nSum of Even: {even_sum}")

min_val = int(input())
max_val = int(input())
print(sum_freq_odd_even(min_val, max_val))