S = input()
A = [-1] * 26

for i, j in enumerate(S):
    char_index = ord(j) - ord('a')
    if A[char_index] == -1:
        A[char_index] = i

print(' '.join(map(str, A)))