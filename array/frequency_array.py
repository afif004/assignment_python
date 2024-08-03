N = int(input())
arr =[]
frequency = {}
for i in range(0,N):
    arr.append(int(input()))
    if arr[i] in frequency:
            frequency[arr[i]] += 1
    else:
            frequency[arr[i]] = 1

for element, count in frequency.items():
    print(f"{element} occurs {count} times.")
