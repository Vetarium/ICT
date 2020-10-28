s = input()
s = sorted(s)
res = ""
arr = ["1","2","3"]
for i in range(0, len(s)):
    if s[i] in arr:
        res += s[i]
        res += "+"

print(res[:len(res) - 1])
#3

s = input()

res = s[:1].upper() + s[1:]
print(res)