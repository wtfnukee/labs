from math import atan


def f(x, i):
	return (-1) ** i * (x ** (2 * i + 1)) / (2 * i + 1)


def y(x):
	return atan(x)


eps = 0.0001
i = 0
a = 0.1
b = 0.5
h = 0.05
x = a
sigma = 0

while x <= b:
	while True:
		sigma += f(x, i)
		i += 1
		if abs(f(x, i)) < eps:
			i = 0
			break
	error = abs(sigma - y(x))
	print(f"{round(x, 2)}: sigma={sigma}, y={y(x)}, error = {error}")
	x += h
	sigma = 0
