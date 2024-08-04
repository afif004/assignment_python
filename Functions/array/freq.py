def count_frequency(arr):
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    return frequency

def print_frequency(frequency):
    for element, count in frequency.items():
        print(f"{element} occurs {count} times.")

N = int(input("Enter the number of elements: "))
arr = [int(input()) for _ in range(N)]
frequency = count_frequency(arr)
print_frequency(frequency)