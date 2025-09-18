def is_star(i, j, size):
    while size > 1:
        size //= 3
        if (i // size) % 3 == 1 and (j // size) % 3 == 1:
            return False
    return True

n = int(input())

for i in range(n):
    line = ""
    for j in range(n):
        if is_star(i, j, n):
            line += "*"
        else:
            line += " "
    print(line)