k = 0
while True:
	bad = 1
	for i in range(1, 5):
		mark = int(input(f"Введите {i}-ю оценку, 0 для завершения"))
		if mark == 0:
			print(f"Студентов без 2 и 3 - {k}")
			quit()
		bad *= (mark != 2 and mark != 3)
	if not bad:
		k += 1
