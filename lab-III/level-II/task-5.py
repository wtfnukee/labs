from random import randint


def pprint(matrix):
	print('\n'.join(map(str, matrix)))


def transpose(matrix):
	return list(zip(*matrix))


a = [[randint(-5, 5) for i in range(5)] for j in range(4)]
pprint(a)
column = int(input()) - 1
for index, value in enumerate(transpose(a)[column]):
	if value < 0:
		print(f"На позиции {index + 1} первое отрицательное число {value}")
		break
else:
	print("Нету отрицательных чисел в выбранном столбце")
