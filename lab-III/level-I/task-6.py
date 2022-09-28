from math import sqrt
from random import randint

vector = [randint(-5, 5) for _ in range(5)]
print(vector)
L = sqrt(sum(map(lambda x: x ** 2, vector)))
print(f"Длина вектора = {L}")
