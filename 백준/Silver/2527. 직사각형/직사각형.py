def cal(x1, y1, p1, q1, x2, y2, p2, q2):
    left = max(x1, x2)
    right = min(p1, p2)
    bottom = max(y1, y2)
    top = min(q1, q2)

    if left > right or bottom > top:
        return "d"
    elif left == right and bottom == top:
        return 'c'
    elif left == right or bottom == top:
        return 'b'
    else:
        return 'a'

for _ in range(4):
    numbers = list(map(int, input().split()))
    x1, y1, p1, q1 = numbers[:4]
    x2, y2, p2, q2 = numbers[4:]

    result = cal(x1, y1, p1, q1, x2, y2, p2, q2)

    print(result)