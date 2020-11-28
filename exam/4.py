#ways to organise employees

n = int(input())
ways = 0;

for i in range( 1, 1 + n //2):
    if(n - i) % i == 0:
        ways+=1

print(ways)
