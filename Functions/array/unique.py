def unique(N):
    arr =[]
    uniq=[]
    for i in range(N):
        arr.append(int(input()))
        if not arr[i] in uniq:
            uniq.append(arr[i])
    return uniq
N = int(input())
uniq = unique(N)
for elmnt in uniq:
    print(elmnt, end=' ')