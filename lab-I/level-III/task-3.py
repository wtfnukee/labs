from math import cos, sin, e, factorial


def f(x, i):
	return cos(i * x) / factorial(i)


def y(x):
	return e ** cos(sin(x))


eps = 0.0001
i = 0
a = 0.1
b = 1.0
h = 0.1
x = a
sigma = 0

while x <= b:
	while True:
		sigma += (1 + f(x, i))
		i += 1
		if abs(f(x, i)) < eps:
			i = 0
			break
	error = abs(sigma - y(x))
	print(f"{x}: sigma={sigma}, y={y(x)}, error = {error}")
	x += h
	sigma = 0
