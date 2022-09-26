males, females = [], []

while True:
	height, sex = input("Введите рост и пол (f/m) через пробел. 0 0 для остановки ввода").split()
	if sex == 'm':
		males.append(int(height))
	elif sex == 'f':
		females.append(int(height))
	elif height == sex == '0':
		print(f"Средний рост мальчиков {sum(males) / len(males)} \n"
		      f"Средний рост девочек {sum(females) / len(females)}")
		break
	else:
		print('Неверные аргументы')
