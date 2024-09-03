N, M = map(int, input().split())
A = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for p in range(i-1, j):
        A[p] = k

print(" ".join(map(str, A)))