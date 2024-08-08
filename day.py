from datetime import datetime, timedelta
def find_day_of_week(date_str):
    date = datetime.strptime(date_str, "%d/%m/%y")
    return date.strftime("%A")

date_str = input("Date(dd/mm/yy): ")
print(f"Day of week for {date_str}: {find_day_of_week(date_str)}")