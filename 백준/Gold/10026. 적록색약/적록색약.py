import sys
sys.setrecursionlimit(10000)

N = int(input())

area = [list(input()) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs_stack(start_x, start_y, visited, is_color_blind = False):
    stack = [(start_x, start_y)]
    color = area[start_x][start_y]

    while stack:
        x, y = stack.pop()

        if visited[x][y]:
            continue

        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                next_color = area[nx][ny]

                same_region = False
                if is_color_blind:
                    if (color in 'RG' and next_color in 'RG') or color == next_color:
                        same_region = True

                else:
                    if color == next_color:
                        same_region = True

                if same_region:
                    stack.append((nx, ny))

def count_regions(is_color_blind = False):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs_stack(i, j, visited, is_color_blind)
                count += 1

    return count

normal_count = count_regions(False)

blind_count = count_regions(True)

print(normal_count, blind_count)