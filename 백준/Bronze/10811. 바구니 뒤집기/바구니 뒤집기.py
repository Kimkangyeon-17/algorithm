N, M = map(int, input().split())
A = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, input().split())
    A[i-1:j] = A[i-1:j][::-1]

print(" ".join(map(str, A)))