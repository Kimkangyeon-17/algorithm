import sys
sys.setrecursionlimit(10000)


N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs_stack(start_x, start_y, height, visited):
    stack = [(start_x, start_y)]

    while stack:
        x, y = stack.pop()

        if visited[x][y]:
            continue

        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and area[nx][ny] > height:
                stack.append((nx, ny))

def count_area(height):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if area[i][j] > height and not visited[i][j]:
                dfs_stack(i, j, height, visited)
                count += 1

    return count

max_safe_area = 0
max_height = max(max(row) for row in area)

for height in range(max_height + 1):
    safe_area = count_area(height)
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)