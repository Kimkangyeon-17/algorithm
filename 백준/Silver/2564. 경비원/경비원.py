N, M = map(int, input().split())

store_count = int(input())


def get_pos(direction, dot):
    if direction == 1:
        return dot
    elif direction == 2:
        return N + M + N - dot
    elif direction == 3:
        return N + M + N + M - dot
    elif direction == 4:
        return dot + N

stores = []
for _ in range(store_count):
    direction, dot = map(int, input().split())
    stores.append(get_pos(direction, dot))

d, dot = map(int, input().split())
dong = get_pos(d, dot)

total = 0
perimeter = 2 * (N+M)

for store in stores:
    dist1 = abs(store - dong)
    dist2 = perimeter - dist1
    total += min(dist1, dist2)

print(total)