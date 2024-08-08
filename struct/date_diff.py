from datetime import datetime
def date_diff(date1, date2):
    d1 = datetime.strptime(date1, "%d/%m/%y")
    d2 = datetime.strptime(date2, "%d/%m/%y")
    return abs((d2 - d1).days)
d1 = input()
d2 = input()
print(f"{date_diff(d1,d2)} days")