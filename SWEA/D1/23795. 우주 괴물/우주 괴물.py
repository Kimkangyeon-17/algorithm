T = int(input())

for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    monster_x = 0
    monster_y = 0

    for x in range(N):
        for y in range(N):
            if table[x][y] == 2:
                monster_x = x
                monster_y = y
                break

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        for step in range(1, N):
            nx = monster_x + dx[i] * step
            ny = monster_y + dy[i] * step
            if 0 <= nx < N and 0 <= ny < N:
                if table[nx][ny] == 1:
                    break
                elif table[nx][ny] == 0:
                    table[nx][ny] = 3
            else:
                break
    count = 0
    for x in range(N):
        for y in range(N):
            if table[x][y] == 0:
                count += 1

    print(f"#{tc} {count}")