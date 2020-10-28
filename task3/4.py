s = input()
cnt = 0
arr = ["0", "1"]
chk = False

for i in range(1, len(s)):
    if s[i] not in ["1", "0"]:
        chk = True

    if s[i - 1] == s[i]:
        cnt += 1
    elif s[i - 1] != s[i]:
        cnt = 0

    if (cnt >= 6):
        break
    else:
        continue

if chk == True:
    print("Wrong input!")
else:
    if cnt >= 6:
        print("YES")
    else:
        print("NO")