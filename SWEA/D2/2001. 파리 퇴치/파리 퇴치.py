T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]

    max_total = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            total = 0
            for i in range(M):
                for j in range(M):
                    total += table[x+i][y+j]

            max_total = max(max_total, total)

    print(f"#{tc} {max_total}")