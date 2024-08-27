import sys

input = sys.stdin.readline

while True:
    line = input().strip()

    if not line:
        break

    A, B = map(int, line.split())

    if A == 0 and B == 0:
        break
        
    print(A + B)
