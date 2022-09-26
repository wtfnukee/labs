STANDARD = 10
count = 0

while True:
	result = int(input("Введите результат участника, 0 для завершения"))
	if result == 0:
		break
	count += result <= STANDARD

print(count)
