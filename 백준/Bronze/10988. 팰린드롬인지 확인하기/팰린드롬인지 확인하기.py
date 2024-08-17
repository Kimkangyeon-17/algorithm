def palindrom(w):
    if w == w[::-1]:
        return 1
    else:
        return 0

w = input()

print(palindrom(w))