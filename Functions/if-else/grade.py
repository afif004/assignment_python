def grade(n):
    if m>80:
        return ("A+")
    elif m>=75 and m<80:
        return ("A")
    elif m>=70 and m<75:
        return ("A-")
    elif m>=65 and m<70:
        return ("B+")
    elif m>=60 and m<65:
        return ("B")
    elif m>=55 and m<60:
        return ("B-")
    elif m>=50 and m<55:
        return ("C+")
    elif m>=45 and m<50:
        return ("C")
    elif m>=40 and m<45:
        return ("D")
    else:
        return ("F")
m = int(input())
print(grade(m))