N = int(input())
A, B = map(int, input().split())
C = int(input())

toping_calories = []
for _ in range(N):
    D = int(input())
    toping_calories.append(D)

toping_calories.sort(reverse=True)

# 토핑 없이 도우만 먹는 경우
max_efficiency = C // A

# 토핑을 하나씩 추가해 가면서 최대 효율 찾기
current_calories = C  # 현재 총 칼로리 

for i in range(N):
    current_calories += toping_calories[i]  # 토핑 칼로리 추가
    current_price = A + B * (i + 1)  # 현재 총 가격
    current_efficiency = current_calories // current_price  # 현재 1원당 칼로리

    max_efficiency = max(max_efficiency, current_efficiency)

print(max_efficiency)
