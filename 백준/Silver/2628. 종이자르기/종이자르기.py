col, row = map(int, input().split())

N = int(input())

rows, cols = [0, row], [0, col]

for _ in range(N):
    num, w = map(int, input().split())
    if num == 0:
        rows.append(w)
    else:
        cols.append(w)

rows, cols = sorted(set(rows)), sorted(set(cols))

max_row = 0
for i in range(len(rows) - 1):
    length = rows[i + 1] - rows[i]
    max_row = max(max_row, length)

max_col = 0
for i in range(len(cols) - 1):
    length = cols[i + 1] - cols[i]
    max_col = max(max_col, length)

print(max_row * max_col)