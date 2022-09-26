k = 0
marks = []
while True:
	bad = 1
	for i in range(1, 5):
		mark = int(input(f"Введите {i}-ю оценку, 0 для завершения"))
		if mark == 0:
			print(f"Неуспевающих студентов - {k}, средний балл - {sum(marks) / len(marks)}")
			quit()
		bad *= mark != 2
		marks.append(mark)
	if not bad:
		k += 1
