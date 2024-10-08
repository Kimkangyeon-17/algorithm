# 입력 처리 및 집합을 이용한 풀이
from sys import stdin

input = stdin.readline

# N: 집합 S에 포함된 문자열의 수, M: 검사해야 할 문자열의 수
N, M = map(int, input().split())

# 집합 S에 포함된 문자열을 저장할 Set
S = set()

# N개의 문자열을 집합 S에 삽입
for _ in range(N):
    word = input().strip()  # 문자열 입력 받기
    S.add(word)

# M개의 문자열 중 S에 포함된 문자열의 개수를 셈
count = 0
for _ in range(M):
    word = input().strip()  # 검사할 문자열 입력 받기
    if word in S:  # 집합 S에 포함되어 있으면 count 증가
        count += 1

# 결과 출력
print(count)