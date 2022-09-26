from math import pi, sqrt

R = float(input("Введите площадь круга"))
S = float(input("Введите площадь квадрата "))

r = sqrt(R / pi)
a = sqrt(S) / 2

if r <= a:
	print("Круг помещается в квадрат")
else:
	print("Круг не помещается в квадрат")
