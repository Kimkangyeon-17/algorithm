N = int(input())

# 첫 번째 피라미드 (1부터 N까지)
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))

# 두 번째 피라미드 (N-1부터 1까지)
for i in range(N - 1, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))