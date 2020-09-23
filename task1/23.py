import math

side = int(input("Insert the side "))
num = float(input("Insert the qty "))
area = num * (side**2 / (math.tan(math.pi / num)))
print("Area is ", area)



