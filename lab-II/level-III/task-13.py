from math import pi, sqrt

while True:
	a, b = map(float, input("Введите a и b, 0 для завершения").split())
	print(f"Площадь прямоугольника - {a * b}")
	print(f"Площадь кольца - {pi * (a * a - b * b)}")
	print(f"Площадь треугольника - {(b * sqrt(a * a - b * b / 4)) / 2}")
