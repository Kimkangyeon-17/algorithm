T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    # 화폐 종류 (큰 것부터)
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []
    
    for coin in money:
        count = N // coin  # 해당 화폐로 몇 개 사용할지
        result.append(count)
        N = N % coin  # 남은 금액
    
    print(f"#{tc}")
    print(*result)