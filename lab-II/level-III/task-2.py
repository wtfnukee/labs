r = 9
a = 0
b = 0
count = 0

while True:
	x, y = map(int, input("Введите координаты точки, 0 0 для завершения ").split())
	if x == y == 0:
		break
	count += (x - a) ** 2 + (y - b) ** 2 <= r
print(count)
