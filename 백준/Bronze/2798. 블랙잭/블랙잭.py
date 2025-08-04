N, M = map(int, input().split())

cards = list(map(int, input().split()))

best_sum = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            card_sum = cards[i] + cards[j] + cards[k]

            if card_sum <= M:
                best_sum = max(card_sum, best_sum)

print(best_sum)
