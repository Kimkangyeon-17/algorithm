from collections import deque

N = int(input())

numbers = list(map(int, input().split()))

balloons = deque(range(1, N+1))

values = deque(numbers)

arr = []

for i in range(N):
    removed_balloon = balloons.popleft()
    paper = values.popleft()
    arr.append(removed_balloon)

    if not balloons:
        break

    if paper > 0:
        balloons.rotate(-(paper - 1))
        values.rotate(-(paper - 1))

    else:
        balloons.rotate(-paper )
        values.rotate(-paper)

print(*arr)
