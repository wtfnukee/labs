fst, thd = 0, 0

while True:
	x, y = map(int, input("Введите координаты точки, 0 0 для завершения "))
	if x == y == 0:
		break
	elif x > 0 and y > 0:
		print("Первый квадрант")
		fst += 1
	elif x < 0 and y > 0:
		print("Второй квадрант")
	elif x < 0 and y < 0:
		print("Третий квадрант")
		thd += 1
	elif x > 0 and y < 0:
		print("Четвертый квадрант")
	else:
		print("Невозможно установить квадрант")

print(f"В первом квадранте {fst} точек, в третьем - {thd}")
