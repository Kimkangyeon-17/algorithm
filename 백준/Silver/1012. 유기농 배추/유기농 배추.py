import sys
sys.setrecursionlimit(10000)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    table = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        table[x][y] = 1

    visited = [[False] * (N) for _ in range(M)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def dfs(x, y):
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and table[nx][ny] == 1:
                dfs(nx, ny)


    count = 0

    for i in range(M):
        for j in range(N):
            if table[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1

    print(count)
