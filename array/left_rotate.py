N = int(input())
arr =[]
for i in range(0,N):
    arr.append(int(input()))
fst_elmnt = arr[0]
for i in range(0,N-1):
    arr[i] = arr[i+1]
arr[N-1] = fst_elmnt
print(arr)