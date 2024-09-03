N = int(input())
A = list(map(int, input().split()))

M = max(A)

New_A = [(i/M) * 100 for i in A]
average = sum(New_A) / N

print(average)