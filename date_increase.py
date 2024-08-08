from datetime import datetime, timedelta

def increase_date(date_str, days):
    date = datetime.strptime(date_str, "%d/%m/%y")
    new_date = date + timedelta(days=days)
    return new_date.strftime("%d/%m/%y")

date_str = input("Date(dd/mm/yy): ")
days = int(input())
print(f"Date after {days} days: {increase_date(date_str, days)}")