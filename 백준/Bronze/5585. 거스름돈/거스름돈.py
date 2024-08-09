def calc_change(payment):
    change = 1000 - payment
    coins = [500, 100, 50, 10, 5, 1]
    count = 0

    for coin in coins:
        count += change//coin
        change %= coin

    return count

payment = int(input())

result = calc_change(payment)

print(result)