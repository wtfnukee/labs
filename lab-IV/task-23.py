def S(t, v, a):
	return v * t + a * t * t / 2


first_v = 10
first_a = 1

second_v = 9
second_a = 1.6

t = 0
while True:
	print(f't={t}, первый проехал {S(t, first_v, first_a)}, второй проехал {S(t, second_v, second_a)}')
	if S(t, first_v, first_a) < S(t, second_v, second_a):
		print(f'Через {t} часов второй догонит первого')
	t += 1
	if t == 5: break
