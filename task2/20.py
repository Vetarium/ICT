import array
n = int(input("insert size of batch "))
k = int(input("insert qty trials  "))

#ar = list(map(int, input().split()))
a = []
for i in range(n):
    a.append("I")
print(a)

i = 0

while i < k:
    x = int(input())
    y = int(input())
    while x<=y:
        a.pop(x-1)
        a.insert(x-1,"0")
        x+=1
    x = 0
    y = 0
    i+=1


print(a)




