from random import randint


def pprint(matrix):
	print('\n'.join(map(str, matrix)))


a = [[randint(-5, 5) for i in range(5)] for j in range(4)]
pprint(a)
print()
max_v = 0
max_i = 0
for index, value in enumerate(a):
	if value[2] > max_v:
		max_v = value[2]
		max_i = index
a[max_i], a[3] = a[3], a[max_i]
pprint(a)
