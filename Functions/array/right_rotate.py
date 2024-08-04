def rotate_right(arr):
    if not arr:
        return arr
    lst_elmnt = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = lst_elmnt
    return arr

N = int(input())
arr = [int(input()) for _ in range(N)]
arr = rotate_right(arr)
print(arr)