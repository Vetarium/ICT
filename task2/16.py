#local max i hate it!!!

a = []
x = 1;
cnt = 0
while x!=0:
    if x == 0:
        break
    else:
        x = int(input())
        a.append(x)

a.remove(0)
for i in range(len(a)):
    if i == 0:
        cnt = 0;
    if a[i] > a[i-1] and a[i] > a[i + 1]:
        cnt += 1

print(cnt)