def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False


N = int(input())
parent = [i for i in range(N + 1)]

costs = [list(map(int, input().split())) for _ in range(N)]
total_cost = 0

for i in range(N):
    for j in range(i + 1, N):
        if costs[i][j] < 0:
            union(i + 1, j + 1)
            total_cost += abs(costs[i][j])

edges = []
for i in range(N):
    for j in range(i + 1, N):
        if costs[i][j] > 0:
            edges.append((costs[i][j], i + 1, j + 1))

edges.sort()

new_rail = []
new_cost = 0
for cost, c1, c2 in edges:
    if union(c1, c2):
        new_rail.append((c1, c2))
        new_cost += cost

total_cost += new_cost
print(total_cost, len(new_rail))

for c1, c2 in new_rail:
    print(c1, c2)