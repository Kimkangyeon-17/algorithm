import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
treeHeight = 0
length = N

while length != 0:
    length //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStrartIndex = treeSize // 2 - 1
tree = [0] * (treeSize + 1)

# 데이터를 리프 노드에 저장
for i in range(leftNodeStrartIndex + 1, leftNodeStrartIndex + N + 1):
    tree[i] = int(input())

# 인덱스 트리 생성 함수
def setTree(i):
    while i != 1:
        tree[i // 2] += tree[i]
        i-= 1

setTree(treeSize - 1)

# 값 변경 함수
def changeVal(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] = tree[index] + diff
        index = index // 2

# 구간 합 계산 함수
def getSum(s, e):
    partSum = 0
    while s <= e:
        if s % 2 == 1:
            partSum += tree[s]
            s += 1
        if e % 2 == 0:
            partSum += tree[e]
            e -= 1
        s = s // 2
        e = e // 2
    return partSum

for _ in range(M + K):
    question, s, e = map(int, input().split())
    if question == 1:
        changeVal(leftNodeStrartIndex + s, e)
    elif question == 2:
        s = s + leftNodeStrartIndex
        e = e + leftNodeStrartIndex
        print(getSum(s, e))