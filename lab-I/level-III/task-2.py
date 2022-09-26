from math import cos, sin, pi


def f(x, i):
	return x ** i * sin(i * pi / 4)


def y(x):
	return (x * sin(pi / 4)) / (1 - 2 * x * cos(pi / 4) + x * x)


eps = 0.0001
i = 1
a = 0.1
b = 0.8
h = 0.1
x = a
sigma = 0

while x <= b:
	while True:
		sigma += f(x, i)
		i += 1
		if abs(x ** i) < eps:
			i = 0
			break
	error = abs(sigma - y(x))
	print(f"{x}: sigma={sigma}, y={y(x)}, error = {error}")
	x += h
	sigma = 0
