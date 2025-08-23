import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

def dfs(x, y, graph, visited, h, w):
    visited[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(nx, ny, graph, visited, h, w)


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    visited = [[False] * w for _ in range(h)]

    count = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j, graph, visited, h, w)
                count += 1

    print(count)