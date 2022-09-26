from math import inf

best = inf
while True:
	time = int(input())
	if time == 0:
		break
	best = min(time, best)

print(best)
