N = int(input())  # 스위치 개수
Switch = list(map(int, input().split()))
Stu = int(input())  # 학생 수

for _ in range(Stu):
    Gnd, Num = map(int, input().split())

    if Gnd == 1:  # 남학생
        for j in range(Num-1, N, Num):
            Switch[j] = 1 - Switch[j]

    elif Gnd == 2:  # 여학생
        idx = Num - 1
        Switch[idx] = 1 - Switch[idx]

        l, r = idx - 1, idx + 1
        while l >= 0 and r < N and Switch[l] == Switch[r]:
            Switch[l] = 1 - Switch[l]
            Switch[r] = 1 - Switch[r]
            l -= 1
            r += 1

# 출력: 한 줄에 20개씩
for i in range(N):
    print(Switch[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
