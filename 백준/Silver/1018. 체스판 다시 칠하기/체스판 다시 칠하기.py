N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

chess_W = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]

chess_B = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]

def count_Repaint(x, y):
    count_w = 0
    count_b = 0
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != chess_W[i][j]:
                count_w += 1
            if board[x + i][y + j] != chess_B[i][j]:
                count_b += 1
    return min(count_w, count_b)

min_repaint = float('inf')

for i in range(N-7):
    for j in range(M-7):
        repaints = count_Repaint(i, j)
        min_repaint = min(min_repaint, repaints)

print(min_repaint)