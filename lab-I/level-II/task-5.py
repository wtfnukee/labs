n = int(input())
m = int(input())
N = n
div = 0
while True:
	if n - m >= 0:
		n -= m
		div += 1
	else:
		break
print(div, N - div * m)
