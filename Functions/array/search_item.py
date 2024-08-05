def search(item):
    for i in range(N):
        if arr[i] == item:
            print (f"Item found at location: {i}")
            return 1
    print("Item not found")
N = int(input())
arr =[]
for i in range(N):
    arr.append(int(input()))
item = int(input("Search: "))
search(item)