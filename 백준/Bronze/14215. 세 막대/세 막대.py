a, b, c = map(int, input().split())

A = sorted([a, b, c])

if A[0] + A[1] > A[2]:
    print(A[0] + A[1] + A[2])

else:
    print((A[0] + A[1])*2 -1)