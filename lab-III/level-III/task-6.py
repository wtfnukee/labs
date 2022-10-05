from random import randint

a = [randint(-5, 5) for i in range(10)]
prev = a[0]
counter = 0
_max = 0
for i in a:
	if i < prev:
		counter += 1
	else:
		_max = max(counter, _max)
		counter = 1
	prev = i

print(a)
print(_max)
