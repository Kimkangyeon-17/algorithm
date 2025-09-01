from collections import deque

N, M = map(int, input().split())

space = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

distance = [[-1] * M for _ in range(N)]

for x in range(N):
    for y in range(M):
        if space[x][y] == 1:
            queue.append((x, y))
            distance[x][y] = 0

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

while queue:
    x, y = queue.popleft()

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and distance[nx][ny] == -1:
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))

max_distance = 0
for x in range(N):
    for y in range(M):
        if distance[x][y] > max_distance:
            max_distance = distance[x][y]

print(max_distance)