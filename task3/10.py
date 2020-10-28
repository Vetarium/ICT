s = str(input())
s2 = ""
s3 = list(s.lower())

s3[0] = s3[0].upper()
for i in range(len(s)):
    s2 += s3[i]

print(s2)




