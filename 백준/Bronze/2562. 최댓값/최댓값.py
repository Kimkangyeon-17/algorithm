result = []
for _ in range(9):
    a = int(input())
    result.append(a)

A = max(result)
index = result.index(A) + 1

print(A)
print(index)