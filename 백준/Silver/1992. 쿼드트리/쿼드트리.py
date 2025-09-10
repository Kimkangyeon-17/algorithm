N = int(input())

grid = [list(map(int,input())) for _ in range(N)]

def is_same(grid, x, y, size):
    first_value = grid[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if grid[i][j] != first_value:
                return False
    return True

def compress(grid, x, y, size):
    if is_same(grid, x, y, size):
        return str(grid[x][y])

    half = size//2

    top_left = compress(grid, x, y, half)
    top_right = compress(grid, x, y + half, half)
    bottom_left = compress(grid, x + half, y, half)
    bottom_right = compress(grid, x + half, y + half, half)

    return "(" + top_left + top_right + bottom_left + bottom_right + ")"

result = compress(grid, 0,0 , N)
print(result)