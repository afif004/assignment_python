N = int(input())
arr =[]
for i in range(0,N):
    arr.append(int(input()))
lst_elmnt = arr[N-1]
for i in range(N-1,0, -1):
    arr[i] = arr[i-1]
arr[0] = lst_elmnt
print(arr)