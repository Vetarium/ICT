#unique array
import numpy
n = int(input("insert size of array "))
a = list(map(int, input().split()))
b = []
cnt = 0;
for i in a:
    if i not in b:
        b.append(i)
        cnt+=1

print(cnt)

