def calculate_supervisors(N, A, B, C):
    total_supervisors = 0

    for students in A:
        # 총감독관은 반드시 1명 필요
        total_supervisors += 1
        students -= B

        # 부감독관이 필요한 경우
        if students > 0:
            total_supervisors += (students + C - 1) // C

    return total_supervisors


# 입력 처리
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

# 필요한 감독관의 최소 수 계산
result = calculate_supervisors(N, A, B, C)

# 결과 출력
print(result)