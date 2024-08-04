def find_min_max(arr):
    min_val = max_val = arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

N = int(input("Number of elements: "))
Num = [float(input()) for i in range(N)]
min_val, max_val = find_min_max(Num)
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")