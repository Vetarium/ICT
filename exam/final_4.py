#Rick shahmaty
n = int(input())
arr = []
for i in range(1, n):
    tst = 1*i + 2*(1 * (i - 1)) + i
    if(tst <= n - i + 1):
        arr.append(i)

print(arr[len(arr)-1])#easiest way to get the biggest value of K