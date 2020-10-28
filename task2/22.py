a = list(map(int, input().split()))

pl = a[2]
n =a[0]
m =a[1]
res = 1
k = 0
j = 0


k = n//pl
j  = m//pl

if(pl*k!=n):
    k+=1

if (pl * j != m):
    j += 1

res = k*j

print(res)