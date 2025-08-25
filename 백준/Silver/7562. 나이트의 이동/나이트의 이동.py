from collections import deque

T = int(input())

for tc in range(T):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    if start_x == end_x and start_y == end_y:
        print(0)
        continue

    queue = deque([(start_x, start_y, 0)])
    visited = [[False] * l for _ in range(l)]
    visited[start_x][start_y] = True

    while queue:
        x, y, moves = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                if nx == end_x and ny == end_y:
                    print(moves + 1)
                    break

                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))

        else:
            continue
        break