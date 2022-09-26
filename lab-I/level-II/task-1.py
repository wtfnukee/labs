from math import cos

s = 0
eps = 0.0001
i = 1
x = float(input())

while True:
	t = (cos(x) ** i) / i ** 2
	if abs(t) < eps:
		break
	s += t
	i += 1
print(s)
