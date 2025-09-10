def convert(R, C ,table):
    bombs = []

    for x in range(R):
        for y in range(C):
            if table[x][y] == 'O':
                bombs.append((x, y))

    new_table = [['.'] * C for _ in range(R)]

    dx = [0, 0, 1, 0, -1]
    dy = [0, 1, 0, -1, 0]

    for x in range(R):
        for y in range(C):
            new_table[x][y] = 'O'

    for bx, by in bombs:
        for i in range(5):
            nx = bx + dx[i]
            ny = by + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                new_table[nx][ny] = '.'

    return new_table

R, C, N = map(int, input().split())

table = [list(input()) for _ in range(R)]

if N == 1:
    result = table

elif N % 2 == 0:
    result = [['O'] * C for _ in range(R)]

elif N % 4 == 3:
    result = convert(R, C, table)

else:
    result = convert(R, C, convert(R, C, table))

for row in result:
    print(''.join(row))