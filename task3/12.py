n = int(input())
s = str(input())
cnt = 0
res = 0
for i in range(n):
    if(s[i] == "x"):
        cnt+=1
        if(cnt > 2):
            res+=1
    else: cnt=0
print(res)
