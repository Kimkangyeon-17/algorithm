import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    a, b = map(int,line.split())

    if a == 0 and b == 0:
        break

    print(a+b)
