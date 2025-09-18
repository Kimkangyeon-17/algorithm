C, N = map(int, input().split())

cities = []

for _ in range(N):
    cost, customer = map(int, input().split())
    cities.append((cost, customer))

dp = [float('inf')] * (C + 1)

dp[0] = 0

for i in range(C + 1):
    if dp[i] == float('inf'):
        continue

    for cost, customer in cities:
        next_customer = min(C, i + customer)
        dp[next_customer] = min(dp[next_customer], dp[i] + cost)

print(dp[C])