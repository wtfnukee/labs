def y(x):
	if x > 0:
		return 1
	elif -1 < x <= 0:
		return 1 + x
	elif x <= -1:
		return 0


x = float(input("Введите х "))
print(f"Значение функции y({x}) = {y(x)}")
