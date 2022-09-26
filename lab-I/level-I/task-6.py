def y(x):
	return 0.5 * x * x - 7 * x


for i in range(-8, 9):
	print(f"x = {i / 2}; y = {y(i / 2)}")
