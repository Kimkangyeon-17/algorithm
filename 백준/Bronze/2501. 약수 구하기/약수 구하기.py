N, K = map(int, input().split())
A = []

for i in range(1, N+1):
    if N % int(i) == 0:
        A.append(i)

if len(A) >= K:
    print(A[K-1])
else:
    print(0)