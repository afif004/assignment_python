def binary(dec):
    bin = ""
    while (dec):
        bin += str(dec%2)
        dec = dec//2
    bin = bin[::-1]
    return bin
dec = int(input())
print(binary(dec))