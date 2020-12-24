#heist
n = int(input())
arrGet = [int(i) for i in input().split()]
arrGet.sort()
res = 0
res = arrGet[n - 1] - arrGet[0] - n + 1 #this formula to know the initial num and - remaining
print(res)

