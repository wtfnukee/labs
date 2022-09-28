from random import randint

a = [randint(1, 5) for _ in range(5)]
print(f"До изменения{a}")
a[a.index(max(a)) + 1] *= 2
print(f"После изменения {a}")
