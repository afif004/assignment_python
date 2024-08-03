dec = int(input())
bin = ""
while (dec):
    bin += str(dec%2)
    dec = dec//2
bin = bin[::-1]
print(bin)