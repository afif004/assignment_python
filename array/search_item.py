N = int(input())
arr =[]
for i in range(0,N):
    arr.append(int(input()))
item = int(input("Search: "))
found = 0

for i in range(0,N):
    if arr[i] == item:
        print(f"Item found at location: {i}")
        found = True
        break
if not found:
    print("ITEM Not Found")