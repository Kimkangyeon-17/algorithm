N, M = map(int, input().split())

I = str(N)
J = I[::-1]

K = str(M)
L = K[::-1]

if int(J) > int(L):
    print(J)
else:
    print(L)