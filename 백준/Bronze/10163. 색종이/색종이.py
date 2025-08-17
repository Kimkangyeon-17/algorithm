table = [[0] * 1001 for _ in range(1001)]

N = int(input())

for i in range(N):
    x1, y1, x2, y2 = list(map(int, input().split()))

    for x in range(x1, x1 + x2):
        for y in range(y1, y1 + y2):
            table[x][y] = (i+1)

result = []

for i in range(N):
    target_num = i + 1
    total = 0

    for col in range(1001):
        for row in range(1001):
            if table[col][row] == target_num:
                total += 1
    result.append(total)

for r in result:
    print(r)