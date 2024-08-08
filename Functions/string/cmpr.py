def cmpr(S1, S2):
    if S1 > S2:
        return "1"
    elif S1 < S2:
        return "-1"
    else:
        return "0"

s1 = input()
s2 = input()
print(cmpr(s1, s2))