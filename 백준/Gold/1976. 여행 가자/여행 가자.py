def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x


N = int(input())
M = int(input())

parent = [i for i in range(N + 1)]

for i in range(N):
    connections = list(map(int, input().split()))

    for j in range(N):
        if connections[j] == 1:
            union(i + 1, j + 1)


plans = list(map(int, input().split()))

possible = True

first_city = find(plans[0])

for city in plans:
    if find(city) != first_city:
        possible = False
        break
if possible:
    print("YES")
else:
    print("NO")