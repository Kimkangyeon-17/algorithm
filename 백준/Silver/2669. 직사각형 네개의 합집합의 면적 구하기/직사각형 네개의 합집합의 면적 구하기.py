table = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            table[x][y] += 1

total = 0

for x in range(100):
    for y in range(100):
        if table[x][y] >= 1:
            total += 1

print(total)