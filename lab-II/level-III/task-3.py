glasses = 0

while True:
	weight = int(input("Введите вес, 0 для завершения "))
	if weight == 0:
		break
	glasses += weight < 30

print(f"Нужно {glasses * 0.2} литров молока")
