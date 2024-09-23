import math

a = math.sqrt(60**2+154**2)
b = math.sqrt(30**2+54**2)
c = a-b
r = 5.73
Alpha_radian = math.acos((a**2+b**2-c**2) / (2*a*b))
print(Alpha_radian)
# d = math.sqrt(a**2+(b+2*r)**2-2*a*(b+2*r)*Alpha_radian)
#
# print(math.degrees(math.atan(154/60)))
# my_degree = math.acos((a**2+d**2-(b+2*r)**2) / (2*a*d))
# print(my_degree)