import math
N = int(input())
A = [0] * (10000001)

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A))+1)):
    if A[i] == 0:
        continue
    for j in range(i + i, len(A), i):
        A[j] = 0

def isPallindrome(target):
    temp = list(str(target))
    s = 0
    e = len(temp) - 1
    while (s < e):
        if temp[s] != temp[e]:
            return False
        s += 1
        e -= 1
    return True

i = N

while True:
    if A[i] != 0:
        result = A[i]
        if (isPallindrome(result)):
            print(result)
            break
    i += 1