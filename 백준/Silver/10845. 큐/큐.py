import sys

input = sys.stdin.readline

N = int(input())

que = []

for i in range(N):
    commands = input().split()
    command = commands[0]

    q_length = len(que)

    if command == 'push':
        val = int(commands[1])
        que.append(val)

    elif command == 'pop':
        if q_length == 0:
            print(-1)
        else:
            print(que.pop(0))

    elif command == 'size':
        print(q_length)

    elif command == 'empty':
        if q_length == 0:
            print(1)
        else:
            print(0)

    elif command == 'front':
        if q_length == 0:
            print(-1)
        else:
            print(que[0])

    elif command == 'back':
        if q_length == 0:
            print(-1)
        else:
            print(que[-1])

