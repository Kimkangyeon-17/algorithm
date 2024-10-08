def find_generator(N):
    # 탐색 범위를 결정 (N - 9 * N의 자리수) 부터 시작
    start = max(1, N - 9 * len(str(N)))
    for i in range(start, N):
        total = i + sum(map(int,str(i)))

        if total == N :
            return i
    return 0

N = int(input())
print(find_generator(N))