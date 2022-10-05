from random import randint


def check(n):
	if n >= 0: return ' ' + str(n)
	return str(n)


def pprint(matrix):
	for i in matrix:
		print('\t'.join(map(check, i)))


a = [[randint(-5, 5) for i in range(7)] for j in range(5)]
pprint(a)
print()
a.sort(key=lambda row: len([i for i in row if i > 0]), reverse=True)
pprint(a)

'6 16 19 23'
