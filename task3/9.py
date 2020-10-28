n = int(input())
s = str(input())
ant = 0
dan = 0
for i in range(n):
    if (s[i] == "A"):
        ant += 1

    elif (s[i] == "D"):
        dan += 1

if(ant > dan):
    print("Anton")
elif(ant < dan):
    print("Danik")
else:
    print("Friendship")