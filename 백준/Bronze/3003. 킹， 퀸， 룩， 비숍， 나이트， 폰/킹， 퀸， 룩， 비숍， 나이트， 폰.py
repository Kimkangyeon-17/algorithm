A = [1, 1, 2, 2, 2, 8]
B = []

N = list(map(int,input().split()))

for i in range(6):
    C = A[i] - N[i]
    B.append(C)

print(" ".join(map(str, B)))