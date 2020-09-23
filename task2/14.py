#largest cnt
import numpy as np

a = []
x = 1;
cnt = 0
while x!=0:
    x = int(input())
    a.append(x)

max = np.max(a)

print("biggest val is ",max)

for i in range (len(a)):
    if max == a[i]:
        cnt+=1

print("cnt is ", cnt)



