#yasha in the pool
n = int(input("Length "))
m = int(input("Width "))

x = int(input("X "))
y = int(input("Y "))
dx = n - x;
dy = m -y;
numb = [x,y,dx,dy]
numb.sort()

if x > n or y > m:
    print("Error Yasha is out of pool")
else:
    print("Shortest way is", numb[0])


