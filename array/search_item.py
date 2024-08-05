N = int(input())
arr =[]
for i in range(N):
    arr.append(int(input()))
item = int(input("Search: "))
found = 0

for i in range(N):
    if arr[i] == item:
        print(f"Item found at location: {i}")
        found = 1
        break
if not found:
    print("ITEM Not Found")