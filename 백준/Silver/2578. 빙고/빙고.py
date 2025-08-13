bingo = [list(map(int, input().split())) for _ in range(5)]

numbers = []
for _ in range(5):
    line = list(map(int, input().split()))
    numbers.extend(line)

for turn in range(25):
    num = numbers[turn]

    for x in range(5):
        for y in range(5):
            if bingo[x][y] == num:
                bingo[x][y] = 0

    count = 0

    for i in range(5):
        if bingo[i] == [0, 0, 0, 0, 0]:
            count += 1

    for j in range(5):
        if [bingo[0][j], bingo[1][j], bingo[2][j], bingo[3][j], bingo[4][j]] == [0, 0, 0, 0, 0]:
            count += 1

    if [bingo[0][0], bingo[1][1], bingo[2][2], bingo[3][3], bingo[4][4]] == [0, 0, 0, 0, 0]:
        count += 1

    if [bingo[0][4], bingo[1][3], bingo[2][2], bingo[3][1], bingo[4][0]] == [0, 0, 0, 0, 0]:
        count += 1

    if count >= 3:
        print(turn + 1)
        break