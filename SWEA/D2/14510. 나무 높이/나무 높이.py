T = int(input())

for test_case in range(1, T + 1):
    N = int(input().strip())
    trees = list(map(int, input().split()))

    max_tree = max(trees)
    twos = 0
    ones = 0

    for tree in trees:
        twos += (max_tree - tree) // 2
        ones += (max_tree - tree) % 2

    # print(f"{ones} {twos}")

    day = 0
    while True:
        if ones == 0 and twos == 0:
            break
        day += 1
        if day % 2 == 1: # 홀수날일 때
            if ones: # 1이 필요한 나무가 있으면
                ones -= 1 # 1씩 성장 시키기
            else: # 1일 필요한 나무가 없으면
                if ones+1 <= twos-1: # 조건 체크해서 2씩 필요한 나무가 더 많으면 2를 1씩 쪼개기
                    twos -= 1
                    ones += 1
        else: # 짝수날
            if twos: # 2가 필요한 나무가 있으면
                twos -= 1 # 2씩 성장
    print(f"#{test_case} {day}")