import random

print("1. macierz")
size = 2
rows = {}
for i in range(size):
    rows[i] = []
    for _ in range(size):
        rows[i].append(random.randint(0,10))
    print(str(rows[i]))

print("Wyznacznik ")
det = rows[0][0] * rows[1][1] + rows[1][0] * rows[0][1]
print(det)