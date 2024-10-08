import sys
sys.setrecursionlimit(10**6)

N = int(input())
visited = [False] * N
tree = [[] for _ in range(N)]
answer = 0
p = list(map(int, input().split()))

for i in range(N):
    if p[i] != -1 :
        tree[i].append(i)
        tree[p[i]].append(i)
    else:
        root = i

# DFS 탐색 함수
def DFS(number):
    global answer
    visited[number] = True
    cNode = 0
    for i in tree[number]:
        if not visited[i] and i != deleteNode: # 삭제 노드일 때도 탐색 중지
            cNode += 1
            DFS(i)
    if cNode == 0:
        answer += 1

deleteNode = int(input())

if deleteNode == root:
    print(0)
else:
    DFS(root)
    print(answer)