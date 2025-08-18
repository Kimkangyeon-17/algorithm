n = int(input())
max_length = 0
best_sequence = []

for second in range(1, n + 1):
    sequence = [n, second]

    while True:
        next_num = sequence[-2] - sequence[-1]
        if next_num < 0:
            break
        sequence.append(next_num)

    if len(sequence) > max_length:
        max_length = len(sequence)
        best_sequence = sequence[:]

print(max_length)
print(*best_sequence)