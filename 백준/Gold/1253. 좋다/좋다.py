import sys
input = sys.stdin.readline

n = int(input())
Result = 0
A = list(map(int,input(). split()))
A.sort()

for k in range(n):
    find = A[k]
    i = 0
    j = n-1
    while i < j:
        if A[i] + A[j] == find:
            if i != k and j != k:
                Result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1

        elif A[i] + A[j] < find:
            i += 1

        else:
            j -= 1

print(Result)