X = int(input("First number (X): "))
Y = int(input("Second number (Y): "))

a = X
b = Y

while b:
    a, b = b, a % b

gcd = a
lcm = (X * Y) // gcd
print(f"GCD of {X} and {Y} is {gcd}")
print(f"LCM of {X} and {Y} is {lcm}")
