def isFrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i ==0:
            return False
    return True

M = int(input())
N = int(input())

A = []

for i in range(M, N+1):
    if isFrime(i):
        A.append(i)

if A:
    print(sum(A))
    print(min(A))
else:
    print(-1)