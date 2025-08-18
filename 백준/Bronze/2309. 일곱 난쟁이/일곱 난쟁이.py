numbers = []

for _ in range(9):
    N = int(input())
    numbers.append(N)

total = sum(numbers)
target = total - 100


found = False
for i in range(9):
    if found:
        break
    for j in range(i+1, 9):
        if numbers[i] + numbers[j] == target:
            remove_idx = {i, j}
            found = True
            break


result = []
for i in range(9):
    if i not in remove_idx:
        result.append(numbers[i])

result.sort()

for h in result:
    print(h)