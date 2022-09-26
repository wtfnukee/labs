from math import atan


def f(x, i):
	return (-1) ** (i + 1) * (x ** (2 * i + 1)) / (4 * i ** 2 - 1)


def y(x):
	return (1 + x * x) * atan(x) / 2 - x / 2


eps = 0.0001
i = 1
a = 0.1
b = 1.0
h = 0.1
x = a
sigma = 0

while x <= b:
	while True:
		print(f"В точке {x} на шаге {i} f(x, i)={f(x, i)}")
		sigma += f(x, i)
		i += 1
		if abs(f(x, i)) < eps:
			print(f"{i} член {f(x, i)} меньше {eps}")
			i = 0
			break
	error = abs(sigma - y(x))
	print(f"x={round(x, 2)}: sigma={sigma}, y={y(x)}, error = {error}")
	x += h
	sigma = 0
	print()
