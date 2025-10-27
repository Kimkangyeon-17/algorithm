from collections import deque

N, W, L = map(int, input().split())

trucks = list(map(int, input().split()))

queue = deque()

bridge = deque([0] * W)
weight = 0
time = 0
index = 0

while index < N or weight > 0:
    time += 1

    exit = bridge.popleft()
    weight -= exit

    if index < N:
        if weight + trucks[index] <= L:
            bridge.append(trucks[index])
            weight += trucks[index]
            index += 1
        else:
            bridge.append(0)
    else:
        bridge.append(0)

print(time)