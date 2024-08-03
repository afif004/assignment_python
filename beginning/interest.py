p = float(input("Principal: "))
r = float(input("Rate(%): "))/100
t = float(input("Years: "))
si = (p*t*r)
print("Simple Interest: ", si)

n = float(input("Number of times interest is compounded per year: "))
ci = (p*((1+(r/n))**(n*t))) - p
print("Compound Interest: ", ci)