N, K = map(int, input().split())

room = [[0, 0] for _ in range(6)]

total_room = 0

for _ in range(N):
    S, Y = map(int, input().split())
    room[Y - 1][S] += 1

for i in range(6):
    for j in range(2):
        if room[i][j] == 0:
            continue
        else:
            if room[i][j] % K == 0:
                total_room += room[i][j] // K
            else:
                total_room += (room[i][j] // K) + 1

print(total_room)
