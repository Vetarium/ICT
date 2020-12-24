#tanya stair monster
n = int(input())
arrGet = [int(i) for i in input().split()]
cnt = 0
arr = []

for i in range(0, len(arrGet)):
    if arrGet[i] == 1:
        cnt += 1 #how many  stairs Tanya climbed
        arr.append(arrGet[i-1]) #prev num before new stair is a lenth of stair

print(cnt)
for i in reversed(arr):
    print(i, end= " ")