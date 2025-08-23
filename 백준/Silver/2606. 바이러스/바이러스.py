def solve_dfs():

    N = int(input())
    Target = int(input())

    nodes = [[] for _ in range(N+1)]

    for _ in range(Target):
        s, e = map(int, input().split())
        nodes[s].append(e)
        nodes[e].append(s)

    visited = [False] * (N + 1)

    def dfs(node):
        visited[node] = True
        count = 0

        for i in nodes[node]:
            if not visited[i]:
                count += 1 + dfs(i)

        return count

    return dfs(1)

print(solve_dfs())
