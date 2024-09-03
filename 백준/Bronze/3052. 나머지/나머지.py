A = set()

for _ in range(10):
    i = int(input())
    A.add(i % 42)

B = len(A)

print(B)