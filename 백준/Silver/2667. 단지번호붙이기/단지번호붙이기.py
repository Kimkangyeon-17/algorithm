N = int(input())

graph = [list(map(int, input())) for _ in range(N)]


visited = [[False] * N for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    visited[x][y] = True
    count = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
            count += dfs(nx, ny)

    return count

apartment_count = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            house_count = dfs(i, j)
            apartment_count.append(house_count)

print(len(apartment_count))
apartment_count.sort()
for count in apartment_count:
    print(count)