n = int(input())
s = str(input())
l = 0;
r = 0;
for i in range(n):
    if(s[i] == "z"):
        l+=1

    elif(s[i] == "n"):
        r+=1

while(r):
    print(1)
    r-=1
while(l):
    print(0)
    l-=1