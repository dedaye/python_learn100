import math
r = float(input('请输入圆的半径：'))
l = 2*math.pi*r
s = math.pi*r**2
print('圆的周长:%d'%l)
print('圆的面积:%d'%s)

year = float(input('请输入年份：'))
is_leap = (year%4 == 0 and year%100 != 0 or year%400 ==0)
print(is_leap)