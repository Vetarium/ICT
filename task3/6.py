import string
s = input()
arr1 = list(string.ascii_lowercase)
arr2 = list(string.ascii_uppercase)
cnt1 = 0
cnt2 = 0

for i in range(0, len(s)):
    if s[i] in arr1:
        cnt1 += 1
    elif s[i] in arr2:
        cnt2 += 1

if cnt1 >= cnt2:
    print(s.lower())
elif cnt1 < cnt2:
    print(s.upper())
