N = int(input())
group_word_count = 0

for _ in range(N):
    word = input()
    error = False

    seen = []

    for i in range(len(word)):
        if i > 0 and word[i] != word[i - 1]:
            if word[i] in seen:
                error = True
                break
        seen.append(word[i])

    if not error:
        group_word_count += 1

print(group_word_count)