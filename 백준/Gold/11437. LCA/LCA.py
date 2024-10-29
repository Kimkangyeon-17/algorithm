import sys
import math
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

# 입력 받기
N = int(input())
tree = [[] for _ in range(N + 1)]

# 트리 구성
for _ in range(N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

# 깊이, 부모 정보 초기화
depth = [0] * (N + 1)
visited = [False] * (N + 1)
max_k = int(math.log2(N)) + 1
parent = [[0] * max_k for _ in range(N + 1)]

# BFS로 깊이와 첫 번째 부모 설정
def BFS(root):
    queue = deque([root])
    visited[root] = True
    while queue:
        node = queue.popleft()
        for next_node in tree[node]:
            if not visited[next_node]:
                visited[next_node] = True
                depth[next_node] = depth[node] + 1
                parent[next_node][0] = node
                queue.append(next_node)

# 희소 테이블 생성
def set_sparse_table():
    for j in range(1, max_k):
        for i in range(1, N + 1):
            parent[i][j] = parent[parent[i][j - 1]][j - 1]

# LCA 계산 함수
def LCA(a, b):
    # 깊이를 동일하게 맞추기
    if depth[a] < depth[b]:
        a, b = b, a

    # a를 b의 깊이에 맞추기
    for i in range(max_k - 1, -1, -1):
        if depth[a] - (1 << i) >= depth[b]:
            a = parent[a][i]

    # 공통 조상 찾기
    if a == b:
        return a

    for i in range(max_k - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

# 루트에서 BFS 시작
BFS(1)
# 희소 테이블 설정
set_sparse_table()

# 쿼리 처리
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(str(LCA(a, b)) + "\n")
