N = int(input())
arr =[]
for i in range(0,N):
    arr.append(int(input()))
for i in range(N):
    for j in range(0, N-i-1):
        if arr[j] > arr[j+1]:
           arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
for i in range(N):
        for j in range(0, N-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)