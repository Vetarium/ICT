#pairs cnt
n = int(input("insert size of array "))
a = list(map(int, input().split()))


cnt = 0
a.sort();
i = 0;
while i < (n - 1):
    if (a[i] == a[i + 1]):
        cnt += 1;
        i = i + 2;
    else:
        i += 1;


print(cnt)