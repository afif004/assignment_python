e = float(input("Electricity usage in units: "))
    
if e > 0 and e <= 199:
    print(f"Electricity Bill = {e * 1.2:.2f} Tk.")
elif e >= 200 and e < 400:
    print(f"Electricity Bill = {e * 1.5:.2f} Tk.")
elif e >= 400 and e < 600:
    print(f"Electricity Bill = {e * 1.8:.2f} Tk.")
elif e >= 600:
    print(f"Electricity Bill = {e * 2:.2f} Tk.")