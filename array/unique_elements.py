N = int(input())
arr =[]
uniq = []
for i in range(0,N):
    arr.append(int(input()))
    if not arr[i] in uniq:
            uniq.append(arr[i])
for elmnt in uniq:
    print(elmnt)