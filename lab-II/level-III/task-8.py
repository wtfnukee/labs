from math import sqrt, inf

minima = (0, inf)
i = 0
while True:
	i += 1
	x, y = map(int, input("Введите координаты точки, 0 0 для завершения ").split())
	if x == y == 0:
		break
	rho = sqrt(x ^ 2 + y ^ 2)
	if rho < minima[1]:
		minima = (i, rho)
print(f"Ближайшая к началу координат точка с номером {minima[0]}, расстояние {minima[1]}")
