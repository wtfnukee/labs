from random import randint


def pprint(matrix):
	print('\n'.join(map(str, matrix)))


A = [[randint(-5, 5) for i in range(6)] for j in range(8)]
pprint(A)
print()
s = 0
n = 0
max_value = 0
max_pos = (0, 0)
for row in A:
	for elem in row:
		if elem > 0:
			s += elem
			n += 1
		if elem > max_value:
			max_pos = A.index(row), A[A.index(row)].index(elem)
			max_value = elem
A[max_pos[0]][max_pos[1]] = s / n
pprint(A)