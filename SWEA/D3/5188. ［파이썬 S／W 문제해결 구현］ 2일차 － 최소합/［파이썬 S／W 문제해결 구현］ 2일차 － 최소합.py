def solve(col, row, current_total):
    global min_total

    if current_total >= min_total:
        return

    if col == N - 1 and row == N - 1:
        min_total = min(min_total, current_total)

    if col + 1 < N:
        solve(col + 1, row, current_total + numbers[row][col+1])

    if row + 1 < N:
        solve(col, row + 1, current_total + numbers[row+1][col])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    min_total = float('inf')

    solve(0, 0, numbers[0][0])

    print(f"#{tc} {min_total}")