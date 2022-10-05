from random import randint

a = [randint(-5, 5) for i in range(10)]


def unique(lst):
	bin = []
	for i in a:
		if i not in bin:
			bin.append(i)
	return bin


print(a)
print(unique(a))
