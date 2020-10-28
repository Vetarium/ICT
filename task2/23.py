n = int(input())

def calc(n):
    res = 0
    for i in range(1, n+1):
        res += i*pow(-1, i)
    return res

print(calc(n))