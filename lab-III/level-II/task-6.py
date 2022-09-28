from random import randint


def check(n):
	if n >= 0: return ' ' + str(n)
	return str(n)


def pprint(matrix):
	for i in matrix:
		print('\t'.join(map(check, i)))


A = [[randint(-5, 5) for i in range(4)] for j in range(7)]

mins = [row.index(min(row)) + 1 for row in A]
pprint(A)
print()
print(mins)
