a, b, c = map(int, input('Введите стороны ').split())
triangle = sorted([a, b, c])
a, b, c = triangle

if a + b < c:
	print('Неравенство треугольника не выполняется')
	quit()
if min(triangle) < 0:
	print('Отрицательные стороны')


def cos(a, b, c):
	return (a * a + b * b - c * c) / (2 * a * b)


print(f'Косинус равен {cos(a, b, c)}')
if cos(a, b, c) == 0:
	print('Треугольник прямой')
elif cos(a, b, c) > 0:
	print('Треугольник острый')
else:
	print('Треугольник тупой')
