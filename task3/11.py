n = int(input())
s = str(input())
l = 0;
r = 0;
res = ""
for i in range(n):
    if(s[i] == "z"):
        l+=1

    elif(s[i] == "n"):
        r+=1

while(r):
    res+= "1 "
    r-=1
while(l):
    res+= "0 "
    l-=1

print(res)