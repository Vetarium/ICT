#Queen

x1 = int(input("Insert the 1st row "))
y1 = int(input("Insert the 1st column "))

x2 = int(input("Insert the 2nd row "))
y2 = int(input("Insert the 2nd column " ))




if abs(x2-x1) == abs(y2-y1) or x1 == x2 or y1 == y2:
    print("Yes")

else: print("NO")