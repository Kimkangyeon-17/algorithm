N, D = map(int, input().split())

shortcut = []
for _ in range(N):
    start, end, length = map(int, input().split())
    shortcut.append((start, end, length))

dp = [float('inf')] * (D + 1)
dp[0] = 0

for i in range(D + 1):
    if dp[i] == float('inf'):
        continue

    if i + 1 <= D:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)

    for start, end, length in shortcut:
        if start == i and end <= D:
            dp[end] = min(dp[end], dp[i] + length)

print(dp[D])