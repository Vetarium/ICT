#task 1 input
#3
#4 1 7
#-2 4 -1
#1 -5 -3
#output
#NO

coordinates = int(input())
x1 = y1 = z1 = 0

for i in range(coordinates):
    x,y,z = map(int,input().split())
    x1 += x
    y1 += y
    z1 += z
if x1 == 0 and y1 == 0 and z1 == 0:
    print("YES")
else:
    print("NO")


