# import math
#
# n = float(input("Enter any Number: "))
# ans =  math.sqrt(n)
# print("Square is : ", ans)
#
#===========================================

# from math import sqrt
# a = float(input("Enter value of a: "))
# b = float(input("Enter value of b: "))
# c = float(input("Enter value of c: "))
#
# r1 = ((-b) + sqrt(b*b - 4*a*c)/(2*a))
# r2 = ((-b) - sqrt(b*b - 4*a*c)/(2*a))
#
# print("Result is : ",r1)
# print("Result is : ",r2)
# ===============================================

# from math import sqrt, pow
# a = float(input("Enter value of x1: "))
# b = float(input("Enter value of x2: "))
# c = float(input("Enter value of y1: "))
# d = float(input("Enter value of y2: "))
#
# dis = sqrt(((b-a)**2) + ((d-c)**2))
# dis2 = sqrt(pow((b-a),2) + pow((d-c),2))
#
# print("Distance is : ", dis)
# print("Distance is : ", dis2)
# =======================================================

from math import *

angle = float(input("Enter tha angle: "))
angle1 = angle*3.14/180

ans = sin(angle1)
print(f"sin({angle}) = {angle1}")

ans = cos(angle1)
print(f"cos({angle}) = {angle1}")

ans = tan(angle1)
print(f"tan({angle}) = {angle1}")
