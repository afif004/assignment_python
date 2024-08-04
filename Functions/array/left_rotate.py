def left_rotate(arr):
    fst_elmnt = arr[0]
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]
    arr[-1] = fst_elmnt
    return arr
N = int(input("Number of elements: "))
arr = [int(input()) for i in range(N)]
rotated_arr = left_rotate(arr)
print("Rotated list:", arr)