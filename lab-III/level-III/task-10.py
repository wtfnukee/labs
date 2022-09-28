from random import randint

a = [randint(-5, 5) for i in range(5)]

doubled = []

for i in a:
	doubled.extend([i, i])

print(a)
print(doubled)
