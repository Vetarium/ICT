s = str(input())
res = ""
arr = ["A","O","Y","E","U","I","a","o","y","e","u","i",]

for i in range(0, len(s)):
    if s[i] not in arr:
        res += "."
        res += s[i]
print(res.lower())