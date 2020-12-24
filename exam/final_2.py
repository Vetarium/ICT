#mnogougolniki

n = int(input())

for i in range(n):
    n,m = map(int,input().split())
    if n%m == 0:  # if i can divide n on m it means that i can put m angle figure inside n angle with the same center
        #like hexagon and triangle will looks like David star
        print("YES")
    else:
        print("NO")