from math import pi, sqrt

n = int(input("Введите количество пар "))
for _ in range(n):
	a, b = map(float, input("Введите a и b").split())
	print(f"Площадь прямоугольника - {a * b}")
	print(f"Площадь кольца - {pi * (a * a - b * b)}")
	print(f"Площадь треугольника - {(b * sqrt(a * a - b * b / 4)) / 2}")
