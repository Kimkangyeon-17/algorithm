N, M = map(int, input().split())

A = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    A[i-1], A[j-1] = A[j-1], A[i-1]

print(" ".join(map(str,A)))