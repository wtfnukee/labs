from math import pi, sqrt

while True:
	r = int(input("Введите r, 0 для завершения"))
	if r == 0:
		break
	print(f"Площадь квадрата со стороной {r} = {r * r}")
	print(f"Площадь круга радиусом {r} = {pi * r * r}")
	print(f"Площадь равностороннего треугольника со стороной {sqrt(3) * r * r / 4} = {pi * r * r}")
