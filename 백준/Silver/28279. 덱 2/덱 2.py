import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

myque = deque()
result = []

for _ in range(N):
    command = list(map(int, input().split()))

    if command[0] == 1:
        myque.appendleft(command[1])

    elif command[0] == 2:
        myque.append(command[1])

    elif command[0] == 3:
        if myque:
            result.append(myque.popleft())
        else:
            result.append(-1)

    elif command[0] == 4:
        if myque:
            result.append(myque.pop())
        else:
            result.append(-1)

    elif command[0] == 5:
        result.append(len(myque))

    elif command[0] == 6:
        if myque:
            result.append(0)
        else:
            result.append(1)

    elif command[0] == 7:
        if myque:
            result.append(myque[0])
        else:
            result.append(-1)

    elif command[0] == 8:
        if myque:
            result.append(myque[-1])
        else:
            result.append(-1)

print('\n'.join(map(str, result)))
