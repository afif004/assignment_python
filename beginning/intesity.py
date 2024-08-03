import math
I = float(input("I: "))
Iref = float(input("Iref: "))
dB = 10 * math.log10(I / Iref)
print(dB)