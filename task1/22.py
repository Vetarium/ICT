import math
import array
from array import *
# a,b,c sides of triangle, hP half perimeter
a = int(input())
b = int(input())
c = int(input())


hP = (a + b + c) / 2

area = math.sqrt(hP * (hP - a) * (hP - b) * (hP - c))
print("area of triangle is", area)