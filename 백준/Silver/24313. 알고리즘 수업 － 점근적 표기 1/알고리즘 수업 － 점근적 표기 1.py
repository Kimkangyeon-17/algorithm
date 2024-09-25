# 입력 받기
a1, a0 = map(int, input().split())  # f(n)의 계수 a1, a0
c = int(input())  # 상수 c
n0 = int(input())  # 상수 n0

# 조건 확인
if a1 <= c:  # a1 - c <= 0이면 항상 만족
    # n >= n0에서 항상 만족하므로 1을 출력
    if (a1 - c) * n0 <= -a0:
        print(1)
    else:
        print(0)
else:
    print(0)
