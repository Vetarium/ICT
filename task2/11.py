# smallest PRIME divisor not NATURAL
import math
a = int(input("Insert a number "))
check = False

if a%2 == 0:
    print(2)

i = 3;
while i <= math.sqrt(a):
    if a%i==0:
        print(i)
        check = True
    i+=2

if check == False:
    print(a)