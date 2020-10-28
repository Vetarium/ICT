s = str(input())
res = ""
arr = ["A","O","Y","E","U","I","a","o","y","e","u","i",]

for i in range(len(s)):
    if s[i] not in arr:
        res += "."
        res += s[i]
print(res.lower())