def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y, x%y)
X = int(input("First number (X): "))
Y = int(input("Second number (Y): "))
print(f"GCD of {X} and {Y} is {gcd(X,Y)}")