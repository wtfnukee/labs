from math import sin, pi

k = 0
while True:
	x, y = map(float, input("Введите координаты точки, 0 0 для завершения").split())
	if x == y == 0:
		break
	if 0 <= x <= pi and 0 <= y <= sin(x):
		k += 1
print(k)
