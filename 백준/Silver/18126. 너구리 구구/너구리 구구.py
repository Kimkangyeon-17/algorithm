import sys
sys.setrecursionlimit(10000) 

N = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    A, B, C = map(int, input().split())

    graph[A].append((B, C))
    graph[B].append((A, C))

def dfs(current, parent):
    max_distance = 0

    for next_room, distance in graph[current]:
        if next_room != parent:
            result = dfs(next_room, current)
            total_distance = distance + result
            max_distance = max(max_distance, total_distance)

    return max_distance

answer = dfs(1, -1)

print(answer)