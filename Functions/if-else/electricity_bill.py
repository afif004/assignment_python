def calculate_electricity_bill(units):
    if units > 0 and units <= 199:
        return units * 1.2
    elif units >= 200 and units < 400:
        return units * 1.5
    elif units >= 400 and units < 600:
        return units * 1.8
    elif units >= 600:
        return units * 2
    return 0.0

units = float(input("Electricity usage in units: "))
bill = calculate_electricity_bill(units)
print(f"Electricity Bill = {bill:.2f} Tk.")