n, m = map(int,input().split())
cards = list(map(int,input().split()))

best_sum = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            card_sum = cards[i] + cards[j] + cards[k]

            if card_sum <= m:
                best_sum = max(best_sum, card_sum)

print(best_sum)