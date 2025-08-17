import sys
input = sys.stdin.readline

N = int(input())
table = [[0] * 1001 for _ in range(1001)]

for i in range(N):
    x1, y1, width, height = map(int, input().split())

    for y in range(y1, y1 + height):
        table[y][x1:(x1 + width)] = [i + 1] * width


for i in range(N):
    target_num = i + 1
    total = 0

    for row in range(1001):
        total += table[row].count(target_num)

    print(total)