def count_croatian_alphabets(word):
    croatian_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

    for alphabet in croatian_alphabets:
        word = word.replace(alphabet, '*')

    return len(word)

word = input().strip()

print(count_croatian_alphabets(word))