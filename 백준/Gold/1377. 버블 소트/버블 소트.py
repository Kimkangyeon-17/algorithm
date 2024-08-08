import sys
input = sys.stdin.readline

n = int(input())
A = []

for i in range(n):
    A.append((int(input()),i))

Max = 0
Sorted_A = sorted(A)

for i in range(n):
    if Max < Sorted_A[i][1] - i:
        Max = Sorted_A[i][1] - i

print(Max+1)