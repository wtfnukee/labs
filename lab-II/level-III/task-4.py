r_1 = 9
r_2 = 10
a = 0
b = 0
count = 0

while True:
	x, y = map(int, input("Введите координаты точки, 0 0 для завершения ").split())
	if x == y == 0:
		break
	count += r_1 <= (x - a) ** 2 + (y - b) ** 2 <= r_2
print(count)
