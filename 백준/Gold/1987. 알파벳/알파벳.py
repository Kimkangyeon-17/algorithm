import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

R, C = map(int, input().split())

table = [list(input()) for _ in range(R)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
max_result = 0

def dfs(x, y, visited, count):
    global max_result, R, C, table

    if count > max_result:
        max_result = count

    if count == 26:
        return

    # 위
    if x > 0:
        char_bit = 1 << (ord(table[x - 1][y]) - 65)  # ord('A') = 65
        if not (visited & char_bit):
            dfs(x - 1, y, visited | char_bit, count + 1)

    # 아래
    if x < R - 1:
        char_bit = 1 << (ord(table[x + 1][y]) - 65)
        if not (visited & char_bit):
            dfs(x + 1, y, visited | char_bit, count + 1)

    # 왼쪽
    if y > 0:
        char_bit = 1 << (ord(table[x][y - 1]) - 65)
        if not (visited & char_bit):
            dfs(x, y - 1, visited | char_bit, count + 1)

    # 오른쪽
    if y < C - 1:
        char_bit = 1 << (ord(table[x][y + 1]) - 65)
        if not (visited & char_bit):
            dfs(x, y + 1, visited | char_bit, count + 1)


start_bit = 1 << (ord(table[0][0]) - 65)
dfs(0, 0, start_bit, 1)
print(max_result)