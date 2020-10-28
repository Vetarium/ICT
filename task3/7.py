import string
n = int(input())
s = input()
ans = list(set(s.lower()))
cnt = 0
arr1 = list(string.ascii_lowercase)
arr2 = list(string.ascii_uppercase)

for i in range(0, len(ans)):
    if ans[i] in arr1 or ans[i] in arr2:
        cnt += 1

if cnt == 26:
    print("YES")
else:
    print("NO")