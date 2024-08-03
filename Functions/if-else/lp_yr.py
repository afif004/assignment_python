def is_leap_year(year):
    return ((year % 4 == 0) and (year % 100 != 0 or year % 400 == 0))
year = int(input("Year: "))
if is_leap_year(year):
        print("Leap Year")
else:
        print("Not Leap Year")