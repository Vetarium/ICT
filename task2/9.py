#korobki
a = int(input("Height of the 1st box"))
b = int(input("Width of the 1st box"))
c = int(input("Length of the 1st box"))

v1 = a*b*c

a2 = int(input("Height of the 2nd box"))
b2 = int(input("Width of the 2nd box"))
c2 = int(input("length of the 2nd box"))

v2 = a2*b2*c2

if v1 == v2:
    print("Boxes are equal")
else:
    if v1 > v2: print("The first box is larger than the second one")
    else: print("The first box is smaller than the second one")


