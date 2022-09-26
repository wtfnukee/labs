from math import factorial

s = 0
for i in range(6):
	s += (-1) ** i * 5 ** i / factorial(i)
print(f"Значение s = {s}")
