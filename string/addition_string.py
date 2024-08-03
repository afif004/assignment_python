s1=input()
s2=input()
if len(s2) > len(s1):
        s1, s2 = s2, s1
s1 = s1[::-1]
s2 = s2[::-1]
s3 = ""
carry = 0
for i in range (len(s1)):
    d1 = int(s1[i])
    d2 = int(s2[i]) if i < len(s2) else 0
    total = d1 + d2 + carry
    carry = total//10
    s3 += str(total%10)
if carry:
        s3 += str(carry)
s3 = s3[::-1]
print(s3)