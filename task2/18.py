#shifting in array
n = int(input("insert size of array "))
a = list(map(int, input().split()))
b = []
cnt = 0

a.insert(0, a.pop())

print(a)
