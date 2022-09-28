from random import randint

a = [randint(-5, 5) for i in range(10)]
print(a)

a[::2] = sorted(a[::2])

print(a)
