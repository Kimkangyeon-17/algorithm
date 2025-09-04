import sys
sys.setrecursionlimit(200000)

N = int(input())

animals = [''] * (N + 1)  # 섬의 동물 종류 ('W' 또는 'S')
counts = [0] * (N + 1)    # 섬의 동물 수
parent = [0] * (N + 1)    # 섬의 부모 섬 (i번 섬의 pi값)
children = [[] for _ in range(N + 1)]  # 섬의 자식 섬들

for i in range(2, N + 1):
    t, a, p = input().split()
    a = int(a)
    p = int(p)
    animals[i] = t
    counts[i] = a
    parent[i] = p
    children[p].append(i)


def dfs(island):
    total_sheep = 0
    sheep = 0

    for child in children[island]:
        sheep += dfs(child)

    if animals[island] == "S":
        total_sheep = counts[island] + sheep

    elif animals[island] == "W":
        total_sheep = max(0, sheep - counts[island])

    else:
        total_sheep = sheep

    return total_sheep

answer = dfs(1)
print(answer)