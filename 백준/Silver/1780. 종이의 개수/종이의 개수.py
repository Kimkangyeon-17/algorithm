count = [0, 0, 0]

def is_same(x, y, size):
    first_val = papers[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if papers[i][j] != first_val:
                return None

    return first_val

def solve(x, y, size):

    result = is_same(x, y, size)

    if result is not None:
        count[result + 1] += 1
    else:
        new_size = size // 3

        for i in range(3):
            for j in range(3):
                solve(x + i * new_size, y + j * new_size, new_size)

N = int(input())

papers = [list(map(int, input().split())) for _ in range(N)]


solve(0, 0, N)

print(count[0])
print(count[1])
print(count[2])