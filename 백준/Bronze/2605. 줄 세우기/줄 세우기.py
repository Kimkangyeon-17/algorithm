N = int(input())
numbers = list(map(int, input().split()))

arr = []
for i in range(N):
    student = i+1
    move = numbers[i]

    position = len(arr) - move
    arr.insert(position, student)

print(*arr)