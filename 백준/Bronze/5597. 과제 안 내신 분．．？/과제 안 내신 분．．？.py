A = set(range(1, 31))

for _ in range(28):
    i = int(input())
    A.remove(i)

B = sorted(A)

print(B[0])
print(B[1])