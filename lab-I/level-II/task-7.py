current = 10
s = 0
for i in range(7):
	s += current
	current *= 1.1
print(f"а) за 7 дней спортсмен пробежит {s} км")

current = 10
time = 0
s = 0
while s < 100:
	s += current
	time += 1
	current *= 1.1
print(f"б) за {time} дней спортсмен пробежит 100 км")

current = 10
time = 0
while current < 20:
	time += 1
	current *= 1.1
print(f"в) через {time} дней спортсмен будет пробегать в день больше 20 км ({current})")
