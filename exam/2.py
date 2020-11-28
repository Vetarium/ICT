#unique year 2013 -> 2014 1987->2013
yr = int(input())
t = h = d = u = 0

while(yr>1000 and yr<9000):
    yr+=1
    t = int(yr % 10)
    h = int((yr / 10) % 10)
    d = int((yr / 100) % 10)
    u = int((yr / 1000) % 10)


    if t != h and t != d and t != u and h != d and h != u and d != u:
        print(yr)
        break
